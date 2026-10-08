import pytest
from app import greet
#assert = ""this must be true
def test_greet_return_hello_name():
  assert greet('Deepthi') == "Hello Deepthi"

def test_gree_strips_spaces():
  assert greet('  Deepthi  ') == "Hello Deepthi"

def test_greed_empty_name_raises_error():
  with pytest.raises(ValueError):
    greet('')

def test_greet_spaces_only_raises_error():
  with pytest.raises(ValueError):
    greet('  ')

