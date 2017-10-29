h2ob = csvread('h2ob.csv');
h2ow = csvread('h2ow.csv');
h2o = [h2ow ; h2ob];
%mat = A;
mat = reshape(h2o, 26, 11);           %# h2ob = 143 = 13*11 
%mat = reshape(A, 16, 8);           %# i2hb = 128 = 16*8
mapminmax(mat,0,1);
imagesc(mat);            %# Create a colored plot of the matrix values
colormap(gray);