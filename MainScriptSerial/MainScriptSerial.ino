
/*********************************************************************
This sketch reads data from an MPU 6050 IMU, and sends it via 
serial to whatever device it is connected to. 

This sketch includes code supplied by Adafruit and Jeff Rowberg

The author of this sketch is David Jedeikin, and it has been developed
as part of an HCARD postgraduate project at Imperial College London 
*********************************************************************/

// I2Cdev and MPU6050 must be installed as libraries, or else the .cpp/.h files
// for both classes must be in the include path of your project
#include "I2Cdev.h"

#include "MPU6050_6Axis_MotionApps20.h"
//#include "MPU6050.h" // not necessary if using MotionApps include file

// Arduino Wire library is required if I2Cdev I2CDEV_ARDUINO_WIRE implementation
// is used in I2Cdev.h
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

// class default I2C address is 0x68
// specific I2C addresses may be passed as a parameter here
// AD0 low = 0x68 (default for SparkFun breakout and InvenSense evaluation board)
// AD0 high = 0x69
MPU6050 mpu;
//MPU6050 mpu(0x69); // <-- use for AD0 high

/* =========================================================================
   NOTE: In addition to connection 3.3v, GND, SDA, and SCL, this sketch
   depends on the MPU-6050's INT pin being connected to the Arduino's
   external interrupt #0 pin. On the Arduino Uno and Mega 2560, this is
   digital I/O pin 2.
 * ========================================================================= */

/* =========================================================================
   NOTE: Arduino v1.0.1 with the Leonardo board generates a compile error
   when using Serial.write(buf, len). The Teapot output uses this method.
   The solution requires a modification to the Arduino USBAPI.h file, which
   is fortunately simple, but annoying. This will be fixed in the next IDE
   release. For more info, see these links:

   http://arduino.cc/forum/index.php/topic,109987.0.html
   http://code.google.com/p/arduino/issues/detail?id=958
 * ========================================================================= */


// uncomment "OUTPUT_READABLE_YAWPITCHROLL" if you want to see the yaw/
// pitch/roll angles (in degrees) calculated from the quaternions coming
// from the FIFO. Note this also requires gravity vector calculations.
// Also note that yaw/pitch/roll angles suffer from gimbal lock (for
// more info, see: http://en.wikipedia.org/wiki/Gimbal_lock)
#define OUTPUT_READABLE_YAWPITCHROLL


#define LED_PIN 13 // (Arduino is 13, Teensy is 11, Teensy++ is 6)
bool blinkState = false;

// MPU control/status vars
bool dmpReady = false;  // set true if DMP init was successful
uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
uint8_t devStatus;      // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount;     // count of all bytes currently in FIFO
uint8_t fifoBuffer[64]; // FIFO storage buffer

// orientation/motion vars
Quaternion q;           // [w, x, y, z]         quaternion container
VectorInt16 aa;         // [x, y, z]            accel sensor measurements
VectorInt16 aaReal;     // [x, y, z]            gravity-free accel sensor measurements
VectorInt16 aaWorld;    // [x, y, z]            world-frame accel sensor measurements
VectorFloat gravity;    // [x, y, z]            gravity vector
float euler[3];         // [psi, theta, phi]    Euler angle container
float ypr[3];           // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector

// packet structure for InvenSense teapot demo
uint8_t teapotPacket[14] = { '$', 0x02, 0,0, 0,0, 0,0, 0,0, 0x00, 0x00, '\r', '\n' };


// ================================================================
// ===               INTERRUPT DETECTION ROUTINE                ===
// ================================================================

volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high
void dmpDataReady() {
    mpuInterrupt = true;
}

// HAPTIC PRE SETUP CODE 
int TargetAngle; 
int Angle; 
String HapticCommand = "Nan"; 
unsigned long PreviousMillis = 0; 
const long Interval = 500;          // Change here to change the vibration motor period 
const long largeInterval = 3000;          // Change here to change the vibration motor period 
int ProgramStart = 0;               // Program Start variable 
int Step = 1; 

// ================================================================
// ===                      INITIAL SETUP                       ===
// ================================================================

