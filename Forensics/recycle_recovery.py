#This script recovers files from the Recycle Bin in windows, even those that are not visible while browsing with the File Explorer.
#Based on the script from the book Violent Python, but also recovers the files instead of just displaying the name.

import os
import optparse
from _winreg import *




def sid2user(sid):
	try:
		key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" + '\\' + sid)
		(value, type) = QueryValueEx(key, 'ProfileImagePath')
		user = value.split('\\')[-1]
		return user
	except:
		return sid
		
		
		
def returnDir():
	dirs=['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
	for recycleDir in dirs:
		if os.path.isdir(recycleDir):
			return recycleDir
	return None
	

def findRecycled(recycleDir):
	dirList = os.listdir(recycleDir)
	for sid in dirList:
		files = os.listdir(recycleDir + sid)
		user = sid2user(sid)
		print '\n[*] Listing Files For User: ' + str(user)
		for file in files:
			print '[+] Found File: ' + str(file)
			os.system('type '+ '\"' + recycleDir + sid + '\\' + str(file) + '\" > recovered_files/' + str(file))
			print 'type '+ '\"' + recycleDir + sid + '\\' + str(file) + '\" > recovered_files/' + str(file)
		

def main():
	recycledDir = returnDir()
	findRecycled(recycledDir)
	
if __name__ == '__main__':
	main()
