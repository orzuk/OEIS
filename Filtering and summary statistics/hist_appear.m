%histogram of appearance - We checked for multiple appearances
% in each sequence and computed the median
% of the occurrences

%dataCat: 1 - for cleaned data (compute for all the sequences in the cleaned data) and choose vecSeq=[]; 
%0 - specific sequences from the uncleaned data (in this
%case you have to add a vector 'vecSeq' that correspond to the IDs of the different
%sequences you would like to make the computation. ex: seqID=(3,100,5000) represent the sequences (A000003,A000100,A005000)

function hist_appear(dataCat,vecSeq)

if dataCat==1
   load('cleaned_data.mat')
else
   cleaned_data=getSeq(vecSeq);
end

Ncount_vec=zeros(1,size(cleaned_data,1));
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    seq=cleaned_data(i,1:idx-1);
    B = unique(seq);
    Ncount_vec(i)= median(histc(seq, B)); % this willgive the number of occurences of each unique element
end

hist(Ncount_vec)

end
