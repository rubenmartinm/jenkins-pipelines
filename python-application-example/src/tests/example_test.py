import sys, os

# referencio a donde tengo el módulo que he creado antes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../application_example")))
import example

def test_add_one():
    assert example.add_one(3)==4