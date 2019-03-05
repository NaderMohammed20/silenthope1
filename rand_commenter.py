
import requests
import json
import time
import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')

print "Facebook Page Post Commenter =>"

		
def comment():
	ID			= raw_input("Your PAGE OR POST ID : ")
	access 		= raw_input("Your ACCESS File : ")
	access		= open(access).readlines()
	xxx 		= int(len(access))
	comments 	= raw_input("Your Comments File : ")
	comments	= open(comments).readlines()
	xx = int(len(comments))
	print 'Total comments equel => ' + str(xx)
	print 'Total Access equel => ' + str(xxx)
	print ""
	print"#############################################"
	print ""
	
	limit			= int(raw_input("Your limit for comments : "))
	t				= int(raw_input("Your timer in seconds : "))
	print ""
	i = 1
	
	for access in access :
		x = int(random.uniform(0, int(xx) ))
		comment = comments[x]
		bd = requests.get("https://graph.facebook.com/"+ ID +"/comments?message="+ comment +"&access_token="+access+"&method=POST")
		try:
			if "id" in bd.json() :
				print "Done => " + str(i)
				i += 1
			if  i > int(limit)  :
				break
			time.sleep(t)
		except IndexError:
			print ""
			print 'No More Access Dummass :3'
			break
		
	print ""
	print "DONE :3"
	print ""

	
	

comment()

print"#############################################"