void setup() {
    // join I2C bus (I2Cdev library doesn't do this automatically)
    #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
        Wire.begin();
        TWBR = 24; // 400kHz I2C clock (200kHz if CPU is 8MHz)
    #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
        Fastwire::setup(400, true);
    #endif

    // initialize serial communication
    Serial.begin(115200);

   // Wait for target angle
    while (!Serial.available()){}; 
    TargetAngle = Serial.parseInt();
    Serial.println(F("The target angle is: "));
    Serial.println(TargetAngle);

  // <<<<<<<<<<<<<<<<<<<<<<<<<<<<< LED AND BUTTON SETUP >>>>>>>>>>>>>>>>>>>>>> 
  pinMode(A3, OUTPUT);
  pinMode(A2, INPUT_PULLUP);
  digitalWrite(A3, HIGH);
  Serial.println("Press Button to Begin");         
  // MULTIPLE WHILE LOOPS ACTS AS A CRUDE DEBOUNCE 
  while(digitalRead(A2) != 0){}           // Hang while button isnt pressed 
  Serial.println(F("Button Pressed"));         
  int i; 
  for (i = 1; i < 5; i = i+1) {
    digitalWrite(A3, LOW);
    delay(200); 
    digitalWrite(A3, HIGH);
    delay(200); 
  }
    digitalWrite(A3, LOW);

    // initialize device
    Serial.println(F("Initializing I2C devices..."));
    mpu.initialize();

    // verify connection
    Serial.println(F("Testing device connections..."));
    Serial.println(mpu.testConnection() ? F("MPU6050 connection successful") : F("MPU6050 connection failed"));

    // wait for ready
    Serial.println(F("Read to Rumble!!!!"));
    //while (Serial.available() && Serial.read()); // empty buffer
    //while (!Serial.available());                 // wait for data
    //while (Serial.available() && Serial.read()); // empty buffer again

    // load and configure the DMP
    Serial.println(F("Initializing DMP..."));
    devStatus = mpu.dmpInitialize();
    
    // supply your own gyro offsets here, scaled for min sensitivity
    mpu.setXGyroOffset(49);
    mpu.setYGyroOffset(51);
    mpu.setZGyroOffset(14);
    mpu.setXAccelOffset(155); 
    mpu.setYAccelOffset(-247); 
    mpu.setZAccelOffset(868); 

    // make sure it worked (returns 0 if so)
    if (devStatus == 0) {
        // turn on the DMP, now that it's ready
        Serial.println(F("Enabling DMP..."));
        mpu.setDMPEnabled(true);

        // enable Arduino interrupt detection
        Serial.println(F("Enabling interrupt detection (Arduino external interrupt 0)..."));
        attachInterrupt(0, dmpDataReady, RISING);
        mpuIntStatus = mpu.getIntStatus();

        // set our DMP Ready flag so the main loop() function knows it's okay to use it
        Serial.println(F("DMP ready! Waiting for first interrupt..."));
        dmpReady = true;

        // get expected DMP packet size for later comparison
        packetSize = mpu.dmpGetFIFOPacketSize();
    } else {
        // ERROR!
        // 1 = initial memory load failed
        // 2 = DMP configuration updates failed
        // (if it's going to break, usually the code will be 1)
        Serial.print(F("DMP Initialization failed (code "));
        Serial.print(devStatus);
        Serial.println(F(")"));
    }

    // configure LED for output
    pinMode(LED_PIN, OUTPUT);

  // Haptic SetUp 
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  Serial.println(F("Press Button to Begin"));
}



// ================================================================
// ===                    MAIN PROGRAM LOOP                     ===
// ================================================================



