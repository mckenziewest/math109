#!/bin/python3

# a script for publishing content that's ready to go!
# this script should be executed from root level in this repo.

dry_run = False

import markdown2canvas as mc

import subprocess
import os
import tex_ready_docs


from course_info import course

tex_ready_docs.tex_if_needed(verbose=False)

print("-------------\nTeX Check Complete\n-------------")

# filename = 'ready_to_publish.txt'
filename = 'publish_this_time.txt'
force = True
do_not_upload = 'do_not_reupload.txt'

with open(filename,'r') as f:
	ready_files = f.read().split('\n')
with open(do_not_upload,'r') as f:
    do_not_replace = f.read().split('\n')

ready_files = [f'{f}' for f in ready_files if f and not f in do_not_replace]

print(ready_files)

if "../course_calendar.page" in ready_files:
	print("updating calendar source")
	leaving = os.getcwd()
	os.chdir("..\\course_calendar.page\\")
	x = subprocess.call(f'python gen_calendar.py')


if "../course_activities.page" in ready_files:
	print("updating activities source")

	leaving = os.getcwd()
	os.chdir("..\\course_activities.page\\")
	x = subprocess.call(f'python gen_calendar.py')
	os.chdir(leaving)



print(f'publishing to {course.name}')

def make_mc_obj(f,course):
	if f.endswith('page'):
		return mc.Page(f,course)
	if f.endswith('assignment'):
		return mc.Assignment(f,course)
	if f.endswith('link'):
		return mc.Link(f)
	if f.endswith('file') or f.endswith('slides'):
		return mc.File(f)


for f in ready_files:
    print(f)
    obj = make_mc_obj(f.strip(),course)
    if not dry_run:
        obj.publish(course, overwrite=True)
    else:
        print(f'[dry run] publishing {obj}')