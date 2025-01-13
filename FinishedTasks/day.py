dict_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def parse_day(input_string):
    for index, day in enumerate(dict_days, 1):
        if input_string.lower().startswith(day.lower()):
            return index
    return -1
