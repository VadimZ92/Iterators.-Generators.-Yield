nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, value):
        self.value = -1

    def __iter__(self):
        # self.nested_list = nested_list
        return self

    def __next__(self):
        self.value += 1
        if self.value == len(nested_list):
            raise StopIteration
        return nested_list[self.value]


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
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

print()
flat_list = [var for item in FlatIterator(nested_list) for var in item]
print(flat_list)
