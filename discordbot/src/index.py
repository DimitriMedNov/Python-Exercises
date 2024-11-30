#discord: la biblioteca principal para interactuar con la API de Discord.
import discord
#commands de discord.ext: una extensión que proporciona estructuras y decoradores para crear comandos y eventos del bot.
from discord.ext import commands
#urllib.parse: una biblioteca para analizar URL.
import urllib.parse as parse
import urllib.request as request
#re: una biblioteca para expresiones regulares.
import re
import random
import requests
import giphy_client 
from giphy_client.rest import ApiException
import json
import openai
from scipy import spatial

#Crea una instancia de discord.Intents y habilita todos los intents disponibles utilizando discord.
#Intents.all(). Los intents permiten controlar qué eventos y datos puede recibir el bot.
intents = discord.Intents.all()
intents.voice_states = True

#Crea una instancia del bot utilizando commands.Bot(). 
# Se especifica el prefijo de comando como '>' y se pasan los intents creados anteriormente.
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())

temp_channel_count = 0

#Define un comando utilizando el decorador @bot.command(). 
@bot.command()
async def ping(ctx):
    print("Ping command received")
    await ctx.send("pong")

@bot.command()
async def hello(ctx):
    print("hello command received")
    await ctx.send("¿Qué tal? ¿Cómo estás?")

@bot.command()
async def info(ctx):
    print("info command received")
    await ctx.send("¡Hola! Soy el bot de la Gameroom de la Universidad Anahuac Mayab.\nEstoy aquí para ayudarte y responder tus preguntas.\nSi me preguntas qué soy, puedes decir que soy un asistente de inteligencia artificial diseñado para brindar información.")

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    print("Sum command received")
    await ctx.send(numOne + numTwo)

@bot.command()
async def rest(ctx, numOne: int, numTwo: int):
    print("rest command received")
    await ctx.send(numOne - numTwo)

@bot.command()
async def mult(ctx, numOne: int, numTwo: int):
    print("mult command received")
    await ctx.send(numOne * numTwo)

@bot.command()
async def div(ctx, numOne: int, numTwo: int):
    print("div command received")
    await ctx.send(numOne / numTwo)

@bot.command()
async def embed(ctx, member: discord.Member = None):
    print("Embed command received")
    if member is None:
        member = ctx.author

    name = member.display_name
    pfp = member.display_avatar

    embed = discord.Embed(title="Hello my name is J. D'mitri Medina Novelo", description="Currently, I am a student of Information Technology Engineering at Anahuac Mayab University.", color=discord.Colour.random())
    embed.set_author(name=name, url="https://www.linkedin.com/in/jdmtmednov82", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Eo_circle_blue_letter-d.svg/768px-Eo_circle_blue_letter-d.svg.png")
    embed.set_thumbnail(url=pfp)
    embed.set_footer(text=f"{name} Made this embed")

    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    print("kick command received")
    if reason == None:
        reason = "No reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f" User {member.mention} has been kicked from the server.\nReason: {reason}")

@bot.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    print("ban command received")
    if reason == None:
        reason = "No reason provided"
    await ctx.guild.ban(member)
    await ctx.send(f" User {member.mention} has been kicked from the server.\nReason: {reason}")

@bot.command()
async def dog(ctx):
    print("dog command received")
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['message'])
    await ctx.send(embed=em)

@bot.command()
async def cat(ctx):
    print("cat command received")
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    image_url = data[0]['url']
    embed = discord.Embed()
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

@bot.command()
async def gif(ctx, *, q="Smile"):
    print("gif command received")

    api_key = "IIFebx2Rb6nzNb6h1vCTzD1L6c1ICBCG"
    api_instance = giphy_client.DefaultApi()

    try:
        api_responce = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_responce.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(giff.embed_url)

    except ApiException as e:
        print("Exception when calling Api")


@bot.command()
async def sticker(ctx, *, q="Smile"):
    print("sticker command received")

    api_key = "IIFebx2Rb6nzNb6h1vCTzD1L6c1ICBCG"
    api_instance = giphy_client.DefaultApi()

    try:
        api_responce = api_instance.stickers_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_responce.data)
        sticker = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url=sticker.images.fixed_height.url)

        await ctx.channel.send(embed=emb)

    except ApiException as e:
        print("Exception when calling API")


