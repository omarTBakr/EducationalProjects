import csv
from dateutil import parser
import collections
import constants
import itertools


def csv_parser(file_name, *, include_heading=True, delimiter=',', quotechar='"'):
    '''
    @param
    file_name : file name you want to parse it
    csv parameters:
        delimiter =',' : (kw)  delimiter exist in that file
        quotechar ='"': (kw) quote character def
    include_heading : True if you want to include the header of the file
    '''

    with open(file_name) as file:
        reader = csv.reader(file, delimiter=delimiter, quotechar=quotechar)

        if not include_heading:
            next(reader)

        yield from reader


def parse_row(row, heading):
    # vehicles.csv          has heading  = ['ssn,vehicle_make,vehicle_model,model_year']
    # employment.csv        has  heading = ['employer,department,employee_id,ssn']
    # update_status.csv    has heading   = ['ssn,last_updated,created']

    # def custom_date_parser(date_string , format = '%Y-%m-%dT%H:%M:%SZ'):
    #     return datetime.strptime(date_string, format)

    dictionary = {
        'model_year': int,
        'last_updated': parser.parse,
        'created': parser.parse,
    }
    return (dictionary.get(entry, str)(word) for entry, word in zip(heading, row))


def file_parser(file_name):
    file_iterator = csv_parser(file_name, include_heading=True)
    heading = next(file_iterator)

    # yield parse_row(next(file_iterator),heading)
    yield from (parse_row(row, heading) for row in file_iterator)


def extract_filed_names(file_name):
    file_iterator = csv_parser(file_name, include_heading=True)
    return next(file_iterator)


def create_named_tuple_class(file_name, class_name):
    field_names = extract_filed_names(file_name)

    return collections.namedtuple(typename=class_name, field_names=field_names)


def iter_file(file_name, class_name):
    header = extract_filed_names(file_name)
    named_tuple_ = create_named_tuple_class(file_name, class_name)
    reader = csv_parser(file_name, include_heading=False)

    for row in reader:
        yield named_tuple_(*parse_row(row, header))


def filter_fields(file_name, exclude='ssn'):
    fileds = extract_filed_names(file_name)
    return (field for field in fileds if field != exclude)


def create_combinded_named_tuple():
    # filter fields in the last 3 files
    fields_last_three = (entry for file in constants.file_names[1:] for entry in filter_fields(file))
    combinded_filtered = tuple(extract_filed_names(constants.file_names[0])) + tuple(fields_last_three)
    class_name = 'Record'
    return collections.namedtuple(typename=class_name, field_names=combinded_filtered)


def filter_named_tuple(named_tuple):
    return filter(lambda x: x != named_tuple.ssn, named_tuple)


def iter_files():
    iterables = (iter_file(file, class_name) for file, class_name in zip(constants.file_names, constants.class_names))

    Record = create_combinded_named_tuple()

    for personal_info, sec_file, third_file, forth_file in zip(*iterables):
        # filter the last three files
        filtered = (
            personal_info,
            filter_named_tuple(sec_file),
            filter_named_tuple(third_file),
            filter_named_tuple(forth_file),
        )

        yield Record(*itertools.chain.from_iterable(filtered))


def filter_combined(key=None):
    combined = iter_files()
    yield from filter(key, combined)


def groupby_combined(filter_key_, group_key, gender):
    filter_key = lambda item: filter_key_(item) and item.gender == gender

    data = tuple(filter_combined(filter_key))

    # sort data based on gender and car_make
    sorted_data = sorted(data, key=group_key, reverse=True)

    grouped_data = tuple((group[0], len(tuple(group[1]))) for group in itertools.groupby(sorted_data, key=group_key))

    return sorted(grouped_data, key=lambda item: item[1], reverse=True)
