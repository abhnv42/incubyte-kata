import re
def add(numbers):

    INVALID_INPUT_ERROR = "Invalid input"
    NEGATIVE_VALUE_ERROR = "negative numbers not allowed : [{}]"
    CUSTOM_DELIMETER_FINDER_REGEX = r'(?<=\/\/).'
    CUSTOM_DELIMETER_DECLARATION_SUB_REGEX = r"^//{}\n"

    if(type(numbers).__name__ != 'str'): raise ValueError(INVALID_INPUT_ERROR)
    if len(numbers) == 0: return 0

    if len(numbers) == 1:
        if int(numbers) < 0: raise ValueError(NEGATIVE_VALUE_ERROR.format(numbers))
        return int(numbers)
    
    default_delimeter = ',|\\n'
    custom_delimiter_match = re.search(CUSTOM_DELIMETER_FINDER_REGEX, numbers)
    
    if custom_delimiter_match:
        custom_delimeter = custom_delimiter_match.group()
        default_delimeter += '|{}'.format(custom_delimeter)

        numbers = re.sub(CUSTOM_DELIMETER_DECLARATION_SUB_REGEX.format(custom_delimeter), '', numbers)

    positive_numbers = []
    negative_numbers = []
    for x in re.split(default_delimeter, numbers):
        if int(x) < 0: 
            negative_numbers.append(x)
        else:
            positive_numbers.append(int(x))

    if len(negative_numbers) > 0: raise ValueError(NEGATIVE_VALUE_ERROR.format(" ".join(negative_numbers)))

    return sum(positive_numbers)