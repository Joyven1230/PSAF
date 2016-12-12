#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.select import Select
from Errors.ExceptionWarpper import *

class PageBase(object):
    def __init__(self, driver, locators):
        self.wd = driver
        self.locators = locators

    def __del__(self):
        pass

    @element_not_found_exception
    def get_element(self, locator):
        return self.wd.find_element_by_css_selector(self.locators.get(locator, ''))

    @element_not_found_exception
    def get_elements(self, locator):
        return self.wd.find_elements_by_css_selector(self.locators.get(locator, ''))

    def select_by_index(self, locator, index):
        ele = self.get_element(locator)
        if ele and ele.get_attribute('tagName')=='SELECT':
            options = ele.find_elements_by_css_selector('option')
            if options and len(options)>=index+1:
                Select(ele).select_by_index(index)
            else:
                print 'options is too less to select'
        else:
            print 'element is not select object'

    def select_by_value(self, locator, value):
        ele = self.get_element(locator)
        if ele and ele.get_attribute('tagName')=='SELECT':
            options = ele.find_elements_by_css_selector('option')
            if options:
                for option in options:
                    new_value = option.get_attribute('value')
                    if value==new_value:
                        Select(ele).select_by_value(value)
                        return
                print 'no value matched'
            else:
                print 'options is too less to select'
        else:
            print 'element is not select object'

    def select_by_text(self, locator, text):
        ele = self.get_element(locator)
        if ele and ele.get_attribute('tagName')=='SELECT':
            options = ele.find_elements_by_css_selector('option')
            if options:
                for option in options:
                    new_text = option.get_attribute('innerText')
                    if text==new_text:
                        Select(ele).select_by_visible_text(text)
                        return
                print 'no text matched'
            else:
                print 'options is too less to select'
        else:
            print 'element is not select object'

    def check_box(self, locator, on=True):
        ele = self.get_element(locator)
        if ele and ele.get_attribute('tagName')=='INPUT' and ele.get_attribute('type')=='checkbox':
            status = ele.is_selected()
            if status != on:
                ele.click()
        else:
            print 'element is not checkbox object'

    def radio_box(self, locator, on=True):
        ele = self.get_element(locator)
        if ele and ele.get_attribute('tagName')=='INPUT' and ele.get_attribute('type')=='radio':
            status = ele.is_selected()
            if status != on:
                ele.click()
        else:
            print 'element is not checkbox object'