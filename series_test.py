from pandas import Series
import numpy as np

d = {
        "Name": "Sai",
        "Alias": ["Krishna", "Rama", "Vasudeva", "Vinayaka"],
        "Yuga": ["Sathya", "Treta", "Dwapura", "Kali"]
    }

a = np.array(['a', 'b', 'c'])

series = Series(15, [1, 2, 3])
print series
