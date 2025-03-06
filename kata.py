import re
def add(numbers):
    if(type(numbers).__name__ != 'str'): return "Invalid input"
    if len(numbers) == 0: return 0
    if len(numbers) == 1: return int(numbers)
    
    delimiter = ',|\\n'
    
    custom_delimiter_match = re.search(r'(?<=\/\/).', numbers)
    
    if custom_delimiter_match:
        custom_delimeter = custom_delimiter_match.group()
        delimiter += '|{}'.format(custom_delimeter)

        numbers = re.sub(r"^//{}\n".format(custom_delimeter), '', numbers)

    values = {int(x) for x in re.split(delimiter, numbers)}
    
    return sum(values)