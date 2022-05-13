void setup() {
  Serial.begin(9600);
}

int inputValue = 0;

void loop() {
  
  sendStatus();
}

void sendStatus()
{
  char buffer[50];
  inputValue = analogRead(A0);

  if(inputValue / 10 > 10)
      {
         sprintf (buffer, "Pulse: %d", inputValue / 10);
      }
      else
      {
        sprintf (buffer, "Pulse: ----");
      }
      
      Serial.println(buffer);
}
