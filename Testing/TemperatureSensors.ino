// #include <OneWire.h>
// #include <DallasTemperature.h>

// #define ONE_WIRE_BUS 5
// OneWire oneWire(ONE_WIRE_BUS);
// DallasTemperature sensors(&oneWire);

void setup(void){
    Serial.begin(115200);
    delay(10);
    Serial.println("ESP Online");
    // sensors.begin();
}

void loop(void){
    // sensors.requestTemperatures();


    Serial.println(" Temperature: ");
    // Serial.println(sensors.getTempCByIndex(0));   
    delay(1000);
}