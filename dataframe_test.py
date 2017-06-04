from pandas import DataFrame, Series

d = {
        "one": Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
        "two": Series([9, 8, 7], index=['a', 'b', 'c']),
        "three": Series([4, 5 ,6, 4], index=['a', 'b', 'c', 'd'])
    }

df = DataFrame(d)

print df
