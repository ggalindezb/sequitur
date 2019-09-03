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

    def print_data(self):
        for week, day_list in self.data.items():
            print(f'Week: {week}')
            for day, tasks in day_list.items():
                self.print_day(day, tasks)

    def print_day(self, day, tasks):
        print(f' Day: {day}')
        self.print_day_tasks(tasks)

    def print_day_tasks(self, tasks):
        if tasks is not None:
            task_summary = ', '.join([str(x) for x in tasks])
            print(f'  {task_summary}')
        else:
            print('Nothing to report')

s = Sequitur()
