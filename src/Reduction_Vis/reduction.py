# import python packages
import numpy as np
from sklearn.decomposition import PCA
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
	print(len(features[0].dtype.descr))
	general_field_names = ["name", "length"]
	feature_names = [name for (name, typ) in features[0].dtype.descr if name not in general_field_names]
	feature_names = ["var","mean"]

	names = features[["name"]]
	X = ftr.extract_features(features, feature_names)
	labels = np.asarray([i%100 for i in range(X.shape[0])])

	test_pca(names, X)

	

def test_pca(names, X, labels=None):
	"""runs a PCA analysis on features"""

	X = X[np.isfinite(X).all(axis=1)]
	pca = PCA(n_components=2)
	X_pc = pca.fit_transform(X)
	plt_scatter(names, X_pc, labels)


	print(pca.explained_variance_ratio_)

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