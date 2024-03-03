def all_true_in_tuple(input_tuple):
    return all(input_tuple)

tuple1 = (True, True, True)


result1 = all_true_in_tuple(tuple1)


print(f"All elements in tuple1 are True: {result1}")
