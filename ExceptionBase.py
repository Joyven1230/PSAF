#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import traceback

def element_not_found_exception(func):
    def warpper(self, locator):
        try:
            return func(self, locator)
        except:
            print 'element not found for locator:',locator, 'At method:', func.__name__
            return None
    return warpper

def assert_logger(func):
    def warpper(self):
        try:
            return func(self)
        except AssertionError, ex:
            print AssertionError, ':', ex.message, 'At method:', func.__name__
    return warpper

def exception_logger(func):
    def warpper(self):
        try:
            return func(self)
        except Exception, ex:
            # print Exception,":",ex.message, 'At method:', func.__name__
            print sys.exc_info()
            # print traceback.print_exc()  ##打印完整堆栈用于定位代码行
    return warpper