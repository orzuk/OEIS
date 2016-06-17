%check for any monotonic sequences
 load('cleaned_data.mat')

vec_check_nonincreasing=zeros(1,size(cleaned_data,1));
vec_check_nondecreasing=zeros(1,size(cleaned_data,1));

%nondecreasing
index=1;
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    seq=cleaned_data(i,:);
    if all(diff(seq(1:idx-1)) >=0)==1
       vec_check_nondecreasing(index)=i;
       index=index+1;
    end
end

[~,idx]=min(vec_check_nondecreasing);
vec_check_nondecreasing=vec_check_nondecreasing(1:idx-1);
nondecreasingMat=cleaned_data(vec_check_nondecreasing,:);
save('nondecreasingSeqData','nondecreasingMat')

%nonincreasing
index=1;
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    seq=cleaned_data(i,:);
    if all(diff(seq(1:idx-1)) <=0)==1
       vec_check_nonincreasing(index)=i;
       index=index+1;
    end
end

[~,idx]=min(vec_check_nonincreasing);
vec_check_nonincreasing=vec_check_nonincreasing(1:idx-1);
nonincreasingMat=cleaned_data(vec_check_nonincreasing,:);
save('nonincreasingSeqData','nonincreasingMat')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% results: 49959*non_decreasing_seqs ; 923*non_increasing_seqs 

