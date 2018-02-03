import numpy as np
import argparse
from params import params


class Interpreter(object):
	""" 
	Interpreter class tries to mimick your model
	using interpretable models and explains how your model works!
	"""

	def __init__(self):
		pass


	@classmethod
	def print_self(cls):
		print("My name is {}".format(cls))

	@staticmethod
	def add(x,y):
		return x+y


def main():
	I = Interpreter()
	I.print_self()
	print(I.add(3,2))



if __name__ == '__main__':
	main()