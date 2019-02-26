import random

# don't use loop number in loop
for _ in range(5):
    print("Hello")

# use loop number in loop
for i in range(5):
    print("Hello in loop", i)
    print(random.randint(1, 6))

# private variable
_recipe = "a1a1a1a"
vat = 0.07

# Export All Variables and Methods
__all__ = ["_recipe", "vat"]
