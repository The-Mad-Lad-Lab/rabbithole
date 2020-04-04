import discord
import asyncio

client = discord.Client()
entrants = []

botmessage = 'U an admin bruh'
botmessageid = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.content.startswith('$check'):
		for role in message.author.roles:
			if role.name == 'admin':
				await message.channel.send(botmessage)
				break
		else:
			await message.channel.send('not admin')

@client.event
async def on_message(message):
	if message.content.startswith(botmessage):
		global botmessageid
		print(message.id)
		botmessageid = message.id
		await message.add_reaction('🥰')

	if message.content.startswith('$bracket'):
		bracket = make_bracket(entrants)
		print(bracket)
		if len(bracket[0] > 1):
			for match in bracket:
				await message.channel.send(str(match[0])+' vs ' +str(match[1]))
		
@client.event
async def on_reaction_add(reaction, user):
	
	print(botmessageid)
	tempmessage = await reaction.message.channel.fetch_message(botmessageid)

	if tempmessage:
		users = await reaction.users().flatten()
		async for areaction in reaction.users():
			if (areaction.name + '#' + areaction.discriminator) == 'RuskiBot#6485':
				continue
			if (areaction.name + '#' + areaction.discriminator) not in entrants:
				entrants.append(areaction.name + '#' + areaction.discriminator)

def make_bracket(entrants):
	#each two entrants put into their own list
	pairs = []

	for i,k in zip(entrants[0::2], entrants[1::2]):
		pairs.append([i,k])

	if len(entrants) % 2 == 1:
		pairs.append([entrants[-1]])

	return pairs

#make_bracket([1,2,3,4,5,6,7,8,9])

client.run('NjkzMjgyNDQ2MjQxOTU1OTEz.Xn6zrg.8WNH98OgU9jvZrW8n5P6nESpBKQ')