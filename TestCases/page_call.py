#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from Errors.ExceptionWarpper import *
from Data.DataPool import DBDataPool
from Pages.BaiduHome import BaiduHome
from Result.Result import Result
class TestDemo(unittest.TestCase):
    @exception_logger
    @name_logger
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.dp = DBDataPool(self.__class__.__name__)
        self.wd.get(self.dp.get('BAIDU_HOME_URL'))
        self.page = BaiduHome(self.wd)
        self.result = Result()

    @exception_logger
    @assert_logger
    def test_sample(self):
        self.page.key_worlds_input(self.dp.get('SELENIUM'))
        self.page.search_click()
        self.result.logInfo('The search button is clicked')
        assert True

    @exception_logger
    def tearDown(self):
        self.wd.close()

if __name__=='__main__':
    unittest.main()