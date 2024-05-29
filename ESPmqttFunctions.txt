#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// WiFi credentials
const char* ssid = "Comunicacion";
const char* password = "123456789";

// MQTT broker details
const char* mqtt_server = "192.168.1.102"; // Replace with your broker
const char* mqtt_topic = "prub"; // Replace with your topic

WiFiClient espClient;
PubSubClient client(espClient);

// Define pins
const int pinW = D1; // GPIO5
const int pinA = D2; // GPIO4
const int pinS = D3; // GPIO0
const int pinD = D4; // GPIO2

// Function prototypes
void setup_wifi();
void callback(char* topic, byte* payload, unsigned int length);
void reconnect();
void onW();
void onA();
void onS();
void onD();

void setup() {
  Serial.begin(115200);

  // Initialize pins
  pinMode(pinW, OUTPUT);
  pinMode(pinA, OUTPUT);
  pinMode(pinS, OUTPUT);
  pinMode(pinD, OUTPUT);

  // Set all pins LOW initially
  digitalWrite(pinW, LOW);
  digitalWrite(pinA, LOW);
  digitalWrite(pinS, LOW);
  digitalWrite(pinD, LOW);

  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  
  char message = (char)payload[0];
  Serial.println(message);
  
  switch (message) {
    case 'w':
      onW();
      break;
    case 'a':
      onA();
      break;
    case 's':
      onS();
      break;
    case 'd':
      onD();
      break;
    default:
      Serial.println("Unknown command");
      break;
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      client.subscribe(mqtt_topic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void onW() {
  Serial.println("Function onW() called");
  digitalWrite(pinW, HIGH);
  delay(1000);
  digitalWrite(pinW, LOW);
}

void onA() {
  Serial.println("Function onA() called");
  digitalWrite(pinA, HIGH);
  delay(1000);
  digitalWrite(pinA, LOW);
}

void onS() {
  Serial.println("Function onS() called");
  digitalWrite(pinS, HIGH);
  delay(1000);
  digitalWrite(pinS, LOW);
}

void onD() {
  Serial.println("Function onD() called");
  digitalWrite(pinD, HIGH);
  delay(1000);
  digitalWrite(pinD, LOW);
}
