clc;clear
%INTEGRAL ENTRE a Y b SIN RESTRICCIONES
f= @(x) 1./(sqrt((x.^2)-4));
a = 2;
b = 2.5; 
N = 9;
[quad, raices, nodos, coefs] = GaussLegendre( f, a,b,N);
display(quad)
%% 

%INTEGRAL DESDE -INF HASTA +-b:
%a f se le debe hacer el cambio de variable f(y) = f(1/y)/y^2

f = @(y) (sin(3.*y.^2).*tan(-5./(y.^4)))./y.^2;
b = -2; 
N = 35;
[quad, raices, nodos, coefs] = GaussLegendre( f, 1/b,0,N);
display(quad)

%% 

%INTEGRAL DESDE a HASTA +Inf:
%a f se le debe hacer el cambio de variable f(y) = f(1/y)/y^2

f = @(y) ((cos(1./y).*exp(y)).*y.^3)./y.^2;
a = 1/3; %a debe ser positivo
N = 5;
[quad, raices, nodos, coefs] = GaussLegendre( f, 0,1/a,N);
display(quad)
%% 
%INTEGRAL DESDE -a HASTA +Inf:
f = @(x) sin(x).^2./exp(x);
%a f se le debe hacer el cambio de variable f(y) = f(1/y)/y^2
f2 = @(y) (sin(1./y).^2./exp(1./y))./y.^2;
a = -1; 
N = 35;
[quad, raices, nodos, coefs] = GaussLegendre(f,a,1,N);
[quad2, raices2, nodos2, coefs2] = GaussLegendre(f2,0,1,N);
Resultado = quad + quad2;
display(Resultado)

%% 
clc;clear
%INTEGRAL DESDE -Inf HASTA +Inf:
%a f se le debe hacer el cambio de variable f(y) = f(1/y)/y^2
f = @(x) (cos(3./x.^2).*exp(-5.*(x.^4)));
f2 = @(y) (cos(3.*y.^2).*exp(-5./(y.^4)))./y.^2;
N = 35;
[quad1, raices1, nodos1, coefs1] = GaussLegendre(f2,-1,0,N);
a = 0; % a es el número que genera discontidad en f;
[quad2, raices2, nodos2, coefs2] = GaussLegendre(f,-1,a,N);
% [quad4, raices4, nodos4, coefs4] = GaussLegendre(f1,a,1,N); %esta linea
% puede entrar o no, dependiendo si el cero o cualquiero número entre -1 y
% 1, genera discontinuidad en la funcion a integrar.
[quad3, raices3, nodos3, coefs3] = GaussLegendre(f2,0,1,N);
Resultado = quad1 + quad2 + quad3; % + quad4
display(Resultado)
