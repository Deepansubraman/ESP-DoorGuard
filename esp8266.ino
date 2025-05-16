// File: esp8266_relay.ino

#include <ESP8266WiFi.h>

const char* ssid = "DEEPAN";
const char* password = "1234567890";

WiFiServer server(80);
const int relayPin = D1;

void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");
  }

  Serial.println("Connected to WiFi.");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (!client) return;

  String request = client.readStringUntil('\r');
  client.flush();

  if (request.indexOf("/on") != -1) {
    digitalWrite(relayPin, HIGH);
  } else if (request.indexOf("/off") != -1) {
    digitalWrite(relayPin, LOW);
  }

  client.print("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nOK");
  delay(1);
}
