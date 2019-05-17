#encoding: utf8

import logging,os,time

 
def main():
	ProList = os.system('tasklist |findstr "iexplore.exe"')
	if ProList != 0 :
		#os.system('taskkill /f /im iexplore.exe')
		os.startfile("d:\iexplore.exe.lnk")
	
if __name__=="__main__" : 
        while True: 
                main() 
                time.sleep(1)


