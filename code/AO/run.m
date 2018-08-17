clear();
clc();

%%
% subapertures : Wavefront sensor (WFS)
% command matrix: Deformable mirror (DM)


%%
% for displaying the eigenmodes of H
showEigenmodes = 1;


%%
% Ns: Number of rows and columns in the wavefront sensor WFS
Ns = 40;
% scale: gain of each subaperture in the WFS
scale = 0.5;


% number of commands is always 1 plus the subapertures (Fried geometry)
Nw = Ns+1;


%%
% generate the command matrix
H = generateMeasureMatrix_fried(Ns,scale);


% pupil area
% readjust the geometry to simulate a circular array of subapertures...
% notice that the command matrix is still a square grid and the DM have
% actuators that act outside the WFS sensors... (that might be fun when you
% try to find the command for a given WFS configuration hehehehe)
masks = generate_mask(Ns);
H([masks(:)<1; masks(:)<1],:) = 0;
maskw = generate_mask(Ns+1);


%% 
% generate a command (deform the deformable mirror)
% for easy "understanding" of the DM commands, generate as a matrix of
% actuator values.

% Random pushes of the actuators
M = 2*rand(Nw).*(rand(Nw)>0.9);

% parabolic shape
[x, y] = meshgrid(linspace(-1,1,Nw),linspace(-1,1,Nw));
M = 3*(x.^2+y.^2);


% reshape the command matrix to a command vector
W = mat2command(M);





%% let there be light!
S = H*W;

 



%% Try to invert and get W back...

% avoid impossible modes
p = ones(size(W))*scale; % piston mode
w = ones(size(W))*scale; %# waffle mode
w(2:2:end) = -scale;

R = H'*H + p*p' + w*w';

[U, d, V] = svd(R);
di = d;
di(d>0.02) = 1./di(d>0.02);
di(d<=0.02) = 0.0;
iR = U*di*V';


Wh = iR*H'*S;


% Ws only in the pupil area
dataW = W(maskw(:));
dataWh = Wh(maskw(:));



M = reshape(W,Ns+1,Ns+1);
Mh = reshape(Wh,Ns+1,Ns+1);


M = M-mean(mean(dataW));

dataW = dataW-mean(mean(dataW));

disp(sum(sum((dataW-dataWh).^2)));

%% plots
% subplot(1,3,1);
% drawCommand(W, Ns);
% subplot(1,3,2);
% drawSubapertures(S,Ns);
% subplot(1,3,3);
% drawCommand(Wh,Ns);

mesh(M.*maskw,'facecolor','red')
hold('on');
mesh(Mh.*maskw,'facecolor','blue')



















%%
if showEigenmodes

    [U, d, V] = svd(H);

    cont = 1;
    for i=1:Ns
        for j = 1:Ns
            axes('position',[(i-1)/Ns (j-1)/Ns 0.95/Ns 0.95/Ns]);

            drawCommand(V(:,cont).*maskw(:),Ns);

            drawnow();
            
            cont = cont+1;
        end
        disp(sprintf('%d of %d',i,Ns));
    end

end