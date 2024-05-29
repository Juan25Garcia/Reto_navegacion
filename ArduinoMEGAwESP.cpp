#include <Encoder.h>

// Declaración de variables
double x = 0;
double y = 0;
double xd = 20;
double yd =0;
double theta = 0;
double Tf = 10;
double t = 0;
double dt = 0.1;
double d = 0; 

double vi = 0;
double vd = 0;

// Motores 
const int D1 = 10;
const int D2 = 9;
const int I1 = 12;
const int I2 = 8; 

// Parámetros del robot
double L = 0.28;
double R = 0.03;

// Constantes de control
double kpr = 2;
double kpt = 2;

// Almacenamiento de trayectoria
double x_trajectory[1000];
double y_trajectory[1000];
int trajectory_index = 0;
trayectoria_input = '0,5;5,5;5,0;0,0'; %cuadrado

Encoder Enc1819(18, 19); //Pines Encoder
Encoder Enc23(2, 3); //Pines Encoder

// Constantes del Encoder
const double PULSOS_POR_REV = 680.0; // Cambia esto según tu encoder
const double CIRCUNFERENCIA_RUEDA = 2 * PI * R;


void setup() {
  // Inicialización de comunicación serial
  Serial.begin(9600);
  pinMode(10,OUTPUT); 
  pinMode(12,OUTPUT); 
  pinMode(8,OUTPUT); 
  pinMode(9,OUTPUT); 
}

long oldPosition  = -999;

void loop() {
  d = sqrt(pow(xd - x, 2) + pow(yd - y, 2));
  while (t < Tf) {

    long pulsosizq = Enc1819.read();
    long pulsosdere = Enc23.read();
    //Serial.print("Pulsos de Encoder");
    //Serial.println(pulsos);

    double actualizq = (abs(pulsosizq) * CIRCUNFERENCIA_RUEDA) / PULSOS_POR_REV;
    double actualder = (abs(pulsosdere) * CIRCUNFERENCIA_RUEDA) / PULSOS_POR_REV;
    double direccion_actual = (actualizq+actualder)/2;

    Serial.println(actualizq);
    Serial.println(actualder);


    // Control de dirección
    d = d-direccion_actual; 
    double v = kpt * d;

    // Detener si está cerca del objetivo
    if (d <= 0.1) {
      vd = 0;
      vi = 0; 
      Tf = 0; 
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
    vd = map(vd, 0, 400, 100, 255)*1.035;

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