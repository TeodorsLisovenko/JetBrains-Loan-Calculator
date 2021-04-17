args = sys.argv

# further code of the script "process_four_numbers.py"

list_of_int = []
for variable in args:
    try:
        if isinstance(int(variable), int):
            list_of_int.append(int(variable))
    except ValueError:
        pass

print(list_of_int)
