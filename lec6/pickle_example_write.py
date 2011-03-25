# coding: utf-8

# Запись обекта в pickle

import cPickle as  pickle

class State(object):
    def __init__(self, first_name,
                       third_name,
                       second_name=''):
        self.first_name = first_name.decode('utf-8')
        self.second_name = second_name.decode('utf-8')
        self.third_name = third_name.decode('utf-8')

    def get_initials(self):
        tn = self.third_name.lower().capitalize()
        fn = self.first_name[0].capitalize()
        if self.second_name:
            sn = self.second_name[0].capitalize()
        else:
            sn = ''
        return "%s%s%s" % (tn, fn, sn)

def main():
    s = State("Иван", "Иванов", "Иванович")
    print s.get_initials()
    pickled_data = pickle.dumps(s)
    with open('pickle_example.pickle', 'w') as f:
        f.write(pickled_data)

if __name__ == "__main__":
    main()
