

String HapticCommand = "nan";   // for incoming serial data
void setup() {
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  Serial.println(F("Select front or back haptic motor"));
}

  
void loop() {
  
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    HapticCommand = Serial.readString();

    if (HapticCommand == "front") {
      Serial.println("front Haptic");
      digitalWrite(A0, HIGH);   
      delay(1000);                     
      digitalWrite(A0, LOW);
      HapticCommand = "False";    
      //Serial.readString(); 
    }
    else if (HapticCommand == "back"){
      Serial.println("Back Haptic");
      digitalWrite(A1, HIGH);   
      delay(1000);                     
      digitalWrite(A1, LOW);
      HapticCommand = "False";  
    }
    
  }

}




