import telebot
from config import API_TOKEN
import os
import random
import requests
 
spisok = os.listdir('images')




bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['mem'])
def send_mem(message):
    rand_image = random.choice(spisok)
    with open(f'images/{rand_image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

def get_dog_image_url():    
        url = 'https://random.dog/woof.json'
        res = requests.get(url)
        data = res.json()
        return data['url']


def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
@bot.message_handler(commands=['dog'])
def dog(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_dog_image_url()
    bot.reply_to(message, image_url)

    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)



bot.infinity_polling()
