
// Includes
#include "Mainlibs.h" 
#include <Arduino.h>


// 1:<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Serial Setup>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
void SetupSerial(void){
  Serial.begin(115200);
  while (!Serial) ;           //Wait for serial 
  Serial.println("Serial Connected"); 
}

// 2:<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Target Angle Setup >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
void GetTrargetAngle(void){
     // Wait for target angle
    while (!Serial.available()){};
    TargetAngle = Serial.parseInt();
    Serial.println(F("The target angle is: "));
    Serial.println(TargetAngle);
}

// 3:<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Button & LED setup >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
void ButtonLEDSetup(void){
    Serial.begin(115200);     
    pinMode(A2,INPUT_PULLUP);
    pinMode(A3,OUTPUT);
    digitalWrite(A3,HIGH); 
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
}

// 4:<<<<<<<<<<<<<<<<<<<<<<<<<<<<< HAPTIC setup >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
void HapticSetup(void){
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
}

// 5:<<<<<<<<<<<<<<<<<<<<<<<<<<<<< IMU setup >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

void SetupIMU(void){
    // join I2C bus (I2Cdev library doesn't do this automatically)
    #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
        Wire.begin();
        TWBR = 24; // 400kHz I2C clock (200kHz if CPU is 8MHz)
    #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
        Fastwire::setup(400, true);
    #endif

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

}

// 6:<<<<<<<<<<<<<<<<<<<<<<<<<<<<< IMU setup >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

int GetAngle(void){
      // if programming failed, don't try to do anything
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

        
          // display Euler angles in degrees
          mpu.dmpGetQuaternion(&q, fifoBuffer);
          mpu.dmpGetGravity(&gravity, &q);
          mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
          //Serial.print("ypr\t");
          //Serial.print(ypr[0] * 180/M_PI);
          //Serial.print("\t");
          //Serial.print(ypr[1] * 180/M_PI);
          //Serial.print("\t");
          Serial.println(-ypr[2] * 180/M_PI);
          int AngleNow = -ypr[2] * 180/M_PI; 
          return AngleNow; 

        // blink LED to indicate activity
        blinkState = !blinkState;
        digitalWrite(LED_PIN, blinkState);
    }
}