##############################################
# Cargar las preguntas desde el archivo JSON
# with open('preguntas.json', 'r', encoding='utf-8') as file:
#     preguntas = json.load(file)["preguntas"]

# @bot.command()
# async def pregunta(ctx, *, contenido):
#     print("Pregunta command received")
#     respuestas = []  # Lista para almacenar las respuestas encontradas
#     for pregunta in preguntas:
#         if contenido.lower() in pregunta["contenido"].lower():
#             respuestas.append(pregunta["respuesta"])  # Agregar la respuesta a la lista de respuestas
            
#     if respuestas:
#         # Enviar las respuestas en un solo mensaje, separadas por nuevas líneas
#         await ctx.send("\n".join(respuestas))
#     else:
#         await ctx.send("No se encontraron respuestas para la pregunta.")
        
#     # Obtener un sticker aleatorio
#     url = "https://api.giphy.com/v1/stickers/random"
#     api_key = "IIFebx2Rb6nzNb6h1vCTzD1L6c1ICBCG"

#     # Parámetros de la solicitud GET
#     params = {
#         "api_key": api_key,
#         "rating": "g",
#         "limit": 1
#     }

#     try:
#         response = requests.get(url, params=params)
#         if response.status_code == 200:
#             data = response.json()
#             sticker_url = data["data"]["images"]["original"]["url"]

#             emb = discord.Embed()
#             emb.set_image(url=sticker_url)

#             await ctx.channel.send(embed=emb)
#         else:
#             await ctx.send("No se pudo obtener un sticker en este momento.")
#     except Exception as e:
#         print("Error:", e)

##############################################

#############################################

# # Carga el archivo JSON
# with open('pregunta.json', 'r') as file:
#     data = json.load(file)

# # Configura tu clave de OpenAI
# openai.api_key = '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'

# # Función para buscar una respuesta en base al contexto del archivo JSON
# def buscar_respuesta(pregunta):
#     contexto = '\n'.join([item['contenido'] for item in data['preguntas']])
#     respuesta = openai.Completion.create(
#         engine='text-davinci-003',
#         prompt=contexto,
#         max_tokens=100,
#         temperature=0.7,
#         n=1,
#         stop=None,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.0
#     )
#     return respuesta.choices[0].text.strip()

# # Comando para hacer una pregunta utilizando la API de OpenAI y el contexto del archivo JSON
# @bot.command()
# async def pregunta_openai(ctx, *, pregunta):
#     print("pregunta_openai command received")
#     respuesta = buscar_respuesta(pregunta)
#     if respuesta:
#         respuesta_encoded = respuesta.encode("utf-8")
#         await ctx.send(respuesta_encoded.decode("utf-8"))
#     else:
#         await ctx.send("Lo siento, no encontré una respuesta para esa pregunta.")


#############################################

# Configura tu clave de API de OpenAI
openai.api_key = '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'

from sentence_transformers import SentenceTransformer

# Carga el modelo pre-entrenado
model = SentenceTransformer('bert-base-nli-mean-tokens')

# Carga los datos del archivo JSON
with open('preguntas.json') as file:
    data = json.load(file)

# Genera los embeddings y agrega la información al archivo JSON
for pregunta in data['preguntas']:
    contenido = pregunta['contenido']
    respuesta = pregunta['respuesta']
    embedding = model.encode([contenido + ' ' + respuesta])[0].tolist()
    pregunta['embedding'] = embedding

# Guarda los datos actualizados en el archivo JSON
with open('preguntas_con_embeddings.json', 'w') as file:
    json.dump(data, file, indent=4)



from sentence_transformers import SentenceTransformer

# Carga el archivo "preguntas_con_embeddings.json"
with open("preguntas_con_embeddings.json", "r") as file:
    data = json.load(file)

# Carga el modelo de SentenceTransformer
model = SentenceTransformer('paraphrase-xlm-r-multilingual-v1')

