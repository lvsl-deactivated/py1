# coding: utf-8

# Чтение данных из pickle

import cPickle as pickle

from pickle_example_write import State

def main():
    obj = None
    pickled_obj = ''
    with open('pickle_example.pickle') as f:
        pickled_obj = f.read()

    obj = pickle.loads(pickled_obj)

    print type(obj)
    print obj.get_initials()


if __name__ == "__main__":
    main()
