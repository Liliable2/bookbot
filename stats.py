def get_num_words(contents):
    word_list = contents.split()
    word_count = len(word_list)
    return word_count


def get_num_char(contents):
    result = {}

    for char in contents.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def sort_on(item):
    return item["num"]


def format_char_dict(char_num_dict):
    char_list = []

    # for each char in input dict
    for char in char_num_dict:
        # form the char dict first
        char_dict = {"char": char, "num": char_num_dict[char]}

        # then append to list
        char_list.append(char_dict)

    # now sort the list
    char_list.sort(reverse=True, key=sort_on)

    return char_list
