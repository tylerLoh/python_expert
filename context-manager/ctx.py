# ctx.py

from sqlite3 import connect
from contextlib import contextmanager

# class context:
#     def __init__(self, gen):
#         self.gen = gen
#
#     def __call__(self, *args, **kwargs):
#         self.args, self.kwargs = args, kwargs
#         return self
#
#     def __enter__(self):
#         self.gen_list = self.gen(*self.args, **self.kwargs)
#         next(self.gen_list)
#
#     def __exit__(self, *args):
#         next(self.gen_list, None)


# @context
@contextmanager
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cur.execute('drop table points')

# temptable = context(temptable)

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(2, 2)')
        cur.execute('insert into points (x, y) values(3, 3)')

        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x*y) from points'):
            print(row)
