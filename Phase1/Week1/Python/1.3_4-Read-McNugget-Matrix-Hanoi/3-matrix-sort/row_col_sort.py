import numpy as np 
from tabulate import tabulate

def read_matrix_file(filename):
    with open(filename, 'r') as open_file:
        output_list = []
        for line in open_file:
            output_list.append(line.split())
    output_list = [[int(j) for j in i] for i in output_list]
    return (output_list)


def print_matrix(list_of_lists):
    for line in list_of_lists:
        frmt = "|{:4}|"*len(line)
        print(frmt.format(*line))


def row_sums(list_of_lists):
    list_of_sums = []
    for line in list_of_lists:
        list_of_sums.append(sum(line))
    return list_of_sums


def col_sums(list_of_lists):
    return ([sum(x) for x in zip(*list_of_lists)])
    

def row_sort(list_of_lists):
    list_of_lists = np.array(list_of_lists)
    sum_list_of_lists = np.sum(list_of_lists, axis = 0)
    sum_sorted_list_of_lists = sum_list_of_lists.argsort()
    return(np.take(list_of_lists, sum_sorted_list_of_lists, axis=1))
    

def col_sort(list_of_lists):
    list_of_lists = np.array(list_of_lists)
    sum_columns_list_of_lists = np.sum(list_of_lists, axis = 1)
    sum_sorted_list_of_lists = sum_columns_list_of_lists.argsort()
    return(np.take(list_of_lists, sum_sorted_list_of_lists, axis=0))

if __name__ == "__main__":
    file = "test.txt"
    list_of_lists = read_matrix_file(file)
    print(tabulate(list_of_lists))
    # print(list_of_lists)
    # print_matrix(list_of_lists)
    # print(row_sums(list_of_lists))
    print(col_sums(list_of_lists))
    print(tabulate(row_sort(list_of_lists)))
    print(tabulate(col_sort(list_of_lists)))
