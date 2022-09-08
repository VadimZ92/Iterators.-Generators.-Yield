nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_generator(nested_list):
    value = 0
    len(nested_list)
    while value != len(nested_list):
        yield nested_list[value]
        value += 1


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        for var in item:
            if type(var) == list:
                for var1 in var:
                    if type(var1) != list:
                        print(var1)
                    else:
                        for var2 in var1:
                            if type(var2) != list:
                                print(var2)
            else:
                print(var)
