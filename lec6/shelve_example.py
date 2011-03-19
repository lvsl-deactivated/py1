# coding: utf-8

# Использование модуля shelve для хранения данных

import shelve
import random

def main():
    db = shelve.open('example_db.shlv')
    print db.keys()
    print db.values()

    for i in range(5):
        db[str(random.random())] = 'test shelve'

if __name__ == "__main__":
    main()
