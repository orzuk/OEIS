# import python packages
import numpy as np

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.manifold import MDS

import matplotlib.pyplot as plt
import matplotlib.cm as cm

# add to python environment the directory above the one the file is in (src)
import sys
import os
sys.path.append(os.path.dirname(__file__) + r"/..") 

#import OEIS files
import features as ftr


def main():
	features = ftr.read_features_file()
	general_field_names = ["name", "length"]
	feature_names = [name for (name, typ) in features[0].dtype.descr if name not in general_field_names]
	#feature_names = ["var","mean"]

	names = features[["name"]]
	X = ftr.extract_features(features, feature_names)
	X = X[0:1000,:]

	labels = np.asarray([i%100 for i in range(X.shape[0])])

	tsne(names,X)
	#pca(names, X)
	#mds(names,X)

def dim_red(names,X,model,labels=None):
	X = X[np.isfinite(X).all(axis=1)]
	X_ts = model.fit_transform(X)
	plt_scatter(names,X_ts,labels)
	return X_ts

def mds(names, X, labels=None):
	dim_red(names,X,MDS(n_components=2),labels)


def tsne(names, X, labels=None):
	"""runs a TSNE analysis"""
	dim_red(names,X,TSNE(n_components=2),labels)
	

def pca(names, X, labels=None):
	"""runs a PCA analysis on features"""
	dim_red(names,X,PCA(n_components=2),labels)
	#print(model.explained_variance_ratio_)

def plt_scatter(names,X, labels=None):
	if labels is None:
		labels = np.asarray([0 for i in range(X.shape[0])])

	cls = set(labels)

	colors = cm.rainbow(np.linspace(0, 1, len(cls)))
	plt.figure()
	for c,l in zip(cls,colors):
		idx = labels == c
		plt.scatter(X[idx,0], X[idx,1],c = l)

	plt.show()


if __name__ == '__main__':
	main()