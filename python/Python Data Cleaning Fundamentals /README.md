
# Basic Data Cleaning Using Pure Python

__Disclaimer: This project could be done with a couple of lines using Pandas, BUT the goal is mainly educational, to see how things work behind the scenes.__

## What You Will Learn from This Project?
1. Lazy iteration and how to utilize it to save resources.
2. Properly iterating over a file.
3. Understanding the power of `yield` and `yield from`.
4. Cleaning data using pure Python.
5. Breaking down large problems into smaller, manageable tasks.
6. Organizing code into multiple modules.
7. Exploring the use of named tuples from the `collections` module.
8. explore `itertools` module specially `groupby` and `chain` functionality.

## Problem Statement

You are given 4 data files (included in the Data directory):
1. `personal_info.csv`
2. `vehicles.csv`
3. `employment.csv`
4. `update_status.csv`

Each file has a common feature: SSN. Each SSN appears only once in each file and is present in all four files. The order of SSNs is the same in each file.

__Ignore these assumptions and work accordingly. Hint: Use a dictionary with SSN as a key.__

The overall problem is divided into 4 different goals to make things a bit easier. If you want, you can jump to the final goal and start from there.

### Goal 1: Explore the Data and Create a Lazy Iterator for Each File
Create a lazy iterator for each of the 4 files. It should:
1. Return a named tuple with correct field names.
2. Use appropriate data types (this one is tricky).
3. Ensure the 4 iterators are independent of each other.

Example:
```python
 
import collections
def iter_file(  ):
    # Your implementation
    for row in file:
        yield collections.named_tuple(row )  
```

### Goal 2: Create a Single Named Tuple Containing All Information
1. Combine data from all 4 files into a single iterable.
2. Return a named tuple containing all information from all files.

### Goal 3: Filter the Data
1. Filter all data with update date 3/1/2017 (this feature is in `update_status.csv`).
__There are two ways here__:
    1. Just filtering named tuples you have from Goal 2 which is straightforward.
    2. Modify the iterator itself to filter the data form each file which could be a little bit tedious.

### Goal 4: Largest Car Makes by Gender
1. Generate a list of numbers of car makes by gender for non-stale records.

## Expected Output & Validation
After successfully running the code, you should see a breakdown of car makes grouped by gender:

Female: ('Ford', 42), ('Chevrolet', 42), ('Mitsubishi', 22) ... etc
Male: ('Ford', 40), ('Chevrolet', 30) ... etc

These results indicate the frequency of each car make within the specified gender group.

## My Approach
_Inspired by Dr. Fred Baptiste. For more info, check the last section._

1. Organize your code by:
    1. Creating a directory containing all your data.
    2. Creating a constants module that contains all constants.
    3. Creating a module to test your assumptions and explore the data within.
2. Alternate between testing your hypothesis  code / implementation between `playground.py` and `parse_util.py` .
3. follow each goal carefully

## For More
Check this amazing course of Dr. Fred Baptiste on [Udemy](https://www.udemy.com/course/python-3-deep-dive-part-2/).

__I highly recommend his deep dive series, check them out__ 
