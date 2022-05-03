void setup() {
  Serial.begin(9600);
}

int current = 0;

void loop() {
  if(analogRead(A0) != current)
  {
    current = analogRead(A0) / 10;
    if(current > 20)
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
