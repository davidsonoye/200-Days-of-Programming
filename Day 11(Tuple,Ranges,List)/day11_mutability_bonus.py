# List is mutable
a = [1, 2, 3]
b = a
b[0] = 99
print(a)  # [99, 2, 3] → changes reflect in 'a'

# Tuple is immutable
x = (1, 2, 3)
y = x
# y[0] = 99  ❌ This will raise a TypeError
