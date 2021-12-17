function  s = PuntoMedioCompu(f, a, b, n)

% Entrada  - f funcion integrando creada con @
%          - a y b son los limites superior e inferior de integracion
%          - M es el numero de subintervalos
% Salida   - s es la suma de la regla de Boole


if mod(n,2) ~= 0
sprintf('Error!!  El numero de subintervalos debe ser par...')
return

end

h = (b - a) / (n+2);
s1 = 0;

N=n/2;

for  k = 0:N
   x = a + h*(2*k);
   s1 = s1 + feval(f, x);
end

s = (2*h)*s1;
end
