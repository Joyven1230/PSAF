#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import traceback
from selenium.common.exceptions import NoSuchElementException
def element_not_found_exception(func):
    def warpper(self, locator):
        try:
            return func(self, locator)
        except NoSuchElementException:
            print 'element not found for locator:',locator, 'At method:', func.__name__
            return None
    return warpper

def assert_logger(func):
    def warpper(self):
        try:
            print 'Test Case is:', func.__name__
            return func(self)
        except AssertionError, ex:
            print 'AssertError in: %s.%s', (self.__class__.__name__, func.__name__)
    warpper.__name__=func.__name__
    return warpper

def exception_logger(func):
    def warpper(self):
        try:
            return func(self)
        except Exception, ex:
            print Exception,":",ex.message, 'At method:', func.__name__
            # print sys.exc_info()
            # print traceback.print_exc()  ##打印完整堆栈用于定位代码行
    return warpper

def name_logger(func):
    def warpper(self):
        print 'Test Class is:', self.__class__.__name__
        return func(self)
    warpper.__name__=func.__name__
    return warpper

class NOTESTDATAERROR(Exception):
    def __init__(self, module, test_case, name):
        self.value = '%s: Module: %s, TestCase: %s, Name: %s' % (self.__name__, module, test_case, name)
    def __str__(self):
        return repr(self.value)

class NOLOCATORERROR(Exception):
    def __init__(self, module, test_case, name):
        self.value = '%s: Module: %s, TestCase: %s, Name: %s' % (self.__name__, module, test_case, name)
    def __str__(self):
        return repr(self.value)
