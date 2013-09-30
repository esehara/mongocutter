# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
from tasks import TaskTracker
import color

gp = color.green_print
bp = color.blue_print
SEPARATE_LINE = "="


def console_args_parse():
    parser = argparse.ArgumentParser(
        description=(
            "mongocutter"
            "--"
            "Perfomance Test for Python and Mongodb"))
    parser.add_argument('filename')
    args = parser.parse_args()
    return args.filename


def import_filepath(filename):
    tasks = TaskTracker(filename)
    return tasks


def read_yaml(tasks):
    gp(" * Read Yaml Data")
    tasks.yaml_read()
    bp("   * Done Read Yaml Data")
    return tasks


def connect_database(tasks):
    gp(" * Connect MongoDB")
    tasks.connect_database()
    bp("   * Connected MongoDB")
    return tasks


def disconnect_databae(tasks):
    gp(" * Disconnect MongoDB")
    tasks.disconnect_database()
    bp("   * Disconnected MongoDB")
    return tasks


def create_setup_data(tasks):
    gp(" * Create Setup Data")
    tasks.create_setup_data()


def destory_setup_data(tasks):
    gp(" * Destory Setup Data")
    pass


def _task_runner(tasks):
    print(SEPARATE_LINE * 12)
    print("Start.")
    print(SEPARATE_LINE * 12)

    # TaskManager Model Setup
    tasks = read_yaml(tasks)
    tasks = connect_database(tasks)

    # Use Database
    create_setup_data(tasks)
    gp(" * Fix Setup Data")
    gp(" * Running Task")
    destory_setup_data(tasks)
    disconnect_databae(tasks)
    print(SEPARATE_LINE * 12)
    print("End.")
    print(SEPARATE_LINE * 12)


def main():
    tasks = import_filepath(
        console_args_parse())
    _task_runner(tasks)


if __name__ == "__main__":
    main()
