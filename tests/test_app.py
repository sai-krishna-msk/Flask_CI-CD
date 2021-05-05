import pytest
from app import index 

def test_home():
	assert index()=="Hello World!"