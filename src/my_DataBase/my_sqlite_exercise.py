# -*- coding: utf-8 -*-

import os
import sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('CREATE TABLE user(id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), score INT)')
cursor.execute(r"INSERT INTO user VALUES ('A-001', 'Adam', 95)")
cursor.execute(r"INSERT INTO user VALUES ('A-002', 'Bart', 62)")
cursor.execute(r"INSERT INTO user VALUES ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('select name from user where score > ? AND score <= ? ORDER BY score', (low, high))
        values = cursor.fetchall()
        print('values:', values, 'type:', type(values))
        return [x[0] for x in values]
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')