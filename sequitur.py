"""
Sequitur main entry point
"""
#!/usr/local/bin/python3

import os
import pdb
import yaml

class Sequitur:
    LAPSE = {
        'tiny': 1,
        'small': 2
    }

    def __init__(self):
        self.init = True
        # pdb.set_trace()
        self.__set_data__()

    def __set_data__(self):
        path = os.path.join('dummy.yml')
        contents = open(path, "r").read()
        self.data = yaml.full_load(contents)

    # All of this code should be ported to a printer class
    def print_data(self):
        """Output the current context"""
        for week, day_list in self.data.items():
            print(f'Week: {week}')
            for day, tasks in day_list.items():
                self.__print_day__(day, tasks)

    def __print_day__(self, day, tasks):
        print(f'{self.__indent_size__(1)}Day: {day}')
        self.__print_day_tasks__(tasks)

    def __print_day_tasks__(self, tasks):
        if tasks is not None:
            task_summary = ', '.join([str(x) for x in tasks])
            print(f'{self.__indent_size__(2)}{task_summary}')
        else:
            print('Nothing to report')

    def __indent_size__(self, index):
        return ' ' * index
    # Printer -------------------

    """
    """
    def process_report(self):
        print('Processing report...')

client = Sequitur()
# client.print_data()
client.process_report()
