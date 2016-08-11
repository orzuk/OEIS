%histogram of appearance - We checked for multiple appearances
% in each sequence and computed the median
% of the occurrences

function hist_appear(seqID)

if nargin == 1
	cleaned_data=getSeq(seqID);
else
	load cleaned_data;
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
