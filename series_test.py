from pandas import Series

d = {
        "Name": "Sai",
        "Alias": ["Krishna", "Rama", "Vasudeva", "Vinayaka"],
        "Yuga": ["Sathya", "Treta", "Dwapura", "Kali"]
    }

series = Series(d)
print series
