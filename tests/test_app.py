import pytest
from app import index, custom 

def test_index():
	assert index()=="Hello World!"


def test_custom():
	assert custom()=="My First CI/CD push!"