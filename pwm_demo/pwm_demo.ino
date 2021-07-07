

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  //to make a PWM signal with period 10 ms (100 Hz), the sum of the two
  //delays below need to be 10.
  
  digitalWrite(13, HIGH);
  delay(1); //delay for n ms time
   digitalWrite(13, LOW);
  delay(9); //delay for n ms time

}
