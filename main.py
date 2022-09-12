main_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        self.main_list_cursor = 0  # курсор основного списка
        self.nested_list_cursor = -1  # курсор списка вложенного в основной список
        return self

    def __next__(self):

        while len(main_list) != self.main_list_cursor:
            self.nested_list_cursor += 1
            if len(main_list[self.main_list_cursor]) == self.nested_list_cursor:
                self.main_list_cursor += 1
                self.nested_list_cursor = 0
            if len(main_list) == self.main_list_cursor:
                raise StopIteration
            return self.main_list[self.main_list_cursor][self.nested_list_cursor]


if __name__ == '__main__':
    for item in FlatIterator(main_list):
        print(item)
print()
flat_list = [item for item in FlatIterator(main_list)]
print(flat_list)
