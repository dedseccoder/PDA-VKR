void setup() {
  Serial.begin(9600);
}

int current = 0;

void loop() {
  if (Serial.available())
  {
     if(analogRead(A0) != current)
    {
      current = analogRead(A0) / 10;
      if(current > 10)
      {
        Serial.println(current); 
      }
      else
      {
        Serial.println("------"); 
      }
    }
    delay(1000); 
  }
}
