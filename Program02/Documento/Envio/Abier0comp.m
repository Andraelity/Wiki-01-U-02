function S = Abier0comp( f, a, b, n)

% Entrada   - f funcion integrando creada con @
%           - a y b limites superior e inferior de integracion
%           - N es el numero de nodos en la cuadratura

% Salida    - S es la aproximacion de la integral de f definida en a,b

if mod(M,2) ~= 0
sprintf('Error"" El numero de subintervalos deber ser multiplo de 2');
return
end

h = (b-a)/n;

x = [a:h:b];

S = (2*h)*(sum(f(x(2:2:n+1))));