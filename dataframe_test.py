from pandas import DataFrame, Series

d = {
        "one": Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
        "two": Series([9, 8, 7], index=['a', 'b', 'c']),
        "three": Series([4, 5 ,6, 4], index=['a', 'b', 'c', 'd'])
    }

pod = {
    #"one": [1, 2, 3],
    #"two": [4, 5, 6],
    #"three": [7, 8, 9],
    "four": {
        "a":{
            1:1
        },
        "b": {
            2:2
        },
        "c": {
            3:3
        }
    }
}

df = DataFrame(pod)

print df
