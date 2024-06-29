# Summary

- This programme looks a particular file types in a given directory
- Move the matched patterned files to a new given directory
- If no match found simply print a message

How to run the programme

```bash
python3.9 move_files.py /Volumes/KINGSTON/2024/photos/ /Volumes/KINGSTON/2024/photos/test/
No match found.
```

How to run the unit test

```bash
python3.9 -m unittest test_move_files.py
or 
python3.9 test_move_files.py

Moved: /source/file1 2.jpeg -> /target/file1 2.jpeg
Moved: /source/file1 2.jpeg -> /target/file1 2.jpeg
Moved: /source/file3 2.MOV -> /target/file3 2.MOV
Moved: /source/file4 (1).MOV -> /target/file4 (1).MOV
..
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

## Requirements

Python 3.6 or later
