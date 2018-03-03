#include <Wire.h>
#include <TinyWireM.h>
#include <USI_TWI_Master.h>

// MPU-6050 Short Example Sketch
// By Arduino User JohnChi
// August 17, 2014
// Public Domain
#include<Wire.h>
const int MPU_addr=0x68;  // I2C address of the MPU-6050
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;
int16_t AcXoff,AcYoff,AcZoff,Tmpoff,GyXoff,GyYoff,GyZoff;
int16_t AcXoffavg,AcYoffavg,AcZoffavg,Tmpoffavg,GyXoffavg,GyYoffavg,GyZoffavg;
int16_t AcXoffavgRunning; 

void setup(){
  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Serial.begin(9600);
}

// Calibration variable 
int i = 1 ;
int limit = 100; 
int32_t Xstore = 0;

void loop(){

  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
  
  //Calibration Code
  if(i <= limit){
  AcXoff=Wire.read()<<8|Wire.read();   
  Serial.print("AcXoff"), Serial.println(AcXoff); 
  Xstore = Xstore + AcXoff; 
  Serial.print("Xstore"), Serial.println(Xstore);
  AcYoff=Wire.read()<<8|Wire.read();  
  AcZoff=Wire.read()<<8|Wire.read(); 
  Tmpoff=Wire.read()<<8|Wire.read();  
  GyXoff=Wire.read()<<8|Wire.read();  
  GyYoff=Wire.read()<<8|Wire.read();  
  GyZoff=Wire.read()<<8|Wire.read();  
   AcXoffavgRunning = Xstore/i;
  Serial.print(" Running Average Xoff "); Serial.println(AcXoffavgRunning);
  i += 1; 
  delay(300);
  }

  //Averaging Calculation 
  AcXoffavg = Xstore/limit;
 
  if (i > limit){
  AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
  AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  Tmp=Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
  GyX=Wire.read()<<8|Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  GyY=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  GyZ=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)
  Serial.print(" | AcX = "); Serial.println(AcX - AcXoffavg);
//  Serial.print(" | AcY = "); Serial.print(AcY - AcYoff);
//  Serial.print(" | AcZ = "); Serial.print(AcZ - AcZoff);
//  Serial.print(" | Tmp = "); Serial.print(Tmp/340.00+36.53);  //equation for temperature in degrees C from datasheet
//  Serial.print(" | GyX = "); Serial.print(GyX - GyXoff);
//  Serial.print(" | GyY = "); Serial.print(GyY - GyYoff);
//  Serial.print(" | GyZ = "); Serial.println(GyZ - GyZoff);
  delay(333);
  }
}
