

function [vi,vd,x,y,theta,xd,yd]=robot_dif_giro(x,y,theta,xd,yd)
 

% Tiempos
Tf = 10; %Tiempo final 
t = 0;   %Tiempo inicial 
dt = 0.01; %intervalos de tiempo

% Parametros del coche 
R = 0.12; %radio de llanta
L = 0.78; %distancia entre llantas 


% Valores iniciales
   %Posición actual en X
   %Posición actual en Y
 %Orientacion actual del coche 

% Constantes Giro 
kpr = 5; %Constante P para Giro (rotate)



% Velocidad Máxima  
vmax = 5; %Velocidad Máxima 

% Valores deseados 
   %Posición deseada en X
  %Posición deseada en Y
%orientacion deseada 
i = 1; %iterador 

%Variables que no afecta el while son: xd, yd 
while t < Tf

    % Control de Orientación:
    thetadir = atan2(yd-y,xd-x);  %Ángulo de dirección hacia el que el objeto debe orientarse para apuntar directamente hacia el objetivo.
    thetae = thetadir - theta  %revisar si es thetad - theta

  
    % Saturación de giro 
    if thetae > pi
        thetae = thetae - 2*pi;
    end
    if thetae < -pi
        thetae = thetae + 2*pi;
    end

    w = kpr*thetae;  %Velocidad angular o theta punto. Control P

    % Velocidades de llantas
    vd = (L*w)/(2*R);
    vi = -vd;

   

    % Simulación:
    % Primero, gira hacia la dirección del objetivo
    theta = theta + w*dt;  %Iteraciones de theta para saber en cada instante su orientacion

    %Saturación de giro 
    if theta > pi
        theta = theta - 2*pi;
    end
    if theta < -pi
        theta = theta + 2*pi;
    end
    
 
    %Saturación de giro igual a 0 
    if  vd > 0 && thetae <= 0.001
        Tf = 0;
    end
    if vd < 0 && thetae >= -0.001
        Tf = 0;
    end

    % Graficación:
    figure(1)
    scatter(x,y);
    hold on
    scatter(xd,yd);
    plot([x,x+0.5*cos(theta)],[y,y+0.5*sin(theta)],'linewidth',2);
    axis([-10 10 -10 10]);
    hold off
 
    i = i+1;
    t = t + dt;
    
end

    
end
