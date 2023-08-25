# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:18:48 2022

@author: WESTMR
"""
from course_info import course

import markdown2canvas as mc

destination = 'downloaded_pages' 

my_filter = lambda title: 'Homework' in title

#mc.download_pages(destination, course,even_if_exists=True, name_filter=my_filter)
mc.download_assignments(destination, course,even_if_exists=True, name_filter=my_filter)