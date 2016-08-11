%check number of even and odd in each seq
%dataCat: 1 - for cleaned data (compute for all the sequences in the cleaned data) and choose vecSeq=[]; 
%0 - specific sequences from the uncleaned data (in this
%case you have to add a vector 'vecSeq' that correspond to the IDs of the different
%sequences you would like to make the computation. ex: seqID=(3,100,5000) represent the sequences (A000003,A000100,A005000)

function even_odd(dataCat,vecSeq)

if dataCat==1
   load('cleaned_data.mat');
else
   cleaned_data=getSeq(vecSeq);
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