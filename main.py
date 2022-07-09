import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SUDO = int(os.environ.get("SUDO","5359109940"))
Heroku = os.environ.get("HEROKU", "APP-NAME")
APP_URL = "https://"+ Heroku +".herokuapp.com/" + BOT_TOKEN
from flask import Flask, request
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

ban = ['T_4_Y','K_M_E','F_8_W','Z_K_1','T_N_3',
       'Y_L_6','K_A_2','S_X_1','C_R_J','Y_6_S',
       'F_P_7','Q_I_9','R_Y_2','I_M_9','C_J_7',
       'T_P_4','Y_P_7','Q_K_9','C_J_7','J_I_2',
       'M_K_6','H_B_3','E_G_8','J_I_2','C_B_6',
       'A_D_6','L_O_8','O_Y_1','C_T_7','Y_O_4',
       'S_X_9','Y_E_5','U_C_7','U_T_3','N_P_6',
       'Q_I_9','B_W_9','Q_H_1','P_L_3','N_X_8',
       'E_G_8','I_J_4','Y_E_5','P_R_0','F_M_0',
       'Q_L_4','J_J_9','B_M_9','E_G_8','P_K_9',
       'U_T_3','G_V_5','R_A_4','R_Y_2','M_J_8',
       'F_D_5','Y_E_5','Q_K_9','M_K_6','X_D_4',
       'Y_P_1','Z_K_1','S_E_4','C_J_7','T_Z_7',
       'X_T_7','S_X_1','V_F_9','W_P_6','O_Y_1',
       'C_D_6','C_F_5','S_X_9','U_X_0','J_I_2',
       'J_J_3','X_W_4','I_M_9','X_U_4','T_J_8',
       'O_Y_1','Q_K_9','I_6_W','B_6_V','Y_4_N',
       'P_9_T','V_8_W','T_2_Y','J_9_N','A_7_C',
       'X_7_W','C_1_K','O_9_F','G_8_M','L_3_D',
       'P_3_M','W_5_F','N_7_G','P_1_R','U_8_Q',
       'K_9_P','P_8_P','T_9_L','C_2_N','C_2_N',
       'S_0_N','I_5_N','T_5_O','R_5_C','A_1_C',
       'L_4_Y','B_6_V','H_8_D','J_3_M','T_5_O',
       'T_6_S','T_5_O','V_5_C','P_9_H','G_5_L',
       'V_6_M','E_0_P','R_1_D','W_0_C','J_8_C',
       'V_4_E','N_7_G','Z_4_V','G_1_P','Q_8_P',
       'L_3_D','V_8_W','B_4_D','X_6_L','X_7_W',
       'R_6_R','H_0_Y','X_9_Y','A_1_N','F_0_I',
       'E_5_Q','F_3_E','O_3_K','F_0_L','C_0_S',
       'K_4_Y','B_0_X','B_8_B','D_5_H','B_0_E',
       'F_2_I','Q_5_T','Z_9_W','A_1_N','W_1_J',
       'B_0_S','W_8_H','E_J_Q','N_Y_V','H_H_A',
       'Z_L_P','U_H_B','F_C_T','Q_X_I','I_G_U',
       'S_X_X','C_F_Y','J_Y_K','Q_D_G','O_C_O',
       'V_T_G','D_U_U','Q_V_K','G_C_E','P_F_D',
       'W_B_G','X_B_K','A_F_T','W_W_L','T_J_Y',
       'Q_V_H','P_T_Z','U_X_O','F_U_V','G_M_F',
       'S_G_T','B_Q_L','X_H_F','F_O_M','P_N_X',
       'L_B_D','X_N_S','X_J_C','O_Z_T','I_F_M',
       'A_P_S','G_M_F','I_S_B','O_K_G','B_W_P',
       'N_P_B','I_P_S','G_U_J','U_D_B','W_L_N',
       'X_X_A','K_X_X','A_D_L','F_F_W','Y_P_U',
       'I_W_T','N_Y_B','K_M_E','B_I_X','W_O_R',
       'O_K_G','K_S_H','G_L_J','A_S_S','U_H_B',
       'F_L_G','A_A_C','W_D_V','F_O_F','B_J_O',
       'X_E_S','K_T_W','P_Y_Q','V_B_B','S_B_W',
       'T_C_N','T_P_J','H_U_I','W_I_R','U_H_B',
       'W_O_R','H_D_X','N_Y_B','B_I_O','E_K_W',
       'D_X_V','R_I_K','C_N_C','C_F_Y','A_E_G',
       'C_H_T','O_M_T','Y_W_J','A_A_C','B_X_J',
       'U_G_C','X_N_S','Y_S_R','E_Q_C','H_K_E',
       'B_X_Z','D_D_W','X_E_S','B_X_Z','B_D_L',
       'A_F_T','D_X_V','X_C_Z','I_G_T','I_W_T',
       'X_W_V','H_V_R','X_S_I','K_S_U','E_J_Q',
       'P_G_N','U_X_O','B_X_B','W_U_B','T_P_J',
       'D_S_O','R_G_C','Q_U_W','E_T_U','F_C_T',
       'K_Q_N','U_D_B','Q_A_U','D_J_X','R_I_Q',
       'B_V_N','Q_D_W','T_J_Y','W_D_V','B_X_C',
       'Y_W_J','T_P_V','T_D_T','D_S_O','I_F_M',
       'X_N_P','Q_U_W','Q_D_O']

