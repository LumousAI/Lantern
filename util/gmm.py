import numpy as np
from sklearn import mixture
from itertools import product

from params import Params
np.random.seed(Params.RANDOM_SEED)


class GaussianMixtureModel(object):
	"""
	GuassianMixtureModel creates a GMM model and fits it on your data.
	It is built on top of scikit-learn. It automatically selects the best number
	of components and saves your from writing some boiler-plate code
	"""
	def __init__(self,max_components=Params.MAX_COMPONENTS):
		self._best_gmm = None
		self._max_components = max_components

	def find_best_gmm(self,data,*args,**kwargs):
		
		# parse arguments
		cv_types = Params.DEFAULT_CV if "cv_types" not in kwargs else \
			kwargs["cv_types"]
		number_of_components  =range(1,self.max_components) if \
		 "number_of_components" not in kwargs else kwargs["number_of_components"]

		# select the best models using the bic score
		bic_score = {}
		min_bic = float('Inf')
		for cv,n in product(cv_types,number_of_components):
			gmm = mixture.GaussianMixture(n_components=n,covariance_type=cv)
			gmm.fit(data)
			score = gmm.bic(data)
			bic_score[(cv,n)]=score
			if score < min_bic:
				self._best_gmm = gmm
				min_bic=score

		return self._best_gmm

	@property
	def max_components(self):
		return self._max_components

	@max_components.setter
	def max_components(self,max_val):
		self._max_components = max_val

	@property
	def best_gmm(self):
		return self._best_gmm


def main():
	g = GaussianMixtureModel()
	print(dir(g))


if __name__ == '__main__':
	main()