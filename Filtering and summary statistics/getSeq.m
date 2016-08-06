%The function return a subset of the sequences 
%seqID - a vec with IDs of the different sequences the user is willing to
%get

%example for input: seqID=(3,100,5000) represent the sequences (A000003,A000100,A005000)

function subMat=getSeq(seqID)

load('stripped');

subMat=stripped(seqID,:);

end