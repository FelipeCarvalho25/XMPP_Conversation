import logging
from getpass import getpass

from slixmpp import ClientXMPP


logger = logging.getLogger(__name__)


class SendMsgIot(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.recipient = None
        self.msg = None
        self.mensagem_chegou = None

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

    async def start(self, event):

        self.send_presence()
        await self.get_roster()

        
    def send_msg(self, recipient, message):
        self.recipient = recipient
        self.msg = message
        self.send_message(mto=self.recipient,
                          mbody=self.msg,
                          mtype='chat')


    def message(self, msg):
        print("[\] mensagem", msg["body"], " por ", msg["from"])
        if msg["type"] in ("chat", "normal"):
            self.mensagem_chego = msg["body"]

    def getMensage(self):
        return self.mensagem_chegou

