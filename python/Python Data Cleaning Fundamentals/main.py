from datetime import datetime, timezone
import parse_utility

cutoff_date = datetime(2017, 3, 1, tzinfo=timezone.utc)
filter_key = lambda item: item.last_updated >= cutoff_date
group_key = lambda item: item.vehicle_make


data_male = tuple(parse_utility.groupby_combined(filter_key_=filter_key, group_key=group_key, gender='Male'))
print('male data'.center(100, '*'))
print(data_male)

data_female = tuple(parse_utility.groupby_combined(filter_key_=filter_key, group_key=group_key, gender='Female'))
print('female data'.center(100, '*'))
print(data_female)
