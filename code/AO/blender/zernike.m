function [Ie, Io] = zernike(n, m, N)


[X, Y] = meshgrid(linspace(-1,1,N),linspace(-1,1,N) );

Ie = zeros(N);
Io = zeros(N);

if (n<m) || mod(n-m,2)==1
    warning('n<m or n-m odd...')
else
    p = sqrt(X.^2+Y.^2);
    o = atan2(Y,X);

    mask = 1+0./(p<1);
    
    k = 0:(n-m)/2;
    
    rk = zeros(N);
    for k=0:(n-m)/2
        t1 = p.^(n-2*k);
        num = ((-1).^k).*factorial(n-k);
        den = factorial(k).*factorial(-k+(n-m)/2).*factorial(-k+(n+m)/2);
        rk = rk + t1.*num./den;
    end
    
    Ie = mask.*rk.*cos(m*o);
    Io = mask.*rk.*sin(m*o);
    
end