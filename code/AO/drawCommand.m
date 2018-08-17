function drawCommand(W, Ns)

% function drawCommand(W, Ns)
%
%   Draw a reshaped version of the command vector W (as image)

I = reshape(W, Ns+1, Ns+1);

imagesc(I(2:2:end,1:2:end));
axis('off');
    

end