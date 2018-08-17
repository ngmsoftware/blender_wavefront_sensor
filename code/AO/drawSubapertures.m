function drawSubapertures(S, Ns)

    sx = S(1:end/2,1);
    sy = S(end/2+1:end,1);
    
    Ix = reshape(sx, Ns, Ns);
    Iy = reshape(sy, Ns, Ns);

    quiver(Ix, Iy);
    
    axis('off');
    
    cla();
    hold('on');
    for i=1:Ns
        for j=1:Ns
            patch(-0.5+[i i+1 i+1 i],-0.5+[j j j+1 j+1],[0 0 0],'facealpha',0,'edgecolor','k');
            plot(i+Ix(i,j)/2,j+Iy(i,j)/2,'xb');
            plot(i,j,'og');
        end
    end
    
end