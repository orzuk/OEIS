function [convergentSequences,toReturn] =getConverges(seqID)
%getConverges 
%   checks whether sequence converges.
%a sequence is defines as convergin if the last
%toReturn - 2 denotes converges, 1 denotes inconclusive, 0 denotes diverges
%convergentSequences - all convergent sequences
if nargin == 1
	cleaned_data=getSeq(seqID);
else
	load cleaned_data;
end	
nan = isnan(cleaned_data);
g= ones(size(nan,1),1);
nan=[nan g];
v=[1:size(nan,1)].';
B=accumarray(v,v,[],@(i) find(nan(i,:)==1,1,'first'));
temp=zeros(size(cleaned_data,1),10);
for i=1:length(B)
    temp(i,:)=cleaned_data(i,B(i)-10:B(i)-1);
end
%b1 = B-10;
%b2 = B-1;
%[P, Q] = ndgrid(1:size(cleaned_data,1), 10:-1:1);
%K = repmat(B(:), [1 10]);
%ind = K-Q;
%toAdd = repmat((0:1:(size(cleaned_data,1)-1))*size(cleaned_data,1)',[10 1]);
%toAdd = toAdd';
%ind = ind+toAdd;
%t = cleaned_data';
%temp = t(ind);
%temp = temp+0:1:(size(cleaned_data,1)-1)*size(cleaned_data,2);
last10 = abs(temp);
%div=last10(:,2:10)./last10(:,1:9);
monodec=sum(all(diff(last10,2,2)<0,2));
mightmonodec=sum(all(diff(last10,2,2)<=0,2));
toReturn = all(diff(last10,2,2)<=0,2)+all(diff(last10,2,2)<0,2);
convergentSequences=cleaned_data(toReturn==2,:);
%converges = sum(( sum((last10(:,2:10)./last10(:,1:9))<1,2)==9 ));
%mightConverge = sum(( sum((last10(:,2:10)./last10(:,1:9))<=1,2)==9 ));

bar([monodec,mightmonodec-monodec,size(cleaned_data,1)-mightmonodec]/size(cleaned_data,1));
set(gca,'XTickLabel',{'converges', 'inconclusive', 'diverges'})



title('percentage of convergent  series');
saveas(gcf,'convergence.png');



