#include <Encoder.h>
#include <string.h>

float x = 0.0;  // Posición actual en X
float y = 0.0;  // Posición actual en Y
float theta = 0.0;  // Orientación actual del coche
//float xd = 0.0;  // Posición deseada en X
//float yd = 10.0;  // Posición deseada en Y
int t = 0.0;  // Tiempo inicial
int aux = 1; 
float d = 0; 
int grados = 0;
float radianes = 0.0; 

// Parámetros del coche
const float R = 0.03;  // Radio de llanta en metros
const float L = 0.28;  // Distancia entre llantas en metros

float vi = 0; //velocidad izquierda
float vd = 0; //velocidad derecha

// Constantes de control
float kpr = 2; //rotación
float kpt = 2; //traslación


// Motores 
// Input 1 y 2 para motor 1 (rueda izquierda)
// Input 3 y 4 para motor 2 (rueda derecha)
const int I2 = 10; //Input 2
const int D2 = 9;  //Input 4
const int I1 = 12; //Input 1
const int D1 = 8;  //Input 3

// Variables para almacenar la trayectoria
//char xdir[0,5,5,0]; 
//char ydir[5,5,0,0];
int num_puntos = 0;
char trayectoria_input[] = "0,5;5,5;5,0;0,0"; // Cuadrado




// Variables de estado actuales
float x_now = 0;
float y_now = 0;
float theta_now = 0;


// Tiempos
const float dt = 0.01;  // Intervalos de tiempo en segundos
int Tf = 10;

Encoder RightEnc(2, 3); // Pines Encoder
Encoder LeftEnc(18, 19); // Pines Encoder
//Encoder Enc1819(18, 19); //Pines Encoder
//Encoder Enc23(2, 3); //Pines Encoder

// Constantes del Encoder
const float PULSOS_POR_REV = 680.0; // Cambia esto según tu encoder
const float CIRCUNFERENCIA_RUEDA = 2 * PI * R;

void setup() {
  Serial.begin(9600);
  pinMode(D1, OUTPUT); 
  pinMode(D2, OUTPUT); 
  pinMode(I1, OUTPUT); 
  pinMode(I2, OUTPUT); 
}

long oldPosition  = -999;

void resetEncoders() {
  LeftEnc.write(0);
  RightEnc.write(0);
}

void desplazamiento(int xd, int yd) {
  t = 0; 
  resetEncoders(); 
  d = sqrt(pow(xd - x, 2) + pow(yd - y, 2));
  while (t < Tf) {

    long pulsosizq = LeftEnc.read();
    long pulsosdere = RightEnc.read();
    //Serial.print("Pulsos de Encoder");
    //Serial.println(pulsos);

    float actualizq = (abs(pulsosizq) * CIRCUNFERENCIA_RUEDA) / PULSOS_POR_REV;
    float actualder = (abs(pulsosdere) * CIRCUNFERENCIA_RUEDA) / PULSOS_POR_REV;
    float direccion_actual = (actualizq+actualder)/2;

    Serial.println(actualizq);
    Serial.println(actualder);


    // Control de dirección
    d = d-direccion_actual; 
    float v = kpt * d;

    // Detener si está cerca del objetivo
    if (d <= 0.1) {
      vd = 0;
      vi = 0; 
      t = 10; 
    }
    analogWrite(5,vi); 
    analogWrite(6,vd); 
    digitalWrite(10,LOW);
    digitalWrite(9,LOW);
    digitalWrite(12,HIGH);
    digitalWrite(8,HIGH);

    // Velocidades de llantas
    vi = v;
    vd = v;
    vi = vi;
    vd = vd;

    vi = map(vi,0, 400, 100, 255);  //1.1
    vd = map(vd, 0, 400, 100, 255)*1.03;

    //Serial.println(v);
    Serial.print("Velocidad derecha: ");
    Serial.println(vd);
    Serial.print("Velocidad izquierda: ");
    Serial.println(vi);
    Serial.print("distancia");
    Serial.println(d);

    
    // Actualizar el tiempo
    t += dt;
  }
}

