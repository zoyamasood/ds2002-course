#!/Users/zoyamasood/opt/anaconda3/bin/python3

import os

DESSERT = input("What is your favorite dessert? ")
COLOR = input("What is your favorite color? ")
SHOW = input("What is your favorite TV Show? ")

os.environ["DESSERT"] = DESSERT
os.environ["COLOR"] = COLOR
os.environ["SHOW"] = SHOW

print(os.getenv("DESSERT"))
print(os.getenv("COLOR"))
print(os.getenv("SHOW"))
