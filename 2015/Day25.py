import re


def incrementing(x):
    return (252533 * x) % 33554393

def get_incrementing_times(row, column):
    round_number = sum(range(row + column - 1))
    return round_number + column


input_string = "To continue, please consult the code grid in the manual.  Enter the code at row 2981, column 3075."
row_number_text, column_number_text = re.findall(r'\d+', input_string)
row_number, column_number = int(row_number_text), int(column_number_text)
initial_value = 20151125
increment_times = get_incrementing_times(row_number, column_number)
for _ in range(increment_times-1):
    initial_value = incrementing(initial_value)
print(initial_value)