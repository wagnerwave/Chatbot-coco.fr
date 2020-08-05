#!/usr/bin/env python3

from bot import Bot

def CreateBot(PostalCode, Years, Username):
    bot = Bot(PostalCode, Years, Username)
    bot.Start()

if __name__ == "__main__":
    CreateBot("92000", 24, "SexyLapine92")
