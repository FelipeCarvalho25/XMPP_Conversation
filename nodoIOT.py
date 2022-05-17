#adaptado de
# Slixmpp: The Slick XMPP Library
# Copyright (C) 2010  Nathanael C. Fritz
# This file is part of Slixmpp.
# See the file LICENSE for copying permission.


import asyncio, logging, json, os, sys, inspect;

from slixmpp import ClientXMPP

CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

logger = logging.getLogger(__name__)


class NodoBot(ClientXMPP):

    def __init__(self, jId, password):
        ClientXMPP.__init__(self, jId, password)

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

    async def start(self, event):
        print("[-] Sessão iniciada.")
        self.send_presence()
        await self.get_roster()
        

    def message(self, msg):
        print("[\] mensagem", msg["body"], " por ", msg["from"])
        if msg["type"] in ("chat", "normal"):
            msg.reply("Recebi: " + msg["body"]).send()


if __name__ == '__main__':

    formatter = "%(levelname)-8s %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=formatter)
    CONFIG = json.loads(open(CURRENTDIR + "/data/config.json").read())
    xmpp = NodoBot("testeiot2@jabber.de", "b4t4t1nh4123")
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0004') # Service Discovery
    xmpp.register_plugin('xep_0060') # Service Discovery
    xmpp.register_plugin('xep_0199') # XMPP Ping

    xmpp.connect()
    xmpp.process(forever=True)
