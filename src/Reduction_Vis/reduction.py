# import python packages
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
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
	names = ftr.extract_features(features, ["name"])
	X = ftr.extract_features(features, feature_names)

	# print(features[0].dtype)
	# print(feature_names)
	#print(features[0][1])
	test_pca(names, X)

def test_pca(names, X):
	"""runs a PCA analysis on features"""

	print(X.shape)

	X = X[np.isfinite(X).all(axis=1)]
	print (X.shape)
	pca = PCA(n_components=2)
	#pca.fit(X)
	X_pc = pca.fit_transform(X)
	plt.figure()
	plt.scatter(X_pc[:,0], X_pc[:,1])
	plt.show()
	#print(pca.explained_variance_ratio_)

if __name__ == '__main__':
	main()