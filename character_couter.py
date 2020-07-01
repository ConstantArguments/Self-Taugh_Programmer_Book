def count_characters(string):
    """
    Iterates though string.
    Creates a dictionary with each character in string as a key.
    Increases the key value by 1 for every occurrence of key.
    Creates a list from dict keys and values, sorted alphabetically.
    :param: string
    """
    count_dict = {}
    for character in string:
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1
    print(count_dict)
    dict_items = count_dict.items()
    sorted_items = sorted(dict_items)
    print(sorted_items)

count_characters("Supercalifragilisticexpialidocious")
count_characters("Cras in libero euismod, pellentesque lorem ac, finibus leo. Donec eget lectus orci. Cras est odio, viverra vel placerat at, faucibus sed est. Integer dapibus dignissim elit eu placerat. Donec vehicula urna ut enim ultrices sodales. Aliquam non mi scelerisque, vulputate lacus sed, porttitor odio. In aliquet, quam vitae finibus posuere, turpis nisi bibendum eros, eu tincidunt leo nulla ut tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget consequat augue. Donec sit.")