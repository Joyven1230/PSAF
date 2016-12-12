#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from Errors.ExceptionWarpper import *
from Data.DataPool import DataPool
from Pages.BaiduHome import BaiduHome

class TestDemo(unittest.TestCase):
    @exception_logger
    @name_logger
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.dp = DataPool(self.__class__.__name__)
        self.wd.get(self.dp.get('BAIDU_HOME_URL'))
        self.page = BaiduHome(self.wd)

    @exception_logger
    @assert_logger
    def test_sample(self):
        self.page.key_worlds_input(self.dp.get('SELENIUM'))
        self.page.search_click()
        assert True

    @exception_logger
    def tearDown(self):
        self.wd.close()

if __name__=='__main__':
    unittest.main()