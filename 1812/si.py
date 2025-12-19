# si.py
# function to calculate simple interest
from mathfunc import divide, tripod

# simple interest calculate function
def simple_interest(p, r, t):
    return divide(tripod(p,r,t),100)