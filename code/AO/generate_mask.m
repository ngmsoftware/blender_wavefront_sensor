function M = generate_mask(Ns)

    
    [x, y] = meshgrid(linspace(-1,1,Ns),linspace(-1,1,Ns));

    z = sqrt(x.^2+y.^2);
    
    M = z<=1.02;
    
    
end