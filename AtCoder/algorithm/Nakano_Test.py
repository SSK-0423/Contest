import random

def make_problem():
    random.seed(123)
    xs = random.sample(range(1000),100)
    ys = random.sample(range(1000),100)
    zs = random.sample(range(1000),100)
    return xs,ys,zs

def find(xs,ys,zs,s):
    