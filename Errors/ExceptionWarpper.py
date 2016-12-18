#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import traceback
from selenium.common.exceptions import NoSuchElementException
from Result.Result import Result
result = Result()
def element_not_found_exception(func):
    def not_found(self, locator):
        try:
            return func(self, locator)
        except NoSuchElementException:
            result.logError('element not found for locator:'+locator+'At method:'+func.__name__)
            return None
    return not_found

def assert_logger(func):
    def assertlogger(self):
        try:
            result.logInfo('Test Case is:'+func.__name__)
            return func(self)
        except AssertionError, ex:
            result.logError('AssertError in: %s.%s' % (self.__class__.__name__, func.__name__))
    assertlogger.__name__=func.__name__
    return assertlogger

def exception_logger(func):
    def exceptionlogger(self):
        try:
            return func(self)
        except Exception, ex:
            result.logError("%s:%s At method:%s" % (Exception, ex.message, func.__name__))
            # print sys.exc_info()
            if True: ##debug is Ttrue?
                print traceback.print_exc()  ##打印完整堆栈用于定位代码行
    return exceptionlogger

def name_logger(func):
    def namelogger(self):
        result.logInfo('Test Class is:'+self.__class__.__name__)
        return func(self)
    namelogger.__name__=func.__name__
    return namelogger

class NOTESTDATAERROR(Exception):
    def __init__(self, module, test_case):
        self.value = '%s: Module: %s, TestCase: %s' % (self.__class__.__name__, module, test_case)
    def __str__(self):
        return repr(self.value)

class NOLOCATORERROR(Exception):
    def __init__(self, module, test_case, name):
        self.value = '%s: Module: %s, TestCase: %s' % (self.__class__.__name__, module, test_case)
    def __str__(self):
        return repr(self.value)
