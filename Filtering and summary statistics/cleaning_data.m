load('stripped.mat')

%check for sequences that their length >= 40

vec_idx=zeros();
idx=1;

for i=1:size(stripped,1)
    if ~isnan(stripped(i,40))
       vec_idx(idx)=i;
       idx=idx+1;
    end
end

cleaned_data=zeros(length(vec_idx),size(stripped,2));

for i=1:length(vec_idx)
    cleaned_data(i,:)=stripped(vec_idx(i),:);
end

%delete duplicates

vec_dup_idx=zeros();
idx=1;

for i=1:size(cleaned_data,1)
    for j=1:size(cleaned_data,2)
        if min(cleaned_data(i,:)-cleaned_data(j,:))==0 && max(cleaned_data(i,:)-cleaned_data(j,:))==0
           vec_dup_idx(idx)=i;
           idx=idx+1;
        end
    end
    disp(i)
end

cleaned_data(vec_dup_idx,:)=[];

%check for any gaps or non numeric values
vec_str_idx=zeros();
idx=1;

for i=1:size(cleaned_data,1)
    for j=1:size(cleaned_data,2) 
        if j+1<=size(cleaned_data,2) && j-1>=1 && ischar(cleaned_data(i,j-1)) && ischar(cleaned_data(i,j+1))
           vec_str_idx(idx)=i;
           idx=idx+1;
        end
    end
    disp(i)
end

%delete fixed seqs
save_idx=zeros();
index=1;
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    temp2=cleaned_data(i,1);
    if all(cleaned_data(i,1:idx-1)==temp2)
       save_idx(index)=i;
       index=index+1;
    end
end
cleaned_data(save_idx,:)=[];

%delete seq with only 10 different values
save_idx=zeros();
index=1;
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    if length(unique(cleaned_data(i,1:idx-1)))<=10
       save_idx(index)=i;
       index=index+1;
    end
end

cleaned_data(save_idx,:)=[];


% %delete seqs that are almost simmilar and differ by few values
% save_idx=zeros();
% index=1;
% for i=38852:size(cleaned_data,1)
%     temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
%     [~,idx]=max(temp);
%     a=cleaned_data(i,1:idx-1);
%     for j=1:size(cleaned_data,1)
%         temp2=isnan(cleaned_data(j,:)); %run over the seq till the NaN
%         [~,idx2]=max(temp2);
%         b=cleaned_data(j,1:idx2-1);
%         if sum(a(1:39)==b(1:39))<=15
%            save_idx(index)=j;
%            index=index+1;
%         end
%     end
%     disp(i);
% end

% cleaned_data(save_idx,:)=[];


save('cleaned_data','cleaned_data')