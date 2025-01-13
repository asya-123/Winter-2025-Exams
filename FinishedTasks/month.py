def get_month_number(input_string):
    months_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for index, month in enumerate(months_list, 1):
        if input_string.lower().startswith(month):
            return index
    return -1
