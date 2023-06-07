import discord
import json
import os
import tensorflow as tf
from classificar import prediction
from menu import help

js = open('token.json')
useful = json.load(js)

# Define os intents que o bot usará
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

bot_channel_id = useful['canal']


@client.event
async def on_ready():
    # o bot está conectado e pronto para ser usado
    print('Conectado como {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == bot_channel_id:  
        if str(message.content).startswith("!predict") and message:
            if len(message.attachments) == 0:
                await message.channel.send("Perai... não estou vendo nenhuma imagem para classificar!") 
                return
            elif len(message.attachments) > 1:
                await message.channel.send("Ei, você só pode enviar uma imagem por vez!") 
                return
            elif str(message.attachments[0].url).split(".")[-1] not in useful["image_format"]:
                await message.channel.send("hmmm... eu não aceito esse tipo de imagem, desculpa!") 
                return
            predicao = prediction(message.attachments[0].url)
            await message.channel.send(f'{predicao}')

        if message.content.lower().startswith('oi'):
            await message.channel.send(f'Olá {message.author}! Espero que esteja bem')
        
        if(message.content.lower().startswith('!help')):
            await message.channel.send(help())

        if message.content.lower().startswith('boa noite'):
            await message.channel.send(f'Boa noite {message.author}! Durma bem, até mais <3')
        
        if message.content.lower().startswith('bom dia'):
            await message.channel.send(f'Bom dia {message.author}! Vamos nessa! <3')

    

# inicia o bot com o token
client.run(useful['token'])