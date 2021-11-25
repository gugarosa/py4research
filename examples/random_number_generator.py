import py4research.math.random as r

# Generates an integer random number array
i = r.generate_integer_random_number(low=0, high=100, size=10)
print(f'Shape: {i.shape}')
print(f'Value: {i}')

# Generates a random gaussian number array
g = r.generate_gaussian_random_number(mean=0.5, variance=1.0, size=10)
print(f'Shape: {g.shape}')
print(f'Value: {g}')
