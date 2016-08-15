%check number of even and odd in each seq

function even_odd(seqID)

if nargin == 1
	cleaned_data=getSeq(seqID);
else
	load cleaned_data;
end

result_vec=zeros(1,size(cleaned_data,1)); %0-even, 1-odd
Ncount_vec=zeros(1,size(cleaned_data,1));
tmp=0;
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    seq=cleaned_data(i,1:idx-1);
    seq_even=mod(seq,2);
    tmp=sum(seq_even); %compute number of odd number in the seq
    if tmp>length(seq)/2
       result_vec(i)=1; %odd seq
    elseif tmp<length(seq)/2
       result_vec(i)=0; %even
    elseif tmp==length(seq)/2
       result_vec(i)=2;
    end
end

y=[sum(result_vec==1) sum(result_vec==0) sum(result_vec==2)]; %(even,odd,equal)


bar(y)
end