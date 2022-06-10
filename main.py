import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
Heroku = os.environ.get("HEROKU", "APP-NAME")
APP_URL = "https://"+ Heroku +".herokuapp.com/" + BOT_TOKEN
from flask import Flask, request
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	
    
    
    mas = types.InlineKeyboardMarkup(row_width=2)
    
    A = types.InlineKeyboardButton(text ="(KKKK4)", callback_data="F1")
    
    E = types.InlineKeyboardButton(text ="(FF8FF)", callback_data="F2")
    
    K = types.InlineKeyboardButton(text ="(K_8_U)", callback_data="F3")
    
    J = types.InlineKeyboardButton(text ="(N_G_6)", callback_data="F4")
    
    I = types.InlineKeyboardButton(text ="(B_5_7)", callback_data="F5")
    
    O = types.InlineKeyboardButton(text ="(I_C_E)", callback_data="F6")

    F = types.InlineKeyboardButton(text ="(UUU8UU)", callback_data="F7")
    
    M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
    
    mas.add(A,E,K,J,I,O,F)
    mas.add(M)
    
    bot.send_message(message.chat.id, f"- أهلاً بكً  !\n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
    
    
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="N_B_1":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="(KKKK4)", callback_data="F1")

		E = types.InlineKeyboardButton(text ="(FF8FF)", callback_data="F2")
		
		K = types.InlineKeyboardButton(text ="(Q_8_P)", callback_data="F3")
		
		J = types.InlineKeyboardButton(text ="(N_G_6)", callback_data="F4")
		
		I = types.InlineKeyboardButton(text ="(B_5_7)", callback_data="F5")
		
		O = types.InlineKeyboardButton(text ="(I_C_E)", callback_data="F6")
		
		F = types.InlineKeyboardButton(text ="(9UUUUU)", callback_data="F7")
		
		M = types.InlineKeyboardButton('قناه البوت', url='https://t.me/N_B_10')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- أهلاً بكً عزيزي المستخدم \n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)

	elif call.data =="F1":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xa = "1234567890"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			us1 = str(us)+str(us)+str(us)+str(us)+str(ua)
			us2 = str(us)+str(us)+str(us)+str(ua)+str(us)
			us3 = str(us)+str(us)+str(ua)+str(us)+str(us)
			us4 = str(us)+str(ua)+str(us)+str(us)+str(us)
			d = [us1,us2,us3,us4]
			h = random.choice(d)
			url = "https://t.me/"+d
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{h}\n────── • ✧✧ • ──────\n•مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{h}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
			
		
		
	elif call.data =="F2":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xm = "0987654321"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			bs = str(''.join(random.choice(xm)for i in range(1))) 
			u2 = str(us)+str(bs)+str(us)+str(us)+str(us)
			u3 = str(us)+str(us)+str(bs)+str(us)+str(us)
			u4 = str(us)+str(us)+str(us)+str(bs)+str(us)
			u5 = str(us)+str(us)+str(us)+str(us)+str(bs)
			h = [u2,u3,u4,u5]
			li = random.choice(h)
			url = "https://t.me/"+li
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{li}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}', callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{li}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
		
	elif call.data =="F3":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			username = str(us)+"_"+str(un)+"_"+str(ua)
			url = "https://t.me/"+str(username)
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{username}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
				
	elif call.data =="F4":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			username = str(us)+"_"+str(ua)+"_"+str(un)
			url = "https://t.me/"+str(username)
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{username}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
	elif call.data =="F5":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xh = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xh)for i in range(1)))
			username = str(us)+"_"+str(un)+"_"+str(ua)
			url = "https://t.me/"+str(username)
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{username}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
				
	elif call.data =="F6":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xu)for i in range(1)))
			ua = str(''.join(random.choice(xu)for i in range(1)))
			username = str(us)+"_"+str(un)+"_"+str(ua)
			url = "https://t.me/"+str(username)
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{username}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
	elif call.data =="F7":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			h1 = str(us)+str(un)+str(us)+str(us)+str(us)+str(us)
			h2 = str(us)+str(us)+str(un)+str(us)+str(us)+str(us)
			h3 = str(us)+str(us)+str(us)+str(un)+str(us)+str(us)
			h4 = str(us)+str(us)+str(us)+str(us)+str(un)+str(us)
			h5 = str(us)+str(us)+str(us)+str(us)+str(us)+str(un)
			K_8_U = [h1,h2,h3,h4,h5]
			j = random.choice(K_8_U)
			url = "https://t.me/"+j
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{j}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{j}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				K_8_U = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,K_8_U)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)			


@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
  
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://"+ Heroku +".herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
