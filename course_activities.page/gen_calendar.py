# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:18:29 2022

@author: WESTMR

There should be a text file with the daily schedule for the course in a
file named "basic_schedule.txt". The content from this schedule will be placed
sequentially in a grid with 3 columns.

TODO Make this a csv with columns: short description, long description, reading, notes
"""
from bs4 import BeautifulSoup
import datetime

import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from _tools.course_info import course

with open('source.md','r',encoding="utf-8") as current_calendar:
    html_source = current_calendar.read()
    
soup = BeautifulSoup(html_source,'html.parser')
table_body = soup.table.tbody
table_body.clear()

assignments = course.get_assignments()
all_assignments = {}
for hw in assignments:
    hw_dict = {}
    try:
        due_at = hw.due_at_date
        label = datetime.date(due_at.year,due_at.month,due_at.day)
        hw_dict['name'] = hw.name
        hw_dict['href'] = hw.html_url
        if label in all_assignments:
            all_assignments[label].append(hw_dict)
        else:
            all_assignments[label]= [hw_dict]
    except:
        continue

with open('..\\course_calendar.page\\basic_schedule.txt','r') as list_form:
    calendar = list_form.read().split('\n')

with open('readings.txt','r') as list_form:
    readings = list_form.read().split('\n')

with open('preclass.txt','r') as list_form:
    preclass = list_form.read().split('\n')

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
first = datetime.date(2023,9,6)
last = datetime.date(2023,12,15)
class_meeting_days = [0,2,3,4] # MWThF
spring_term = False
spring_break = datetime.date(2023,3,20)
break_days = [datetime.date(2023,9,4),datetime.date(2023,11,22),datetime.date(2023,11,23),datetime.date(2023,11,24)]
one_day = datetime.timedelta(days=1)
two_days = datetime.timedelta(days=2)
three_days = datetime.timedelta(days=3)
seven_days = datetime.timedelta(days=7)

current_day = first
week_number = 1
ii = 0


while current_day <= last:
    new_tr = soup.new_tag("tr")
    new_th = soup.new_tag('th')

    # First column is day and date
    wkday = weekdays[current_day.weekday()]
    new_th.string = f"{wkday[:3]} {current_day.month}/{current_day.day}"
    new_th['style'] = "padding-bottom:10px;padding-top:10px;"
    new_tr.append(new_th)

    # Remaining columns come from text files
    for content_list in [calendar,readings,preclass]:
        new_td = soup.new_tag('td')
        if current_day in break_days and content_list == calendar:
            content = "No Class"
        elif ii < len(content_list):
            content = content_list[ii]
        else:
            content = ''
        new_td.string = f"{content}"
        new_td['style'] = "padding-bottom:10px;padding-top:10px;"
        new_tr.append(new_td)

    # Canvas assignment column
    new_td = soup.new_tag('td')
    new_td['style'] = "padding-bottom:10px;padding-top:10px;"
    if current_day in all_assignments:
        for asnt in all_assignments[current_day]:
            new_a = soup.new_tag('a', attrs=asnt)
            new_a.string = asnt['name']
            new_td.append(new_a)
            new_td.append(soup.new_tag('br'))
    new_tr.append(new_td)
    table_body.append(new_tr)
    # Increment counter
    if current_day not in break_days:
        ii += 1
    
    # Find the next day

    current_day += one_day 
    while current_day.weekday() not in class_meeting_days:
        
        current_day += one_day 
    #if current_day.weekday()==0:
    #    current_day = current_day + two_days
    #elif current_day.weekday() in [2,3]:
    #    current_day = current_day + one_day
    #elif current_day.weekday() == 4:
    #   current_day = current_day + three_days

with open('source.md','w',encoding="utf-8") as current_calendar:
    current_calendar.write(soup.prettify())