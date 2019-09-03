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
        path = os.path.join('dummy.yml')
        contents = open(path, "r").read()
        self.data = yaml.full_load(contents)
        self.print_data()

    # All of this code should be ported to a printer class
    def print_data(self):
        for week, day_list in self.data.items():
            print(f'Week: {week}')
            for day, tasks in day_list.items():
                self.print_day(day, tasks)

    def print_day(self, day, tasks):
        print(f'{self.indent_size(1)}Day: {day}')
        self.print_day_tasks(tasks)

    def print_day_tasks(self, tasks):
        if tasks is not None:
            task_summary = ', '.join([str(x) for x in tasks])
            print(f'{self.indent_size(2)}{task_summary}')
        else:
            print('Nothing to report')

    def indent_size(self, index):
        return ' ' * index

s = Sequitur()
