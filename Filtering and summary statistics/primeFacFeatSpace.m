load('cleaned_data.mat')
vec_idx=zeros();

%check seq the factor cant be computed
index=1;
rng(1);

%delete seq that have too big values
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    if max(abs(cleaned_data(i,1:idx)))>=10^13
       vec_idx(index)=i;
       index=index+1;
    end
end

cleaned_data(vec_idx,:)=[];

% % v=randperm(size(cleaned_data,1),10000);

%create new feature using factor
cleaned_data=abs(cleaned_data);
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    for j=1:idx-1
         fac=factor(cleaned_data(i,j));
         cleaned_data(i,j)=median(fac); %%replace with the median factorial
    end  
    disp(i)
end

data_fac=cleaned_data;

save('data_fac','data_fac')

