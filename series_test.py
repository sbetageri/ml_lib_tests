from pandas import Series

d = {
        "Name": "Sai",
        "Alias": ["Krishna", "Rama", "Vasudeva", "Vinayaka"],
        "Yuga": ["Sathya", "Treta", "Dwapura", "Kali"]
    }

series = Series(d, [1, 2, 3])
print series
