#define led_pin 8

void setup()
{
    pinMode(led_pin, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    while (Serial.available() > 0)
    {
        int val = Serial.read();
        digitalWrite(led_pin, val);
    }
}
