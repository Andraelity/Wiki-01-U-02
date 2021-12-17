function S = Abier2comp( f, a, b, n)

% Entrada   - f funcion integrando creada con @
%           - a y b limites superior e inferior de integracion
%           - N es el numero de nodos en la cuadratura

% Salida    - S es la aproximacion de la integral de f definida en a,b

if mod(M,4) ~= 0
sprintf('Error"" El numero de subintervalos deber ser multiplo de 4');
return
end

h = (b-a)/n;

x = [a:h:b];

S = (4*h/3)*(2*sum(f(x(2:4:n+1)) + f(x(3:4:n+1))) + sum(f(x(3:4:n+1))));
