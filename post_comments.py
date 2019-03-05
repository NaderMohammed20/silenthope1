import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

print "Facebook Page OR Post Comments extractor =>"
ID = raw_input("Your PAGE OR POST ID : ")
access = raw_input("Your ACCESS : ")
file = open(ID+".txt", "a+")
print ""
print"#############################################"
print ""
def extract_comments():

	limit = int(raw_input("Your limit for comments : "))
	print ""
	
	for i in range(0, limit):

		bd = requests.get("https://graph.facebook.com/"+ ID +"/comments?fields=message&limit="+ str(limit) +"&access_token="+access)
		
		try:
			file.write(bd.json()['data'][i]['message']+"\n")
			i += 1
			print "Done => " + str(i)
			if  i == int(limit)  :
				break
				
		except IndexError:
			print ""
			print 'No More Dummass :3'
			break
		
	print ""
	print "DONE :3"
	print ""


extract_comments()

print"#############################################"
