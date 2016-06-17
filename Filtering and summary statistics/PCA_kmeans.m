%after factorization - PCA + kmeans
%compute the length of the new features
load('data_fac.mat')

vecLength=zeros(1,size(data_fac,1));

for i=1:size(data_fac,1)
    temp=isnan(data_fac(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    vecLength(i)=idx-1;
end

hist(vecLength);

%create new data with length(seq)=40
data_fac_40=data_fac;
data_fac_40(vecLength~=40,:)=[];
data_fac_40=data_fac_40(:,1:40);
 
%pca
 [wcoeff,~,latent,~,explained] = pca(data_fac_40,...
'VariableWeights','variance')

wcoeff=wcoeff(:,1:2)';
data_fac_pca_3=wcoeff*data_fac_40';
data_fac_pca_3=data_fac_pca_3';

 data_fac_pca_3=log10(abs(data_fac_pca_3));
% scatter3(data_fac_pca_3(:,1),data_fac_pca_3(:,2),data_fac_pca_3(:,3));
% 
% H = fspecial('gaussian',3,1000000);
% data_fac_pca_3 = imfilter(data_fac_pca_3,H,'replicate');
% scatter3(data_fac_pca_3(:,1),data_fac_pca_3(:,2),data_fac_pca_3(:,3));
% 

%kmeans
opts = statset('Display','final');
[idx,C] = kmeans(data_fac_pca_3,2,'Distance','cityblock',...
    'Replicates',20,'Options',opts);

%plot kmeans
figure;
plot(data_fac_pca_3(idx==1,1),data_fac_pca_3(idx==1,2),'r.','MarkerSize',12)
hold on
plot(data_fac_pca_3(idx==2,1),data_fac_pca_3(idx==2,2),'b.','MarkerSize',12)
plot(C(:,1),C(:,2),'kx',...
     'MarkerSize',15,'LineWidth',3)
legend('Cluster 1','Cluster 2','Centroids',...
       'Location','NW')
title 'Cluster Assignments and Centroids'
hold off