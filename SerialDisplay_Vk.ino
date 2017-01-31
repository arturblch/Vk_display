// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7,8,9,10,11,12);


int led = 6;      
int brightness = 0;   
int fadeAmount = 5; 
String msg,h,m,t;

byte newChar1[8] = {
  0b00010,
  0b00101,
  0b00010,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000
};

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
  Serial.println("Ready");
  pinMode(led, OUTPUT);
  lcd.createChar(0, newChar1);
}

void loop() {
  // when characters arrive over the serial port...
  if (msg[0] == 'Y'){
    digitalWrite(led,LOW);  
    delay(500);
    digitalWrite(led,HIGH);  
    delay(500);
  }
  else{
     digitalWrite(led,LOW);
  }
  
   
}

void serialEvent(){
    lcd.clear();
    while (Serial.available() > 0) {
      
      msg = Serial.readStringUntil('\n');
      t = Serial.readStringUntil('\n');
      h = Serial.readStringUntil('\n');
      m = Serial.readStringUntil('\n');
      lcd.setCursor(0, 0);
      lcd.print(msg);
      lcd.setCursor(0, 1);
      lcd.print(t);  
      lcd.write(byte(0));
      lcd.print("C");
      lcd.setCursor(11, 1);
      lcd.print(h+':'+m);    
}
}
