from sklearn import preprocessing

def normalize_iris(iris_dataset):
	norm_iris = preprocessing.normalize(iris_dataset)
	return norm_iris

def normalize_diabetes(diabetes_dataset):
	norm_diabetes = preprocessing.normalize(diabetes_dataset)
	return norm_diabetes