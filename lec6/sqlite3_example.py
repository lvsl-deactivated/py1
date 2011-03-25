# coding: utf-8

import sqlite3

def main():
    con = sqlite3.connect('db.sqlite3')

    c = con.cursor()

    c.execute('''create table stocks (
                    date text,
                    trans text,
                    symbol text,
                    qty real,
                    price real)''')

    for t in [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
              ('2006-04-05', 'BUY', 'MSOFT', 1000, 72.00),
              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
             ]:
        c.execute('insert into stocks values (?,?,?,?,?)', t)

    c.execute('select * from stocks where symbol=? order by price', ('IBM',))
    for row in c:
        print row

    c.execute('select sum(price) as summ from stocks')
    for row in c:
        print row


if __name__ == "__main__":
    main()
