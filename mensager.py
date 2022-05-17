#adaptado de

# Slixmpp: The Slick XMPP Library
# Copyright (C) 2010  Nathanael C. Fritz
# This file is part of Slixmpp.
# See the file LICENSE for copying permission


import asyncio, logging, json, os, sys, inspect

from slixmpp import ClientXMPP


logger = logging.getLogger(__name__)
CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


class SendMsgBot(ClientXMPP):

    def __init__(self, jid, password, recipient, message):
        ClientXMPP.__init__(self, jid, password)

        self.recipient = recipient
        self.msg = message

        self.add_event_handler("session_start", self.start)

    async def start(self, event):

        self.send_presence()
        await self.get_roster()

        self.send_message(mto=self.recipient,
                          mbody=self.msg,
                          mtype='chat')

        self.disconnect()


if __name__ == '__main__':
    CONFIG = json.loads(open(CURRENTDIR + "/data/config2.json").read())
    jid = CONFIG["username"]
    password = CONFIG["password"]
    to = input("Send To: ")
    message = input("Message: ")
    # Setup the EchoBot and register plugins. Note that while plugins may
    # have interdependencies, the order in which you register them does
    # not matter.
    xmpp = SendMsgBot(jid, password, to, message)
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0199') # XMPP Ping

    # Connect to the XMPP server and start processing XMPP stanzas.
    xmpp.connect()
    xmpp.process(forever=False)