void giro(int xd, int yd) {
  t = 0; 
  resetEncoders(); 
  while (t<Tf){
    
  float thetadir = ((atan2(yd - y, xd - x))/2)-0.0873;  //0.0873
  long pulsosLeft = LeftEnc.read();
  long pulsosRight = RightEnc.read();
  float distancia_recorridaLeft = (pulsosLeft / PULSOS_POR_REV) * CIRCUNFERENCIA_RUEDA;
  float distancia_recorridaRight = (pulsosRight / PULSOS_POR_REV) * CIRCUNFERENCIA_RUEDA;  
  
  if(yd > 0){ 
    Serial.print("antihorario\n");
    // Calcular el ángulo de giro
    theta = (-distancia_recorridaRight + distancia_recorridaLeft) / L;
    float thetae = (thetadir - abs(theta))*aux;  // Error angular
    float w = kpr * thetae;
    w = map(w,0,332,130,255);
    analogWrite(5,w);
    analogWrite(6,w);
    digitalWrite(I1, HIGH);
    digitalWrite(D2, HIGH);
    digitalWrite(I2, LOW);
    digitalWrite(D1, LOW);
    if(thetae<0){
      Serial.print("se acabo");
      analogWrite(5,0);
      analogWrite(6,0);
      digitalWrite(I1, LOW);
      digitalWrite(D2, LOW);
      digitalWrite(I2, LOW);
      digitalWrite(D1, LOW);
      t = 10; 
    }
  }
  else if(yd < 0){
    Serial.print("horario\n");
    theta = (distancia_recorridaRight - distancia_recorridaLeft) / L;
    float thetae = (abs(thetadir) - (theta))*aux;  // Error angular
    Serial.println(theta);
    Serial.println(thetadir);
    Serial.println(thetae);
    float w = kpr * thetae;
    w = map(w,0,332,130,255);
    analogWrite(5,w);
    analogWrite(6,w);
    digitalWrite(I1, LOW);
    digitalWrite(D2, LOW);
    digitalWrite(I2, HIGH);
    digitalWrite(D1, HIGH);
    if(thetae<0){
      Serial.print("se acabo");
      analogWrite(5,0);
      analogWrite(6,0);
      digitalWrite(I1, LOW);
      digitalWrite(D2, LOW);
      digitalWrite(I2, LOW);
      digitalWrite(D1, LOW);
      t = 10; 
    }
  }
  else{
    Serial.print("se acabo");
    analogWrite(5,0);
    analogWrite(6,0);
    digitalWrite(I1, LOW);
    digitalWrite(D2, LOW);
    digitalWrite(I2, LOW);
    digitalWrite(D1, LOW);
    t = 10; 
  }
  }

}


void cuadrado(){ //funcion que hace la trayectoria de un cuadrado
  int xd1 = 0;
  int yd1 = 2;
  int xd2 = 0;
  int yd2 = 2;
  int xd3 = 0;
  int yd3 = 2;
  int xd4 = 0;
  int yd4 = 2;
  giro(xd1,yd1); 
  desplazamiento(xd1,yd1);
  giro(xd2,yd2); 
  desplazamiento(xd2,yd2);
  giro(xd3,yd3); 
  desplazamiento(xd3,yd3);
  giro(xd4,yd4); 
  desplazamiento(xd4,yd4);
}

void triangulo(){ //funcion que hace la trayectoria de un triangulo
  int xd1 = 6;
  int yd1 = 0;
  int xd2 = -3;
  int yd2 = 6;
  int xd3 = -3;
  int yd3 = 6;
  giro(xd1,yd1); 
  desplazamiento(xd1,yd1);
  giro(xd2,yd2); 
  desplazamiento(xd2,yd2);
  giro(xd3,yd3); 
  desplazamiento(xd3,yd3);
}


void loop() {
  //grados = 5; 
  //radianes = grados *(3.1416*180); 
  int xd1 = 6;
  int yd1 = 0;
  int xd2 = -3;
  int yd2 = 6;
  int xd3 = -3;
  int yd3 = 6;
  giro(xd1,yd1); 
  desplazamiento(xd1,yd1);
  giro(xd2,yd2); 
  desplazamiento(xd2,yd2);
  giro(xd3,yd3); 
  desplazamiento(xd3,yd3);
  exit(0); // Sale del programa con código de salida 0

}