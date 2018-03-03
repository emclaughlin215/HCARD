#include <Wire.h>
#include <TinyWireM.h>
#include <USI_TWI_Master.h>

// MPU-6050 Short Example Sketch
// By Arduino User JohnChi
// August 17, 2014
// Public Domain

// Global variables 
const int MPU_addr=0x68;  // I2C address of the MPU-6050
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;
int16_t AcXoff,AcYoff,AcZoff,Tmpoff,GyXoff,GyYoff,GyZoff;
int16_t AcXoffavg,AcYoffavg,AcZoffavg,Tmpoffavg,GyXoffavg,GyYoffavg,GyZoffavg;

// Calibration Code Global variables
int limit = 100; 
int32_t Xstore = 0;
int32_t Ystore = 0;
int32_t Zstore = 0;
int32_t GXstore = 0;
int32_t GYstore = 0;
int32_t GZstore = 0;
int CalibrationDone = 0; 

void setup(){
  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Serial.begin(9600);
}


void loop(){


  // Calibration code 
  if (CalibrationDone == 0){
    int i; 
    for(i = 1; i< limit; i +=1){
    // This block of code must be executed each time IMU is read 
    Wire.beginTransmission(MPU_addr);
    Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
    Wire.endTransmission(false);
    Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers

    // Depermining the offset 
    AcXoff=Wire.read()<<8|Wire.read();   
    Xstore = Xstore + AcXoff;             //Storing the accumulated offset 
    AcYoff=Wire.read()<<8|Wire.read();  
    Ystore = Ystore + AcYoff;             //Storing the accumulated offset 
    AcZoff=Wire.read()<<8|Wire.read(); 
    Zstore = Zstore + AcZoff;             //Storing the accumulated offset 
    Tmpoff=Wire.read()<<8|Wire.read();  
    GyXoff=Wire.read()<<8|Wire.read();  
    GXstore = GXstore + GyXoff;           //Storing the accumulated offset 
    GyYoff=Wire.read()<<8|Wire.read();  
    GYstore = GYstore + GyYoff;           //Storing the accumulated offset 
    GyZoff=Wire.read()<<8|Wire.read();  
    GZstore = GZstore + GyZoff;           //Storing the accumulated offset 
    delay(10);   
    }
    CalibrationDone = 1; 
  }

  // Averaging calculation, calculating the average offset for "limit" readings. 
  // This aveverage offset is then subtracted from the reading as the calibration 
  AcXoffavg = Xstore/limit;
  AcYoffavg = Ystore/limit;
  AcZoffavg = Zstore/limit;
  GyXoffavg = GXstore/limit;
  GyYoffavg = GYstore/limit;
  GyZoffavg = GZstore/limit;

  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
 
  AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
  AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  Tmp=Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
  GyX=Wire.read()<<8|Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  GyY=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  GyZ=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)
  Serial.print(" | AcX = "); Serial.print(AcX - AcXoffavg);
  Serial.print(" | AcY = "); Serial.print(AcY - AcYoffavg);
  Serial.print(" | AcZ = "); Serial.print(AcZ - AcZoffavg);
  Serial.print(" | Tmp = "); Serial.print(Tmp/340.00+36.53);  //equation for temperature in degrees C from datasheet
  Serial.print(" | GyX = "); Serial.print(GyX - GyXoffavg);
  Serial.print(" | GyY = "); Serial.print(GyY - GyYoffavg);
  Serial.print(" | GyZ = "); Serial.println(GyZ - GyZoffavg);
  delay(333);
} 


