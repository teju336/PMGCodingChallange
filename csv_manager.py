# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:55:22 2021

@author: tejas
"""

import sys


class CsvObj:
    __name = ""
    __line = ""
    __column_names = ""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def write_to_file(self):
        with open(self.__name, 'r') as input_file:
            for line in input_file:
                if self.__column_names == line:
                    continue
                else:
                    sys.stdout.write(line.strip() + ',\"' + self.__name + '\"\n')
                input_file.closed

    def get_columns(self):
        return self.__column_names

    def set_columns(self):
        with open(self.__name, 'r') as input_file:
            self.__column_names = input_file.readline();
        input_file.closed