void loop() {

     // Press button to start process
     if (ProgramStart == 0){
        while(digitalRead(A2) != 0){}           // Hang while button isnt pressed 
        ProgramStart = 1; 
     }

      // Main Program flow variables 
      int programCounter = 0;
      int holdInPlace = 0;  
      int waitTime = 400; 
      int zeroThreshold = 8; 
      int angleThreshold = 2; 
      while (programCounter <= 10) {

        //Debugging: 
        Serial.print("Current Step: "); 
        Serial.println(Step); 
        Serial.print("Target Angle: "); 
        Serial.println(TargetAngle); 
        
                
            // *********************************************************
            // IMU MAIN LOOP, DONT WORRY ABOUT THIS! 
            if (!dmpReady) return;
        
            // wait for MPU interrupt or extra packet(s) available
            while (!mpuInterrupt && fifoCount < packetSize) {
            }
        
            // reset interrupt flag and get INT_STATUS byte
            mpuInterrupt = false;
            mpuIntStatus = mpu.getIntStatus();
        
            // get current FIFO count
            fifoCount = mpu.getFIFOCount();
        
            // check for overflow (this should never happen unless our code is too inefficient)
            if ((mpuIntStatus & 0x10) || fifoCount == 1024) {
                // reset so we can continue cleanly
                mpu.resetFIFO();
                // CURRENTLY CODE IS INEFFICIENT 
                //Serial.println(F("FIFO overflow!"));
        
            // otherwise, check for DMP data ready interrupt (this should happen frequently)
            } else if (mpuIntStatus & 0x02) {
                // wait for correct available data length, should be a VERY short wait
                while (fifoCount < packetSize) fifoCount = mpu.getFIFOCount();
        
                // read a packet from FIFO
                mpu.getFIFOBytes(fifoBuffer, packetSize);
                
                // track FIFO count here in case there is > 1 packet available
                // (this lets us immediately read more without waiting for an interrupt)
                fifoCount -= packetSize;
        
                #ifdef OUTPUT_READABLE_YAWPITCHROLL
                    // display Euler angles in degrees
                    mpu.dmpGetQuaternion(&q, fifoBuffer);
                    mpu.dmpGetGravity(&gravity, &q);
                    mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
                    //Serial.print("ypr\t");
                    //Serial.print(ypr[0] * 180/M_PI);
                    //Serial.print("\t");
                    //Serial.print(ypr[1] * 180/M_PI);
                    //Serial.print("\t");
                    //0Serial.println(-ypr[2] * 180/M_PI);
                    Angle = -ypr[2] * 180/M_PI;
                    Angle = 90 - Angle;
                    Serial.println(Angle);
                   
                     
                #endif
        
                // blink LED to indicate activity
                blinkState = !blinkState;
                digitalWrite(LED_PIN, blinkState);
            }
            
            // *********************************************************
        
        
          //<<<<<<<<<<<<<<<<<<<< HAPTIC Control Commands >>>>>>>>>>>>>>>>>>>

          // ********************************************************
          //********************* TIMING CODE ***********************
          unsigned long CurrentMillis = millis(); 
          unsigned long CurrentInverval = CurrentMillis - PreviousMillis ;  
          if (CurrentInverval >  Interval){                
            digitalWrite(A0, LOW);
          }
          
            if (CurrentInverval >  Interval){                
            digitalWrite(A1, LOW);
          }
          // ********************************************************

          int difference = Angle - TargetAngle;
          int absDifference = abs(difference);  

          // Process flow switch case 
          switch (Step) {
            case 1:             // Set back haptic high to initiate rehab
              holdInPlace = 0;      // Reset hold in place variable  
              digitalWrite(A1, HIGH);   
              PreviousMillis = CurrentMillis; 
              Step = 2; 
              break;
            case 2:             // Set both haptics if target angle is reached
              if (absDifference < 2) {
                digitalWrite(A0, HIGH);  
                digitalWrite(A1, HIGH);  
                PreviousMillis = CurrentMillis;
                Step = 3; 
              }
                
              break;
            case 3:             // Wait for interval to complete
              if (holdInPlace <= waitTime && absDifference < angleThreshold){   //Only increment if within the threshold
                  holdInPlace++ ; 
              }
              if (holdInPlace > waitTime){
                  Step = 4; 
              }
              break;
            case 4: 
              holdInPlace = 0; 
              digitalWrite(A0, HIGH);   
              PreviousMillis = CurrentMillis; 
              Step = 5; 
              break;
            case 5: 
              if (Angle <= zeroThreshold) {
                digitalWrite(A0, HIGH);  
                digitalWrite(A1, HIGH);  
                PreviousMillis = CurrentMillis;
                Step = 6; 
            }  
              break;
            case 6:         // Wait for interval to complete
              if (holdInPlace <= waitTime && Angle < zeroThreshold){
                  holdInPlace++; 
              }
              if (holdInPlace > waitTime) {
                programCounter++ ; 
                Step = 1;
               }
              
              break;
            default:
              // Nothing 
              break;

          }
        
  }
  
}



