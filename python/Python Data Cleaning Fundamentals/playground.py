# exploring the content of each file
import constants
import itertools
import csv
import parse_utility
from parse_utility import csv_parser
from parse_utility import file_parser
from datetime import datetime, timezone


def display_heading1(file_names, heading=10):
    with open(file_names) as file:
        print(f' content of {file_names}'.center(100, '#'))
        for line in itertools.islice(file, 10):
            print(line)


# just to look at the content of each file

# for file_names in constants.constants.file_names:
#     display_heading1(file_names)


# for proper parsing we need csv module


def display_heading2(file_names, heading=10):
    with open(file_names) as file:
        print(f' content of {file_names}'.center(100, '#'))
        for line in itertools.islice(csv.reader(file, delimiter=',', quotechar='"'), 10):
            print(line)


# for file in constants.file_names:
#     display_heading2(file)


# for file in constants.file_names:
#     iterator = csv_parser(file , include_heading= True)
#     print(f"{file}".center(100 , '#'))
#     # for _ in range( 5):
#     #     print(next (iterator))
#     print(next(iterator))


# testing file parser

# for file in constants.file_names:
#     print(f"{file}".center(100 , '#'))
#     for line in  itertools.islice(file_parser(file), 2):
#         # print(list(line))
#         print( [  type(item) for item in list(line)])


# for file,class_name in zip(constants.file_names ,
#                            constants.class_names):
#     print(parse_utility.create_named_tuple_class(file,class_name))


# test named tuple for each file

# for file_name, class_name in zip( constants.file_names,
#                                  constants.class_names):
#     file_iterator = parse_utility.iter_file(file_name ,class_name)
#     print(f"{file_name}".center(100 , '#'))
#     for line in itertools.islice(file_iterator,5):
#         print(line)
#         print()
#


# test combined named tuple
# nt = parse_utility.create_combinded_named_tuple()
# print(nt._fields)

# test filtered files

# for row in itertools.islice( parse_utility.iter_files() , 5):
#     print(row)
#     print()
#     print()


# cehck filter combined

cutoff_date = datetime(2017, 3, 1, tzinfo=timezone.utc)

filter_iter = parse_utility.filter_combined(key=lambda named_tuple: named_tuple.last_updated >= cutoff_date)

for nt in itertools.islice(filter_iter, 4):
    print(nt, '\n')


# test groupby

# filter_key = lambda item: item.last_updated >= cutoff_date
#
#
# data = tuple(parse_utility.groupby_combined(filter_key, gender='Male'))
# print(sorted(data, key=lambda item: item[1], reverse=True))
