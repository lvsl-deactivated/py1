# coding: utf-8

# Пример работы с CSV файлом

import csv
from StringIO import StringIO

def main():
    sample_data = StringIO(
        'Имя,Фамилия,Отчество\n'
        'Иван, Иванов, Иванович\n'
        'Василий, Васильев, Васильевич\n'
    )
    sample_obj = [
        ("Имя", "Фамилия", "Отчество"),
        ("Иван", "Иванов", "Иванович"),
        ("Василий", "Васильев", "Васильевич"),
    ]

    csv_file = open('csv_example.csv','w')

    csv_reader = csv.reader(sample_data)
    csv_writer = csv.writer(csv_file)

    for row in csv_reader:
        print '|'.join(row)

    csv_writer.writerows(sample_obj)

    print '=' * 10, 'В виде словаря', '=' * 10

    sample_data.seek(0)
    csv_reader_dict = csv.DictReader(sample_data)

    for d in csv_reader_dict:
        for k,v in d.items():
            print "%s: %s" % (k,v)

    sample_dict = [
        {'Имя': 'Иван',
         'Фамилия': 'Иванов',
         'Отчество': 'Иванович'},

        {'Имя': 'Василий',
         'Фамилия': 'Васильев',
         'Отчество': 'Васильевич'},
    ]

    csv_dict_file = open('csv_dict_example.csv', 'w')

    csv_writer_dict = csv.DictWriter(csv_dict_file,
                                     sorted(sample_dict[0].keys()))

    csv_writer_dict.writeheader() # python 2.7+
    csv_writer_dict.writerows(sample_dict)

    csv_dict_file.close()
    csv_file.close()

if __name__ == "__main__":
    main()
