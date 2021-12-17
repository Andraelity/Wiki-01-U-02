function S = Abier3comp( f, a, b, n)

% Entrada   - f funcion integrando creada con @
%           - a y b limites superior e inferior de integracion
%           - N es el numero de nodos en la cuadratura

% Salida    - S es la aproximacion de la integral de f definida en a,b

if mod(M,5) ~= 0
sprintf('Error"" El numero de subintervalos deber ser multiplo de 5');
return
end

h = (b-a)/n;

x = [a:h:b];

S = (5*h/24)*(11*sum(f(x(2:5:n+1))) + sum(f(x(3:5:n+1))) + sum(f(x(4:5:n+1))) + 11*sum(f(x(5:5:n+1))));