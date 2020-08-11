#!/usr/bin/env python3
# -*- coding: latin-1 -*-

from bot import Bot

def CreateBot(PostalCode, Years, Username):
    bot = Bot(PostalCode, Years, Username)
    bot.Start()

if __name__ == "__main__":
    CreateBot("35000", 18, "MissJulie")
