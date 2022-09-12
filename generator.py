nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_generator(nested_list):
    for item in nested_list:
        for var in item:
            if type(var) == list:
                for var1 in var:
                    if type(var1) != list:
                        yield var1
                    else:
                        for var2 in var1:
                            if type(var2) != list:
                                yield var2
            else:
                yield var


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
    print()
    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)
