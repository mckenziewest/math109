#!/bin/python3

# a script for publishing content that's ready to go!
# this script should be executed from root level in this repo.

dry_run = False

import markdown2canvas as mc

import tex_ready_docs

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


from course_info import course


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