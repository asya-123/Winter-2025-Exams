def compare(first_values, second_values):

    dict_1 = list(first_values.keys())
    dict_2 = list(second_values.keys())

    if dict_1 != dict_2:
        return False
    return all(first_values[key] == second_values[key] for key in dict_1)

