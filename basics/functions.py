# %%
def calculate_total(symbol, var_one, var_two):
    if symbol == '+':
        return (var_one + var_two)
    elif symbol == '-':
        return (var_one - var_two)
    elif symbol == '*':
        return (var_one * var_two)
    else:
        return (var_one / var_two)

calculate_total('-', 6, 5)

# %%
def returnValues():
    array = [1, 2, 3, 4, 5]
    first_number = array[0]
    last_number = array[-1]
    return first_number, last_number

first, last = returnValues()
print("First number:", first)
print("Last number:", last)


# %%
