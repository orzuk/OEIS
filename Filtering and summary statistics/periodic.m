%check for any periodic sequences
vecPeriod=zeros();
for i=1:size(cleaned_data,1)
    temp=cleaned_data(i,:);
    temp(isnan(temp))=[];
    [p,num] = seqperiod(temp);
    vecPeriod(i)=p;
end

