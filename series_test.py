from pandas import Series
import numpy as np

d = {
        "Name": "Sai",
        "Alias": ["Krishna", "Rama", "Vasudeva", "Vinayaka"],
        "Yuga": ["Sathya", "Treta", "Dwapura", "Kali"]
    }

a = np.array(['a', 'b', 'c'])

series = Series(15, [1, 2, 3])
series[0] = 'Hello'
series[3] = 'Hello'
series[9] = 'Hello'

series2 = Series(' World', [9, 8, 7])
series2[1] = 9
series = series.mul(2)

print series + series2
