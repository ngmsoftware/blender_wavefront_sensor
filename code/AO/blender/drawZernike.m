clear();
clc();

figure();

N = 256;
maxn = 10;

count = 1;
for n=0:maxn
    for m=0:n
        if mod(n-m,2)==0
            [Ie, Io] = zernike(n,m, N);

            disp([n,m])
            axes('position',[0.5+0.25*m/maxn-0.25/maxn 1-(n+1)/(maxn+1) 0.5/maxn 1/(maxn+1)])
            %mesh(Ie*N/8);
            surf(Ie,'edgecolor','none');
            view(0,90);
            axis('off');
            axis('equal');
            axis('tight');
            if (m>0)
                axes('position',[0.5-0.25*m/maxn-0.25/maxn 1-(n+1)/(maxn+1) 0.5/maxn 1/(maxn+1)])
                %mesh(Io*N/8);
                surf(Io,'edgecolor','none');
                view(0,90);
                axis('off');
                axis('equal');
                axis('tight');
            end
        end
    end
end
