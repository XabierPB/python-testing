from unittest import mock

"""
The main characteristic of a Mock object is that it will return another Mock instance when:
    - accessing one of its attributes
    - calling the object itself
"""
m = mock.Mock()
assert isinstance(m.foo, mock.Mock)
assert isinstance(m.bar, mock.Mock)
assert isinstance(m(), mock.Mock)
assert m.foo is not m.bar is not m()

"""
This is the default behaviour, but it can be overridden in different ways. 
For example you can assign a value to an attribute in the Mock by:

    - Assign it directly, like you’d do with any Python object.
    - Use the configure_mock method on an instance.
    - Or pass keyword arguments to the Mock class on creation.
"""
m.foo = 'bar'
assert m.foo == 'bar'

m.configure_mock(bar='baz')
assert m.bar == 'baz'

https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832