import discord
import emoji
from googletrans import Translator

translator = Translator()

class MyClient(discord.Client):
    active = bool(1)

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        msgList = list(message.content)
        i = 0
        for x in msgList:
            if x in emoji.UNICODE_EMOJI:
                msgList[i]=' '
            i+=1
        msg = ''.join(msgList)
        lang = translator.detect(msg).lang
        #msg = message.content

        if msg == '.die': 
            await message.channel.send('ok')
            MyClient.active = False

        if (message.author != self.user) and (lang in ['nl', 'ru', 'sv']) and (MyClient.active == 1) and (msg[:6] != '.trans') and (len(msg)>4):
            """beg = 0
            while msg.find(':', beg) != -1:
                end = -1
                for x in msg[beg:]:
                    end += 1
                    if x == in [' ', emoji.UNICODE_EMOJI]:
                        break
                    if x == ':':
                        end += beg
                        print(msg[beg:end])
                        emoLang = str (translator.detect(msg[beg:end]).lang)
                        if emoLang not in ['nl', 'ru', 'sv']:
                            msg=msg.replace(msg[beg:end],'')
                        break
                beg = msg.find(':', beg)+1

            beg = 0
            while msg.find('<', beg) != -1:
                end = -1
                for x in msg[beg:]:
                    end += 1
                    if x == in [' ', emoji.UNICODE_EMOJI]:
                        break
                    if x == '>':
                        end += beg
                        print(msg[beg:end])
                        emoLang = str (translator.detect(msg[beg:end]).lang)
                        if emoLang not in ['nl', 'ru', 'sv']:
                            msg=msg.replace(msg[beg:end],'')
                        break
                beg=msg.find('<', beg)+1"""

            await message.channel.send('Human translation of ' + '{.author}'.format(message)[:-5] + '\'s message: \n> ' + translator.translate(msg).text)# + "\nConfidence: " + str(translator.detect(msg).confidence))

        if msg == '.help':
            await message.channel.send('no :smiley:')

        if msg == '.stop die':
            MyClient.active = True
            await message.channel.send('am live')

        if msg[:6] == '.trans':
            await message.channel.send('> ' + translator.translate(msg[6:]).text)
        


client = MyClient()
client.run('NjEyMDEzNTI0MjEzODI1NTYy.XVcfZA.4VFN4YMMfqqy1pvNCJUWUhWR3XA')