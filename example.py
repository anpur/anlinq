from anlinq import AnLinq

arr = [1, 2, 3, 4, 5, 5]

# All kinds of lists comprehension exactly as you used to
print(AnLinq(arr).where(lambda x: x % 2 == 0))
# returns [2, 4]

# Lazy method chaining
print(AnLinq(arr)
      .where(lambda x: x > 1)
      .distinct()
      .order_by(descending=True)
      .select(lambda x: '#' + repr(x)))
# returns ['#5', '#4', '#3', '#2']

# Most complex functions, like mapping selecting both key and value
print(AnLinq(arr).group_by(lambda x: 'even' if x % 2 == 0 else 'odd', lambda x: '#' + repr(x)))
# returns {'even': ['#2', '#4'], 'odd': ['#1', '#3', '#5', '#5']}

