#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
from Errors.ExceptionWarpper import NOLOCATORERROR

class DBLocator(object):
    def __init__(self, page, module=None):
        self.page = page
        self.module = module
        sql = self.__get_sql__()
        self.data = self.select_data(sql)

    def get(self, name, default=None):
        value = self.data.get(name)
        if value:
            return value
        elif default is not None:
            return default
        else:
            raise NOLOCATORERROR(self.module, self.page, name)

    def __get_sql__(self):
        where = ' AND 1=1 '
        if self.module:
            where += ''' AND module='%s' ''' % self.module
        sql = '''SELECT name, value FROM locator
                WHERE page='%s'
                AND status='active' %s;''' % (self.page, where)
        return sql

    def select_data(self, sql):
        db = MySQLdb.connect("localhost","root","root","datapool" )  ##数据库连接
        cursor = db.cursor()  ##获取游标
        cursor.execute(sql)  ##执行sql语句
        data = cursor.fetchall()  ##获取一条查询结果数据
        db.close()
        if data:
            return dict(data)
        else:
            raise NOLOCATORERROR(self.module, self.page)

FileLocator = {
    'KEY_WORLDS' : '#kw',
    'SEARCH' : '#su',
    'RESULT_COUNT' : '.nums',

    'USER_NAME' : '#username',
    'PASSWORD' : '#password',
}
