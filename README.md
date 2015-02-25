# AnLinq
AnLinq is a python module which provides functionality similar to .NET LINQ chaining methods for list comprehensions.

Current project state:

- **Code**: READY
- **Tests**: 80% covered
- **Reference**: meaningful reST docstrings for all methods
- **Supported comprehension methods**: `count`, `any`, `all`, `first`, `first_or_none`, `last`, `last_or_none`, `to_list`, `to_dictionary`, `where`, `distinct`, `group_by`, `order_by`, `take`, `skip`, `select`, `map`, `select_many`, `aggregate`, `reduce`, `foreach`, `concat`, `concat_item`, `except_for`, `intersect`
- **Python integration**: `__repr__`, `__iter__`, `__getitem__`, `__len__`, `__eq__`, `__ne__`

## Example
Here is small example, how you can use AnLinq:
```
arr = [1, 2, 3, 4, 5, 5]

# All kinds of lists comprehension exactly as you used to
print AnLinq(arr).where(lambda x: x % 2 == 0)
# returns [2, 4]

# Lazy method chaining
print AnLinq(arr)\
    .where(lambda x: x > 1)\
    .distinct()\
    .order_by(descending=True)\
    .select(lambda x: '#' + repr(x))
# returns ['#5', '#4', '#3', '#2']

# Most complex functions, like mapping selecting both key and value
print AnLinq(arr).group_by(lambda x: 'even' if x % 2 == 0 else 'odd', lambda x: '#' + repr(x))
# returns {'even': ['#2', '#4'], 'odd': ['#1', '#3', '#5', '#5']}
```