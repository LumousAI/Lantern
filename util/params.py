class Params(object):
	# random seed (usually used with numpy)
	RANDOM_SEED = 1234
	# number of samples generated in samplers
	NUM_OF_SAMPLES = 1000
	# max_components in GaussianMixtureModel
	MAX_COMPONENTS = 100
	# default covariance matrix type in GaussianMixtureModel
	DEFAULT_CV = ["spherical", "tied", "diag", "full"]


