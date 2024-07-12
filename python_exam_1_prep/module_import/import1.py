import math

# pi and sin() do not exist in this code's
# namespace without first referencing the
# imported math module.

# For example,
# x = pi
# Output: NameError: name 'pi' is not defined

x = math.pi
y = math.sin(x/2)

print(x)
print(y)