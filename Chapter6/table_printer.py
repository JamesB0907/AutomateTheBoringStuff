def print_table(list_of_lists):
    # Find the longest string in each list of strings
    col_widths = [0] * len(list_of_lists)
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            if len(list_of_lists[i][j]) > col_widths[i]:
                col_widths[i] = len(list_of_lists[i][j])
    for j in range(len(list_of_lists[0])):
        for i in range(len(list_of_lists)):
            print(list_of_lists[i][j].rjust(col_widths[i]), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)

