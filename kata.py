import re
def add(numbers):
    if(type(numbers).__name__ != 'str'): return "Invalid input"
    if len(numbers) == 0: return 0
    if len(numbers) == 1: return int(numbers)
    
    delimiter = ',|\\n'

    values = {int(x) for x in re.split(delimiter, numbers)}
    
    return sum(values);