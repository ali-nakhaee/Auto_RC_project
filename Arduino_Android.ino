//Motor A
const int motorPin1  = 5;  // Pin 14 of L293
const int motorPin2  = 6;  // Pin 10 of L293
//Motor B
const int motorPin3  = 9; // Pin  7 of L293
const int motorPin4  = 10;  // Pin  2 of L293
int power = 64; 


void setup()  
 {  
  Serial.begin(9600);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
 } 



  
 void loop() { 
  char order;
  if(Serial.available())  
  {  
   order = Serial.read();  
   Serial.print(order);  
  }
  int ord = order - '0'; //conver char(order) to int(ord)
 
  if (ord == 1) {
    analogWrite(motorPin1, power);
    digitalWrite(motorPin2, LOW);
    analogWrite(motorPin3, 2*power/3);
    digitalWrite(motorPin4, LOW);
  }

  if (ord == 2) {
    analogWrite(motorPin1, 2*power/3);
    digitalWrite(motorPin2, LOW);
    analogWrite(motorPin3, power);
    digitalWrite(motorPin4, LOW);
  }


  if (ord == 3) {
    analogWrite(motorPin1, power);
    digitalWrite(motorPin2, LOW);
    analogWrite(motorPin3, power);
    digitalWrite(motorPin4, LOW);
  }

  if (ord == 4) {
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, LOW);
  }

  if (ord > 4) {
    power = map(ord, 4, 9, 0, 255);      //get order between 4 and 9 and scale this to 0 and 255 for power
  }

 delay(20);
}





