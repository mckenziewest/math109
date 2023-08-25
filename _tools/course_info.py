# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 09:35:39 2022

@author: WESTMR
"""
from canvasapi import Canvas
from maccess import API_KEY, API_URL

course_id = 593755
canvas_url = "https://uws.instructure.com/"

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(course_id) 

    