import numpy as np

# create a 1D array of app ratings
oneDRatings = np.linspace(3.8, 5.0, 10)
print(oneDRatings.shape)
print(oneDRatings)

# make it a 2D array
oneDRatings = oneDRatings.reshape([2,5])
print(oneDRatings.shape)
print(oneDRatings.ndim)
print(oneDRatings)

# find average of row 1 and row 2
print(oneDRatings.ndim)
print("The average of the first row is", np.round(np.average(oneDRatings[0,:]),1))
print("The average of the second row is", np.round(np.average(oneDRatings[1,:]),1))

# find min and max ratings
print(oneDRatings.ndim)
print(oneDRatings[0:])
print("The highest (max) rating of the first row is", np.amax(oneDRatings[0,:]))
print("The lowest (min) rating of the first row is", np.amin(oneDRatings[0,:]))
print("The highest (max) rating of the second row is", np.amax(oneDRatings[1,:]))
print("The lowest (min) rating of the second row is", np.amin(oneDRatings[1,:]))
