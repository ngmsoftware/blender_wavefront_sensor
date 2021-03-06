function H = generateMeasureMatrix_hudgin(Ns)

% H = generateMeasureMatrix(Ns)
%
% Generates the measurement matrix H for a wavefront sensor with Ns by Ns
% sub apertures... Using Slope model (Hudgin Geometry)

H = zeros(2*Ns^2, (Ns+1)^2-1);

cont = 1;
for i=1:Ns
    for j=1:Ns
        H(cont,j+(i-1)*Ns+(i-1)) = -1;
        H(cont,j+(i-1)*Ns+1+(i-1)) = 1;
        
        cont = cont+1;
    end
end


for i=1:Ns
    for j=1:Ns
        H(cont,j+(i-1)*Ns+(i-1)) = -1;
        H(cont,j+(i-1)*Ns+4+(i-1)) = 1;
        
        cont = cont+1;
    end
end

