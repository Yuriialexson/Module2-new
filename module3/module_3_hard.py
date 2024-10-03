data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

index = 0
compared_item = data_structure[index]
for index in data_structure:
  print(index)


def calculate_structure_sum(data_structure):
  index = 0
  compared_item = data_structure[index]
  for index in check_list:
    if root_word in compared_item:
      same_words.append(index)
  return same_words



result = calculate_structure_sum(data_structure)
print(result)