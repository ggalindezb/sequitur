#!/usr/local/bin/python3

import os
import pdb
import yaml

class Sequitur:
    def __init__(self):
        self.init = True
        # pdb.set_trace()
        self.set_data()

    def set_data(self):
        path = os.path.join('data.yml')
        contents = open(path, "r").read()
        self.data = yaml.full_load(contents)
        self.print_data()

    def print_data(self):
        for week, day_list in self.data.items():
            print(f'Week: {week}')
            for day, tasks in day_list.items():
                print(day)
                print(', '.join([str(x) for x in tasks]))

s = Sequitur()