@bot.message_handler(commands=["start"])
def start(message):
	f = message.from_user.id
	if f == SUDO:
		mas = types.InlineKeyboardMarkup(row_width=2)
		K = types.InlineKeyboardButton(text ="(يوزرات ثلاثيه)", callback_data="SS")	
		G = types.InlineKeyboardButton(text ="(يوزرات بوتات)", callback_data="F8")
		V = types.InlineKeyboardButton(text ="(يوزرات مميزه)", callback_data="F100")
		M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
		mas.add(G,K)
		mas.add(V)
		mas.add(M)
		bot.send_message(message.chat.id, text=f"- أهلاً {message.from_user.first_name}  !\n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
	else:
		rr = types.InlineKeyboardMarkup(row_width=2)
		me = types.InlineKeyboardButton(text="مجهول",url="https://t.me/k_8_u")
		he = types.InlineKeyboardButton(text="حلم",url="https://t.me/n_n_v")
		de = types.InlineKeyboardButton(text="دراكون",url="https://t.me/s_l_3")
		ch = types.InlineKeyboardButton(text="▶ قناة البوت ◀",url="https://t.me/c_p_8")
		rr.add(me,he,de)
		rr.add(ch)
		bot.send_message(message.chat.id,text="هذا البوت مدفوع وليس لك\n للتفعيل راسل",reply_markup=rr)
               
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="K_8_U":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="(KKKK4)", callback_data="F1")

		E = types.InlineKeyboardButton(text ="(FF8FF)", callback_data="F2")
		
		K = types.InlineKeyboardButton(text ="(Q_8_P)", callback_data="F3")
		
		J = types.InlineKeyboardButton(text ="(N_G_6)", callback_data="F4")
		
		I = types.InlineKeyboardButton(text ="(B_5_7)", callback_data="F5")
		
		O = types.InlineKeyboardButton(text ="(I_C_E)", callback_data="F6")
		
		F = types.InlineKeyboardButton(text ="(UUU4UU)", callback_data="F7")
		
		M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- أهلاً بكً عزيزي المستخدم \n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
	elif call.data == "SS":
		v = types.InlineKeyboardMarkup(row_width=2)
		K = types.InlineKeyboardButton(text ="(Q_8_P)", callback_data="F3")
		J = types.InlineKeyboardButton(text ="(N_G_6)", callback_data="F4")
		I = types.InlineKeyboardButton(text ="(B_5_7)", callback_data="F5")
		O = types.InlineKeyboardButton(text ="(I_C_E)", callback_data="F6")
		S = types.InlineKeyboardButton(text ="(G_K_K)", callback_data="F10")
		B = types.InlineKeyboardButton(text="رجوع",callback_data="bckkk")
		v.add(K,J,O,I,S)
		v.add(B)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اختر من القائمه بالاسفل .",reply_markup=v)
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
			url = "https://t.me/"+h
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and d not in ban:
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
				
			
	elif call.data =="F8":
		e = types.InlineKeyboardMarkup(row_width=2)
		f = types.InlineKeyboardButton(text="(c8bot)",callback_data="b1")
		c = types.InlineKeyboardButton(text="(vd2bot)",callback_data="b2")
		z = types.InlineKeyboardButton(text="(wdv4bot)",callback_data="b4")
		bc = types.InlineKeyboardButton(text="رجوع",callback_data="bckkk")
		e.add(f,c,z)
		e.add(bc)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اختر من القائمه بالاسفل .",reply_markup=e)
	elif call.data =="F100":
		e = types.InlineKeyboardMarkup(row_width=2)
		f = types.InlineKeyboardButton(text="(vv_vv)",callback_data="ew1")
		c = types.InlineKeyboardButton(text="(UUU4UU)",callback_data="F7")
		d = types.InlineKeyboardButton(text="(FFAAA)",callback_data="ew")
		z = types.InlineKeyboardButton(text="(KKKK4)",callback_data="F1")
		bc = types.InlineKeyboardButton(text="رجوع",callback_data="bckkk")
		e.add(f,c,z,d)
		e.add(bc)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اختر من القائمه بالاسفل .",reply_markup=e)
	elif call.data =="bckkk":
		mas = types.InlineKeyboardMarkup(row_width=2)
		K = types.InlineKeyboardButton(text ="(يوزرات ثلاثيه)", callback_data="SS")	
		G = types.InlineKeyboardButton(text ="(يوزرات بوتات)", callback_data="F8")
		V = types.InlineKeyboardButton(text ="(يوزرات مميزه)", callback_data="F100")
		M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
		mas.add(G,K)
		mas.add(V)
		mas.add(M)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- أهلاً بكً عزيزي المستخدم \n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
		
	
	elif call.data =="b4":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(u1s)+str(u2s)+str(un)+"bot"
			u2 = str(us)+str(un)+str(u2s)+str(u1s)+"bot"
			u3 = str(us)+str(u1s)+str(un)+str(u2s)+"bot"
			g = [u1,u2,u3]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
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
	
	elif call.data =="ew1":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(us)+"_"+str(us)+str(us)
			u2= str(us)+"_"+str(us)+str(us)+str(us)
			u3= str(us)+str(us)+str(us)+"_"+str(us)
			g = [u1,u2,u3]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{x}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="ew":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(us)+str(us)+str(u1s)+str(u1s)
			u2= str(u1s)+str(u1s)+str(us)+str(us)+str(us)
			g = [u1,u2]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{x}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="b2":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(u1s)+str(un)+"bot"
			u2 = str(us)+str(u1s)+str(u2s)+"bot"
			u3 = str(us)+str(un)+str(u1s)+"bot"
			g = [u1,u2,u3]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{x}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	
		
	elif call.data =="b1":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(un)+"bot"
			u2 = str(us)+str(u1s)+"bot"
			f = [u1,u2]
			v = random.choice(f)
			url = "https://t.me/"+v
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and f not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{v}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{v}', callback_data="1x")
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
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(u1s)+"_"+str(u2s)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F5":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(un)+"_"+str(u1n)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
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
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(u1s)+"_"+str(un)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
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
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(un)+"_"+str(u1s)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
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
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and j not in ban:
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
				
	elif call.data =="F10":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(us)+"_"+str(u2s)
			d = str(u1s)+"_"+str(us)+"_"+str(us)
			v = str(us)+"_"+str(u1s)+"_"+str(us)
			p = str(us)+"_"+str(un)+"_"+str(us)
			m = str(us)+"_"+str(us)+"_"+str(un)
			i = str(us)+"_"+str(un)+"_"+str(un)
			cs = [c,d,v,p,m,i]
			cc = random.choice(cs)
			url = "https://t.me/"+cc
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and cs not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{cc}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{cc}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
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
