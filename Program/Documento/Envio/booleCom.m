function  s = booleCom  (f, a, b, n)

% Entrada  - f funcion integrando creada con @
%          - a y b son los limites superior e inferior de integracion
%          - M es el numero de subintervalos
% Salida   - s es la suma de la regla de Boole


if mod(n,4) ~= 0
sprintf('Error!!  El numero de subintervalos debe ser multiplo de 4 ...')
return

end

h = (b - a) / (n);
s1 = 0;
s2 = 0;
s3 = 0;

N=n/4;

for  k = 1:N
   x = a + h * (4 * k - 1);
   x2 = a + h * (4 * k - 3);
   s1 = s1 + feval(f, x)+ feval(f, x2);
   x3 = a + h * (4 * k - 2);
   s2 = s2 + feval(f, x3);
end
for  k = 1:(N-1)
   x4 = a + h * 4 * k;
   s3 = s3 + feval(f, x4);
end
s = (2*h/45)*(7*feval(f, a) + 7*feval(f, b) + 32*s1 + 12*s2 + 14*s3);
