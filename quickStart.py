#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from BaiduHome import BaiduHome
from DataPool import DataPool
from ExceptionBase import *

class TestDemo(unittest.TestCase):
    @exception_logger
    def setUp(self):
        wd = webdriver.Chrome()
        wd.get('http://www.baidu.com')
        self.page = BaiduHome(wd)
        self.wd = wd

    @exception_logger
    @assert_logger
    def test_sample(self):
        self.page.key_worlds_input(DataPool.get('SELENIUM'))
        self.page.search_click()
        assert False

    @exception_logger
    def tearDown(self):
        self.wd.close()

if __name__=='__main__':
    unittest.main()