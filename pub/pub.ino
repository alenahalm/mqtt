#define sensor_pin 11

void setup()
{
    pinMode(sensor_pin, INPUT);
    Serial.begin(9600);
}

void loop()
{
    char val = digitalRead(sensor_pin) >> 2;
    Serial.write(val);
    delay(1000);
}