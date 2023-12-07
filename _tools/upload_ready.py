#!/bin/python3

# a script for publishing content that's ready to go!
# this script should be executed from root level in this repo.

dry_run = False

import markdown2canvas as mc

import subprocess
import os
import tex_ready_docs

from course_info import *

canvas = mc.make_canvas_api_obj(url=canvas_url)
course = canvas.get_course(course_id) 

print("\n-------------\nTeXing documents if needed\n-------------\n")

tex_ready_docs.tex_if_needed(verbose=False)

filename = os.path.join("_tools","publish_this_time.txt")
do_not_upload = os.path.join("_tools","do_not_reupload.txt")

with open(filename,'r') as f:
	ready_files = f.read().split('\n')
with open(do_not_upload,'r') as f:
    do_not_replace = f.read().split('\n')

ready_files = [f'{f}' for f in ready_files if f and not f in do_not_replace]

print(ready_files)

if "course_calendar.page" in ready_files:
	print("\n-------------\nupdating calendar source\n-------------\n")
	leaving = os.getcwd()
	os.chdir("course_calendar.page")
	x = subprocess.call(f'python gen_calendar.py')
	os.chdir(leaving)


if "course_activities.page" in ready_files:
	print("\n-------------\nupdating activities source\n-------------\n")

	leaving = os.getcwd()
	os.chdir("course_activities.page")
	x = subprocess.call(f'python gen_calendar.py')
	os.chdir(leaving)



print(f'publishing to {course.name}')

def make_mc_obj(f):
	if f.endswith('page'):
		return mc.Page(f)
	if f.endswith('assignment'):
		return mc.Assignment(f)
	if f.endswith('link'):
		return mc.Link(f)
	if f.endswith('file') or f.endswith('slides'):
		return mc.File(f)


for f in ready_files:
    print(f)
    obj = make_mc_obj(f.strip())
    if not dry_run:
        obj.publish(course, overwrite=True)
    else:
        print(f'[dry run] publishing {obj}')