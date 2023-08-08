import random
import string


def N(
  mean = 0.5
	, stddev = 0.01
	, bounds = None
):
	if bounds:
		return max(bounds[0], min(random.normalvariate(mean, stddev) , bounds[1]))
	else:
		return random.normalvariate(mean, stddev)
	

def uuid():
	letters_digits = string.ascii_letters
	return ''.join(random.choice(letters_digits) for i in range(20))