import numpy as np
import scipy.stats as stat
from gmm import GaussianMixtureModel
from collections import defaultdict
from params import Params

class Sampler(object):
	"""
	Sampler generates samples from your data! You should extend this abstract class
	if you want to define your own sampler.
	"""
	def generate_samples(self,number_of_samples=Params.NUM_OF_SAMPLES):
		raise NotImplementedError("You should implement generate_samples!")


class GMM_Sampler(Sampler):
	"""
	GMM sampler as described in https://arxiv.org/abs/1705.08504
	"""

	def __init__(self):
		super().__init__()

	def generate_samples(self,number_of_samples=Params.NUM_OF_SAMPLES,
		constraints=None,X=None):
		"""
		generate samples step:
			1-fitt a GMM on the data
			2-generate samples for each dimension according to the constraint
				for that dimension
		Arg:
			number_of_samples: number of generated samples
			constraints: dictionary which contains constraints for each dimension,
				{dim:(t,s)} means t <= X_dim <= s. If dim is not in constraits then
				t=-np.inf,s=np.inf.
			X: numpy array with shape [n_samples,n_features]
		Returns:
			None
		Raises:
			None
		"""
		gmm = GaussianMixtureModel(X)
		means,covs = gmm.get_params()
		generated_data = np.zeros(shape=(Params.NUM_OF_SAMPLES,X.shape[1]))
		generated_data = np.apply_along_axis(func,1,generated_data)



	def _create_samples_for_dim(self,dimension,constraint):
		pass


def main():
	# gmms = GMM_Sampler()
	# gmms.generate_samples(number_of_samples=100)
	a = np.ones(shape=(3,2))
	a = np.apply_along_axis(lambda x:sum(x),1,a)
	print(a)


if __name__ == '__main__':
	main()