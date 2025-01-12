def compare(first_values, second_values):

    a = list(first_values.keys())
    b = list(second_values.keys())

    if a != b:
        return False
    return all(first_values[c] == second_values[c] for c in a)

