function  s = simp38 (f, a, b, M)

% Entrada  - f funcion integrando creada con @
%          - a y b son los limites superior e inferior de integracion
%          - M es el numero de subintervalos
% Salida   - s es la suma de la regla de simpson 3/8

%  METODOS NUMERICOS: Programas en Matlab
% (c) 2004 por John H. Mathews y Kurtis D. Fink
%  Software complementario acompa�ando al texto:
%  METODOS NUMERICOS con Matlab, Cuarta Edicion
%  ISBN: 0-13-065248-2
%  Prentice-Hall Pub. Inc.
%  One Lake Street
%  Upper Saddle River, NJ 07458


if mod(M,3) ~= 0
sprintf('Error!!  El numero de subintervalos debe ser multiplo de 3 ...')
return

end

h = (b - a) / (M);
s1 = 0;
s2 = 0;

N=M/3;

for  k = 1:N
   x = a + h * (3 * k - 2);
   x2 = a + h * (3 * k - 1);
   s1 = s1 + feval(f, x) + feval(f , x2);
end
for  k = 1:(N-1)
   x3 = a + h * 3 * k;
   s2 = s2 + feval(f, x3);
end

s = (3*h/8) * (feval(f, a) + 3*s1 +  2 * s2 + feval(f,b));
E = h^5;