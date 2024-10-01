#Задача "Однокоренные":


def single_root_words(root_word, *other_words):
    same_words = []
    check_list = list(other_words)
    compared_item = str(check_list[index])
    for index in check_list:
        if root_word in compared_item:
            same_words.append(index)
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
