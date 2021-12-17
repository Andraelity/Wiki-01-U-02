clc;clear
%Este código sirve para ahorrar tiempo en encontrar el grado de precision
%basta con cambiar a y b para encontrar las primeras 5 integrales de x^k
%los resultados están en el vector F

%intervalo
a = -1;
b= 1;

f1 = @(x) 1 + 0.*x;
f2 = @(x) x;
f3 = @(x) x.^2;
f4 = @(x) x.^3;
f5 = @(x) x.^4;

%integrales
F1 = integral(f1,a,b);
F2 = integral(f2,a,b);
F3 = integral(f3,a,b);
F4 = integral(f4,a,b);
%F5 = integral(f5,a,b);
F = [F1,F2,F3,F4]



%esta otra parte es si nos dan una cuadratura G y nos preguntan su grado de
%precision, toca cambiar algunas cositas en cada ejercicio:
G1 = (2/3)*(f1(-1)+f1(0)+f1(1));
G2 = (2/3)*(f2(-1)+f2(0)+f2(1));
G3 = (2/3)*(f3(-1)+f3(0)+f3(1));
G4 = (2/3)*(f4(-1)+f4(0)+f4(1));
%G5 = (2/3)*(f5(-1)+f5(0)+f5(1));
G = [G1,G2,G3,G4];

