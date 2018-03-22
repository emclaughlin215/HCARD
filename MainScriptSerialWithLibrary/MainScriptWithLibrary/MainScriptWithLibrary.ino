
/*********************************************************************
This sketch reads data from an MPU 6050 IMU, and sends it via 
serial to whatever device it is connected to. 

NB: It uses a library written in C

This sketch includes code supplied by Adafruit and Jeff Rowberg

The author of this sketch is David Jedeikin, and it has been developed
as part of an HCARD postgraduate project at Imperial College London 
*********************************************************************/
#include "Mainlibs.h"

// *************************** IMU INTRERRUPT PRESETUP ******************************** 
void dmpDataReady() {
    mpuInterrupt = true;
}

//***************************** HAPTIC PRE SETUP CODE ********************************* 

String HapticCommand = "Nan"; 
unsigned long PreviousMillis = 0; 
const long Interval = 500;          // Change here to change the vibration motor period 


//********************************* SETUP CODE ********************************* 

void setup() {
   
    SetupSerial(); 
    GetTrargetAngle(); 
    ButtonLEDSetup(); 
    HapticSetup(); 
    SetupIMU();
}

//********************************* MAIN PROGRAM ********************************* 

void loop() {
  
    Angle = GetAngle(); 
    Serial.println(Angle);

  //<<<<<<<<<<<<<<<<<<<<<<<<<<<< HAPTIC >>>>>>>>>>>>>>>>>>>>>>>>

  unsigned long CurrentMillis = millis(); 
  unsigned long CurrentInverval = CurrentMillis - PreviousMillis ; 

  
  // Check for Haptic Feedback command 
  if (CurrentInverval >  Interval){                
    digitalWrite(A0, LOW);
  }
  
    if (CurrentInverval >  Interval){                
    digitalWrite(A1, LOW);
  }

  // Check if angle == angle 
  int difference = Angle - TargetAngle;
  difference = abs(difference);  
  
  if (difference < 1) {
      Serial.println("Back Haptic");
      digitalWrite(A1, HIGH);   
      PreviousMillis = CurrentMillis; 
    }
    else if (HapticCommand == "back") {
      Serial.println("Back Haptic");
      digitalWrite(A1, HIGH);   
      PreviousMillis = CurrentMillis; 
    }  
  }



