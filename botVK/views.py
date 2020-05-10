from django.views.decorators.csrf import csrf_exempt 
from django.http import HttpResponse
from django.shortcuts import render
import json, vk, random
import sqlite3

vk.Session(access_token="e4116669eab6306f879a7b64e954f7205bfdef0508e20c5f4a66b3b2df1e83ccadb85e4a0d281933b9513")
vkAPI = vk.API(session)

@csrf_exempt
def bot(request):
	body = json.loads(request.body)
	print(body)

	if body == {"type": "confirmation", "group_id": 194135920}:
		return HttpResponse("9c2d8b02")

if body["type"] == "message_new":
		
		msg = body["object"]["message"]["text"]
		userID = body["object"]["message"]["from_id"]
		userInfo = vkAPI.users.get(user_ids = userID, v=5.103)[0]
		answ = ""
		attach = ""
		# lastMsg = vkAPI.messages.getHistory(user_id = userID, count = 2, v=5.103)["items"][1]["text"]


		if msg == "/list":
			conn = sqlite3.connect('db.sqlite')
			cur = conn.cursor()
			query = """
			SELECT * FROM answer
			"""
			cur.execute(query)
			answ = cur.fetchall()
			conn.close()

		if msg == "/start":
		    answ = """Hello, there some commands you can use:
		    1) /say [message]\n
		    2) /myName\n
		    3) /fish
        elif msg[:4] == "/say":
			answ = msg[5:]
        elif msg == "/myName":
			answ = "Your name is {0} {1}".format(userInfo["first_name"], userInfo["last_name"])
		elif msg == "/fish":
			attach = "doc352991388_547422944""""
			
		sendAnswer(userID, answ, attach)

	return HttpResponse("ok")
# ---Конец функции---
	

def sendAnswer(userID, answ = "", attach = ""):
	vkAPI.messages.send(user_id = userID, message = answ, attachment=attach, random_id = random.randint(1, 99999999999999999), v=5.103)