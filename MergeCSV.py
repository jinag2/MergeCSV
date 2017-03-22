#! python3

import csv
import sys
import os
import traceback


def main():
    target_csv_list = read_csv(sys.argv[1])
    x = len(target_csv_list)


def read_csv(filename):
    try:
        csv_file = open(filename)
    except:
        print(traceback.format_exc())
        sys.exit()
    csv_reader = csv.reader(csv_file)
    return list(csv_reader)


def abstract_float_col(data_list, col):
    value_list = []
    for row in data_list:
        value_list.append(float(row[col]))
    return value_list


def abstract_int_col(data_list, col):
    value_list = []
    for row in data_list:
        value_list.append(int(row[col]))
    return value_list


main()