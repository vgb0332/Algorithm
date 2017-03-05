# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

def disk_size(path):
	total = os.path.getsize(path);
		
	if(os.path.isdir(path)):
		child_list = os.listdir(path)
		child_list_len = len(child_list)
		for i in range (child_list_len):
			child_path = os.path.join(path, child_list[i])
			total = total + disk_size(child_path)
	
	print "{0:<7}{1}".format(total, path)
	return total
	
path = raw_input()
if(os.path.exists(path)):
	print 
	print (disk_size(path))
