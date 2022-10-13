import discord
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz
import os
token = os.environ.get('BOT_TOKEN')

client = discord.Client(intents=discord.Intents.default())

narodeniny = None;

arr = [
["Rišo", 25, 2, 287215120805789696],
["Filip", 13, 7, 323515888974168064],
["Peťo", 29, 7, 330317061374869504],
["Vikina", 14, 10, 756937170362695782],
["Maroš", 17, 5, 303842110396956672],
["Peťo", 13, 11, 348103197358817281],
["Dado", 24, 4, 182907466898604033],
["Paťo", 15, 5, 229603278055276545],
["Erik", 31, 10, 328208304696197121],
["Viktor", 18, 8, 441235295418187777],
["Marek", 30, 8, 507612654928527361],
["Marko", 18, 4, 530846321544921108],
["Nina", 25, 8, 186839447180935168]]



@client.event
async def on_ready():
	print('FUNGUJEM!')
	loop()

async def task():
	global narodeniny
	guild = client.get_guild(743397937123557426)
	channel = client.get_channel(743397937555701831)
	sk_time = datetime.now(pytz.timezone("Europe/Bratislava"))
	today = sk_time.date()
	today = str(today).split("-") # 0-yyyy 1-mm 2-dd

	if(narodeniny!=None):
		try:
			member = await guild.fetch_member(arr[narodeniny][3])
			meno = member.display_name.replace("🎂", "")
			await member.edit(nick=meno)
		except:
			pass
		narodeniny = None

	for i in range(len(arr)):
		day = ("%02d" % arr[i][1])
		month = ("%02d" % arr[i][2])
		if str(month) == str(today[1]) and str(day) == str(today[2]):
			try:
				await channel.send("Dnes má narodeniny "+str(arr[i][0])+" :tada:\nVšetko najlepšie "+ '<@'+str(arr[i][3])+'>! :tada:')
				narodeniny = i
				member = await guild.fetch_member(arr[narodeniny][3])
				meno = member.display_name
				await member.edit(nick=meno+"🎂")
			except:
				pass

def loop():
	scheduler = AsyncIOScheduler(timezone="Europe/Bratislava")
	scheduler.add_job(task, 'cron', hour='00', minute='15')
	scheduler.start()


client.run(token)
