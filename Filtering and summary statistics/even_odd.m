%check even and odd
load('cleaned_data.mat');

result_vec=zeros(1,size(cleaned_data,1)); %0-even, 1-odd
Ncount_vec=zeros(1,size(cleaned_data,1));
tmp=0;
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    seq=cleaned_data(i,1:idx-1);
    seq_even=mod(seq,2);
    tmp=sum(seq_even);
    if tmp<length(seq)
       result_vec(i)=1; 
    end
end

y=[sum(1-result_vec) sum(result_vec)];


bar(y)
