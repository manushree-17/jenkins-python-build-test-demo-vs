from ops import *

def test_add():
	assert add(2,3) == 5

def test_subtract(x,y):
	assert subtract(2,3) == -1

def test_multiply(x,y):
	assert multiply(2,3) == 6

def test_divide(x,y):
	assert divide(9,3) == 3
