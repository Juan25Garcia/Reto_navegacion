clear all
close all
clc


xd = [-6, -6, -6];
xd1= xd(1);
xd2= xd(2);
xd3= xd(3);
yd =[-5, 0, 5 ];
yd1= yd(1);
yd2= yd(2);
yd3= yd(3);

[vi,vd,x,y,theta,xd,yd]=robot_dife_giro(5,7,0,-6,yd1);
[vi1,vd1]=robot_dif_despl(x,y,theta,xd,yd);
[vi,vd,x,y,theta,xd,yd]=robot_dife_giro(-6,5,theta,-6,0);
[vi1,vd1]=robot_dif_despl(x,y,theta,xd,yd);
[vi,vd,x,y,theta,xd,yd]=robot_dife_giro(-6,0,theta,5,-7);
[vi1,vd1]=robot_dif_despl(x,y,theta,xd,yd);
