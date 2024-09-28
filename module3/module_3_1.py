
calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    str_lenght = len(string)
    str_upper = string.upper()
    str_lower = string.lower()
    return str_lenght, str_upper, str_lower


def is_contains(string, list_to_search):
    count_calls()
    lower_list_to_search = []
    for item in list_to_search:
        lower_list_to_search.append(item.lower())
    return string.lower() in lower_list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)




# def is_member(string, list_to_search):
#     for string in list_to_search:
#         if string is list_to_search or string == list_to_search:
#             return True
#     return False