import random

# don't use loop number in loop
for _ in range(5):
    print("Hello")

# use loop number in loop
for i in range(5):
    print("Hello in loop", i)
    print(random.randint(1, 6))

