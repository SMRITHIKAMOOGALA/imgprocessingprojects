I=imread("cricketball.jpg");
imshow(I)
s=size(I);
I_red=I;
I_green=I;
I_blue=I;
I_red(:,:,2:3)=0;
I_green(:,:,3)=0;
I_green(:,:,1)=0;
I_blue(:,:,1:2)=0;
imshow(I_red);
imshow(I_green);
imshow(I_blue);
n=s(1)*s(2);
AveR=sum(I_red(:))/n;
AveG=sum(I_green(:))/n;
AveB=sum(I_blue(:))/n;
I_gray=rgb2gray(I);
imshow(I_gray)
gray_max=max(I_gray(:));
I_redlc=I_red;
I_greenlc=I_green;
I_bluelc=I_blue;
if (0.95*gray_max)>100
    for i=1:s(1)
        for j=1:s(2)
            I_redlc(i,j,1)=I_red(i,j,1)*(255/AveR);
             I_greenlc(i,j,2)=I_green(i,j,2)*(255/AveG);
              I_bluelc(i,j,3)=I_blue(i,j,3)*(255/AveB);
        end
    end
end
figure
imshow(I_redlc)
I_new=rgb2gray(I_redlc);   
figure
imshow(I_new)
I_smooth = filter2(fspecial('average',7),I_new);
imshow(I_smooth);
figure
b(1:3, 1:3)=1;
e=imerode(I_smooth,b);
imshow(e)
figure
d=imdilate(e,b);
imshow(d)
figure
I_edge = edge(d,'sobel');
imshow(I_edge)
figure
I_convex=bwconvhull(I_edge);
imshow(I_convex)
figure
I_final = edge(I_convex,'sobel');
imshow(I_final)
[centersBright, radiiBright] = imfindcircles(I_convex,[50 500],'ObjectPolarity','bright');
viscircles(centersBright, radiiBright,'Color','b')