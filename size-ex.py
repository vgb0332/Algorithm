# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

#definition of disk_size function
def disk_size(path):
	total = 0;
	#if file, total size = file size
	if(os.path.isfile(path)):
		total = os.path.getsize(path)
	
	#if dir, acheive list of its sub dir and find each size
	if(os.path.isdir(path)):
		child_list = os.listdir(path)
		child_list_len = len(child_list)
		for i in range (child_list_len):
			child_path = os.path.join(path, child_list[i])
			total = total + disk_size(child_path)
	
	#print each size and the path name
	print "{0:<7}{1}".format(total, path)
	return total
	
#achieve the path input and if path is valid, print the total size
path = raw_input()
if(os.path.exists(path)):
	print 
	print (disk_size(path))
