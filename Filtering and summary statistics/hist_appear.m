%histogram of appearance
load('cleaned_data.mat');

Ncount_vec=zeros(1,size(cleaned_data,1));
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    seq=cleaned_data(i,1:idx-1);
    B = unique(seq);
    Ncount_vec(i)= median(histc(seq, B)); % this willgive the number of occurences of each unique element
end

hist(Ncount_vec)
