#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

import os
import discord
#from dotenv import load_dotenv
from random import randint 
from discord.ext import commands

#load_dotenv()
TOKEN = 'xxxxxxxxxxxxxxx'

client = discord.Client()

def write_id(path,x):  
    f = open(path, "w")
    f.write(str(x))    
    f.close            

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

@client.event
async def on_message(message):
    
    y = 0
    nbr = print_file("nbr.txt")
    nbr2 = print_file("ianbr.txt")
    coups = print_file("try.txt")
    coup = int(coups)
    high = print_file("highscore.txt")

    if message.author == client.user:
        return
            
    while True:
        msg = message.content
        msg = msg.split(" ")
        y = y + 1
        big_text = print_file("rules.txt")
        if message.content == 'rules!':
            await message.channel.send(big_text)
            break

        elif msg[0] == "guess" and msg[1].isnumeric() == True:
            if msg[1] < nbr:
                coup = coup + 1
                write_id("try.txt",str(coup))
                await message.channel.send("󠀠🥶🥶🥶")
            if msg[1] > nbr:
                coup = coup + 1
                write_id("try.txt",str(coup))
                await message.channel.send("󠀠🥵🥵🥵")
            if msg[1] == nbr:
                if coup < int(high):
                    print("test")
                    write_id("highscore.txt",coup)
                    high = print_file("highscore.txt")
                    await message.channel.send("󠀠New Highscore! 🥇")
                await message.channel.send("󠀠You win! 🏆")
                await message.channel.send("󠀠In " + str(coup) + " tries")
                await message.channel.send("󠀠Highscore: "+ str(high) + " tries")
                nbr = randint(0,100)
                write_id("nbr.txt",nbr)
                write_id("try.txt","1")
                break
            break
        elif msg[0] == "ia" and msg[1].isnumeric() == True:
            if msg[1] < nbr2:
                await message.channel.send("󠀠YOU 🥶🥶🥶")
                if int(nbr2) > int(msg[1]):
                    ianbr2 = randint(int(msg[1]) + 1 ,int(nbr2))    
                else:
                    ianbr2 = randint(int(nbr2) ,int(msg[1]) + 1)
                if int(ianbr2) < int(nbr2):
                    await message.channel.send("󠀠BOT " + str(ianbr2) + " 🥶🥶🥶")
                elif int(ianbr2) > int(nbr2):
                    await message.channel.send("󠀠BOT " + str(ianbr2) + " 🥵🥵🥵")
                else:
                    youwin = print_file("youwin.txt")
                    totalplay = print_file("stat.txt")
                    totalplay = int(totalplay) + 1
                    write_id("stat.txt",totalplay)
                    iawin = print_file("iawin.txt")
                    iawin = int(iawin) + 1
                    write_id("iawin.txt",iawin)
                    await message.channel.send("󠀠You lost! IA win🏆 The number was: " + str(nbr2))
                    await message.channel.send("󠀠`Statistics: `" + "\n" + "`Number of games played: `" + str(totalplay) + "\n" + "`The number of game you have win: `" + str(youwin) + "\n" + "`The number of game IA win: `" + str(iawin))
                    ianbr = randint(0,100)
                    write_id("ianbr.txt",ianbr)
                    break               
            if msg[1] > nbr2:
                await message.channel.send("󠀠YOU 🥵🥵🥵")
                if int(nbr2) > int(msg[1]):
                    ianbr2 = randint(int(msg[1]) - 1 ,int(nbr2))    
                else:
                    ianbr2 = randint(int(nbr2) ,int(msg[1]) - 1)
                if int(ianbr2) > int(nbr2):
                    await message.channel.send("󠀠BOT " + str(ianbr2) + " 🥵🥵🥵")
                elif int(ianbr2) < int(nbr2):
                    await message.channel.send("󠀠BOT " + str(ianbr2) + " 🥶🥶🥶")
                else:
                    iawin = print_file("iawin.txt")
                    youwin = print_file("youwin.txt")
                    totalplay = print_file("stat.txt")
                    totalplay = int(totalplay) + 1
                    write_id("stat.txt",totalplay)
                    iawin = print_file("iawin.txt")
                    iawin = int(iawin) + 1
                    write_id("iawin.txt",iawin)
                    await message.channel.send("󠀠You lost! IA win🏆 The number was: " + str(nbr2))
                    await message.channel.send("󠀠`Statistics: `" + "\n" + "`Number of games played: `" + str(totalplay) + "\n" + "`The number of game you have win: `" + str(youwin) + "\n" + "`The number of game IA win: `" + str(iawin))
                    ianbr = randint(0,100)
                    write_id("ianbr.txt",ianbr)
                    break
            if msg[1] == nbr2:
                iawin = print_file("iawin.txt")
                totalplay = print_file("stat.txt")
                totalplay = int(totalplay) + 1
                write_id("stat.txt",totalplay)
                youwin = print_file("youwin.txt")
                youwin = int(youwin) + 1
                write_id("youwin.txt",youwin)
                await message.channel.send("󠀠You win 🏆! IA lost")
                await message.channel.send("󠀠`Statistics: `" + "\n" + "`Number of games played: `" + str(totalplay) + "\n" + "`The number of game you have win: `" + str(youwin) + "\n" + "`The number of game IA win: `" + str(iawin))
                ianbr = randint(0,100)
                write_id("ianbr.txt",ianbr)
                break
        else:
            await message.channel.send("󠀠`WRONG ARGUMENT! type rules! to read the rules`")
            break 
        break

nbr = randint(0,100)
ianbr = randint(0,100)
write_id("nbr.txt",nbr)
write_id("ianbr.txt",ianbr)
write_id("try.txt","1")
client.run(TOKEN)
