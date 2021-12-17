function  s = Abierta3Comp(f, a, b, n)

% Entrada  - f funcion integrando creada con @
%          - a y b son los limites superior e inferior de integracion
%          - n es el numero de subintervalos y debe ser multiplo de 5
% Salida   - s es la suma de la regla de Boole

%si se necesita la version simple, coloque n = 3

if mod(n,4) ~= 0
sprintf('Error!!  El numero de subintervalos debe ser multiplo de 4 ...')
return

end

h = (b-a)/n;
x = a:h:b;
x1 = 11*sum(f(x(2:5:n+1)));
x2 = sum(f(x(3:5:n+1)));
x3 = sum(f(x(4:5:n+1)));
x4 = 11*sum(f(x(5:5:n+1)));
s = ((5*h)/24)*x1+x2+x3+x4;
