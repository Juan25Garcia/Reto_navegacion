
function [vi,vd]=robot_dif_despl(x,y,theta,xd,yd)
 
% Tiempos
Tf = 10; % Tiempo final 
t = 0;   % Tiempo inicial 
dt = 0.01; % Intervalos de tiempo

% Parámetros del robot
L = 0.78; % Distancia entre ruedas
R = 0.12; % Radio de las ruedas

% Constantes de control
kpr = 1; % Constante P para giro
kpt = 8; % Constante P para desplazamiento

% Velocidad máxima
vmax = 5; % Velocidad máxima

% Almacenamiento de trayectoria
x_trajectory = [];
y_trajectory = [];

% Bucle de simulación
while t < Tf
    % Control de orientación
    thetadir = atan2(yd - y, xd - x);  % Dirección deseada
    thetae = thetadir - theta;

    % Saturación de giro 
    if thetae > pi
        thetae = thetae - 2*pi;
    end
    if thetae < -pi
        thetae = thetae + 2*pi;
    end

    % Velocidad angular
    w = kpr * thetae;

    % Control de dirección
    d = sqrt((xd - x)^2 + (yd - y)^2); % Distancia entre puntos
    v = kpt * d; % Velocidad lineal

    % Saturación de velocidad máxima
    if v > vmax
        v = vmax;
    end

    % Simulación
    % Actualización de la orientación
    theta = theta + w * dt;

    % Saturación de giro 
    if theta > pi
        theta = theta - 2*pi;
    end
    if theta < -pi
        theta = theta + 2*pi;
    end

    % Avance en la dirección actual
    xp = v * cos(theta); % Velocidad en X
    yp = v * sin(theta); % Velocidad en Y
    
    % Actualización de posición
    x = x + xp * dt;
    y = y + yp * dt;
    
    % Almacenar las posiciones para la trayectoria
    x_trajectory = [x_trajectory x];
    y_trajectory = [y_trajectory y];

    % Velocidades de llantas
    vi = (2 * ((2 * v) - (2 * w * L))) / R; % Velocidad llanta izquierda
    vd = vi + (L * w / R); % Velocidad llanta derecha 

    % Detener si está cerca del objetivo
    if d <= 0.01
        Tf = 0; 
    end 
    
    % Graficación:
    figure(1)
    plot(x_trajectory, y_trajectory, 'b-'); % Trajectory
    hold on
    scatter(x, y, 'ro'); % Current position
    scatter(xd, yd, 'g*'); % Desired position
    plot([x, x + 0.5 * cos(theta)], [y, y + 0.5 * sin(theta)], 'k-', 'LineWidth', 2); % Orientation
    axis([-10 10 -10 10]);
    xlabel('Posición X');
    ylabel('Posición Y');
    title('Simulación de movimiento del robot');
    hold off
 
    % Actualizar el tiempo e iterador
    t = t + dt;
end
