import numpy as np
from numpy.linalg import norm

def computeLineNormal(points1, points2):
	"""
	Compute the normal of interpretation plane defined by two points and the perspective center

	:param points1: homogeneous coordinates of the first points set
	:param points2: homogeneous coordinates of the second points set

	:type points1: np.array nx3
	:type points2: np.array nx3

	:return: normal of the interpretation plane defined by the two points

	:rtype: np.array nx3

	"""

	# check if the points are normalized
	if np.all(norm(points1, axis=1)) != 1 or np.all(norm(points2, axis=1)) != 1:
		points1 = points1 / np.linalg.norm(points1, axis=1)
		points2 = points2 / np.linalg.norm(points2, axis=1)

	# Compute the normal of the interpretation plane
	nl = np.cross(points1, points2)
	# print(nl)

	return nl