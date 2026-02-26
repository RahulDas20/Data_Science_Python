import numpy as np


data = np.array([
    [95, 32, 420],
    [102, 35, 450],
    [98, 33, 430],
    [110, 37, 470],
    [105, 36, 460],
    [100, 34, 440],
    [108, 38, 480],
    [103, 35, 455],
    [97, 32, 425],
    [104, 36, 465]
])

#Here column 1 is the plant height, comlumn 2 is the grain weight and column 3 is the number of grains

#Print the dataset
print(data)
print(data.shape)

#Extract the plant height
plant_height = data[:,0]
print(plant_height)

#Extract the grain weight
grain_weight = data[:,1]
print(grain_weight)

#Extract the number of grains
num_grains = data[:,2]
print(num_grains)

#Calculate the mean plant height
mean_height = np.mean(plant_height)

#Find the tallest plant 
tallest_plant = np.max(plant_height)
print(tallest_plant)
print(np.argmax(plant_height))


#Find the plant with hightest grain weight
best_plant = np.argmax(grain_weight)
print(best_plant)


#Calculate the total grain weight
total_grain_weight = np.sum(grain_weight)
print(total_grain_weight)


#find the plants that have more than 450 grains
high_grain = num_grains[num_grains > 450]
print(high_grain)

print(data.shape[0])