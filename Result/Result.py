#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import logging.config

logging.config.fileConfig("logger.conf")
resulter = logging.getLogger("result")
infor = logging.getLogger("infomation")

resulter.critical('PASS')
resulter.critical('FAIL')

infor.debug("The debug message")
infor.info('The info message')
infor.warning('The warning message')




