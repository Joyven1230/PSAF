#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PageBase import PageBase
from Locator import Locator

class BaiduHome(PageBase):
    def __init__(self, wd):
        PageBase.__init__(self, wd, Locator)

    def __del__(self):
        pass

    def key_worlds_input(self, value):
        self.get_element('KEY_WORLDS').send_keys(value)

    def search_click(self):
        self.get_element('SEARCH').click()