# Comando "pregunta"
@bot.command()
async def pregunta(ctx, consulta):
    print("Pregunta command received")
    # Genera el embedding de la consulta del usuario
    consulta_embedding = model.encode([consulta])[0]

    # Busca la pregunta más similar utilizando embeddings
    preguntas = data["preguntas"]
    mejor_similitud = -1
    mejor_respuesta = ""

    for pregunta in preguntas:
        pregunta_embedding = pregunta["embedding"]
        similitud = 1 - spatial.distance.cosine(consulta_embedding, pregunta_embedding)

        if similitud > mejor_similitud:
            mejor_similitud = similitud
            mejor_respuesta = pregunta["respuesta"]

    await ctx.send(f"Mejor respuesta: {mejor_respuesta}")


















@bot.command()
async def clear(ctx, amount=5):
    print("clear command received")
    # Verificar si el autor del mensaje es un moderador o tiene los permisos necesarios
    if ctx.message.author.guild_permissions.manage_messages:
        # Eliminar el mensaje del comando
        await ctx.message.delete()

        # Eliminar los mensajes antiguos en el canal actual
        deleted = await ctx.channel.purge(limit=amount)
        
        # Enviar un mensaje de confirmación
        await ctx.send(f'Se eliminaron {len(deleted)} mensajes.', delete_after=5)
    else:
        await ctx.send('No tienes permisos para usar este comando.')


@bot.command()
async def meme(ctx):
    print("meme command received")
    
    subreddit = "memes"  # Subreddit de donde se obtendrán los memes
    url = f"https://www.reddit.com/r/{subreddit}/random/.json"
    
    headers = {'User-Agent': 'Mozilla/5.0'}  # Encabezados para simular un navegador web
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        meme = data[0]['data']['children'][0]['data']
        meme_url = meme['url']
        
        em = discord.Embed()
        em.set_image(url=meme_url)
        await ctx.send(embed=em)
    else:
        await ctx.send("No se pudo obtener un meme en este momento.")

@bot.event
async def on_voice_state_update(member, before, after):
    global temp_channel_count

    if before.channel is None and after.channel is not None:
        # Se ha unido a un canal de voz
        category = after.channel.category
        temp_channel_count += 1
        channel_name = f'vc-{temp_channel_count}'

        overwrites = {
            category.guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=False),  # Restringir acceso y visibilidad a usuarios sin roles
            category.guild.me: discord.PermissionOverwrite(connect=True, view_channel=True),  # Permitir acceso y visibilidad al bot
        }

        for role in member.roles:
            if role.name == 'admin':
                overwrites[role] = discord.PermissionOverwrite(connect=True, view_channel=True)  # Permitir acceso y visibilidad a usuarios con rol "admin"
                break

        new_channel = await category.create_voice_channel(channel_name, overwrites=overwrites)
        await member.move_to(new_channel)
        print(f'Temporary channel created: {new_channel.name}')

    elif before.channel is not None and after.channel is None:
        # Se ha salido de un canal de voz
        channel = before.channel
        if channel.name.startswith('vc-'):
            await channel.delete()
            temp_channel_count -= 1
            print(f'Removed temporary channel: {channel.name}')

@bot.event
async def on_guild_channel_create(channel):
    # Verifica si el canal creado es un canal temporal
    if channel.name.startswith('temp-'):
        # Añade el canal temporal a la estructura de datos
        temp_channel_count[channel.id] = channel
        print(f'A new temporary channel has been created: {channel.name}')

@bot.command()
async def create_temp_channel(ctx):
    # Crea un canal temporal en la categoría deseada
    category_id = 1234567890  # Reemplaza con la ID de la categoría deseada
    category = ctx.guild.get_channel(category_id)
    new_channel = await category.create_voice_channel(name='temp-channel')
    temp_channel_count[new_channel.id] = new_channel
    print(f'A new temporary channel has been created: {new_channel.name}')

#Define un evento on_ready utilizando el decorador @bot.event. 
# Este evento se activa cuando el bot se ha conectado correctamente a Discord. 
@bot.event
async def on_ready():
    # En este caso, simplemente imprime un mensaje indicando que el bot está listo.
    print('Bot is ready')


#Ejecuta el bot utilizando bot.run() y proporciona el token de tu bot de Discord. 
#El token es necesario para que el bot se conecte a tu servidor de Discord.
bot.run('MTExMDY0NzY3NTQ5NTQwMzUzMQ.G4Wi4h.jgkRt38Nqk2karfzhsbDin17M__ybhg2SIImWc')

