# The FFXIV: ARR Screenshot Name Correcter
#### Or: "Tanaka Would Have Gotten It Right"

As most people would know, sorting of filenames is done from left to right, alphabetically or numerically.

However, most people don't work at Square-Enix and someone there had the horrible idea that we should use the _least logic way_ of writing dates.

So I bring you the ARR Screenshot Name Correcter, which will rename all your screenshots from the abomination of a date format, MMDDYYYY, to the international ISO 8601 standard of YYYYMMDD, which will naturally sort all of your screenshots from oldest to newest, the way the Twelve intended.

## Running
Python is required. The script is written in Python 3, but Python 2.7 should work (untested!).
This script assumes that your screenshots are in
```C:\Users\${USER}\Documents\My Games\FINAL FANTASY XIV - A Realm Reborn\screenshots```

If you want to use the current logged in user's username, just run the script by either double clicking the file or running it from command line.
```python path\to\ARR_date_correcter.py```

If you want to use a different username than the currently logged in user, you can run the script from command line and pass the wanted username as an input argument to the script.
```python path\to\ARR_date_correcter.py Gwaeryn```