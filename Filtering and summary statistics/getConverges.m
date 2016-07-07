
%getConverges 
%   checks whether sequence converges.
%a sequence is defines as convergin if the last
% 10 members in the sequence fulfill the ratio test
load cleaned_data;
nan = isnan(cleaned_data);
g= ones(size(nan,1),1);
nan=[nan g];
v=[1:size(nan,1)].';
B=accumarray(v,v,[],@(i) find(nan(i,:)==1,1,'first'));
last10 = abs(cleaned_data(:,B-10:B-1));
div=last10(:,2:10)./last10(:,1:9);
monodec=sum(all(diff(div,2)<0,2));
mightmonodec=sum(all(diff(div,2)<=0,2));

%converges = sum(( sum((last10(:,2:10)./last10(:,1:9))<1,2)==9 ));
%mightConverge = sum(( sum((last10(:,2:10)./last10(:,1:9))<=1,2)==9 ));

bar([monodec,mightmonodec-monodec,size(cleaned_data,1)-mightmonodec]/size(cleaned_data,1));
set(gca,'XTickLabel',{'converges', 'inconclusive', 'diverges'})



title('percentage of convergent  series');
saveas(gcf,'convergence.png');



