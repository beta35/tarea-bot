import discord
from main import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Hola'):
        await message.channel.send("Hola")
    elif message.content.startswith('$chao'):
        await message.channel.send(":wave:")
    elif message.content.startswith('$contraseña'):
        await message.channel.send("Tu contraseña es: "+gen_pass(10))  
    elif message.content.startswith('$Emoji'):
        await message.channel.send("tu emoji es: "+gen_emodji(3))   
    elif message.content.startswith('$Lanza una moneda'):
        await message.channel.send("tu resultado es: "+flip_coin(2))    
    else:
    
        await message.channel.send(message.content)

client.run("")
