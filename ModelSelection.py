import os
import numpy as np
from sklearn import mixture
import matplotlib.pyplot as plt
import itertools
import scipy.stats as stat

def main():
	# cdf
	print(stat.norm.cdf(0.0))
	# inverse of cdf
	print(stat.norm.ppf(0.5))
	x = np.linspace(-10,10,100)
	_,ax = plt.subplots(1,1)
	# ax.plot(x,stat.norm.pdf(x))
	# ax.plot(x,stat.norm.cdf(x))
	# ax.plot(x,stat.norm.sf(x))

	# truncated normal function
	a,b = 1,4
	ax.plot(x,stat.truncnorm.pdf(x,a,b))
	ax.plot(x,stat.truncnorm.cdf(x,a,b))
	ax.hist(stat.truncnorm.rvs(a,b,size=10000),normed=True,bins=100)
	plt.show()


if __name__ == '__main__':
	main()