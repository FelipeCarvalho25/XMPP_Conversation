import asyncio, logging, json, os, sys, inspect;

from slixmpp import ClientXMPP

CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

logger = logging.getLogger(__name__)

class NodoBot(ClientXMPP):
    def __int__(self, jId, password):
        ClientXMPP.__init__(self, jId, password)

        self.add_event_handler("session_start", self)
        self.add_event_handler("message"),

    def session_start(self):
        print("[-] Sessão iniciada.")
        self.send_presence()
        self.get_roster()
    def message(self, msg):
        print("[\] mensagem", msg["body"], " por ", msg["from"])
        if msg["type"] in ("chat", "normal"):
            msg.reply("Recebi: " + msg["body"]).send()

if __name__ == '__main___':
    formatter = "%(levelname)-8s %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=formatter)
    CONFIG = json.loads(open(CURRENTDIR+"/data/config.json").read())
    xmpp = NodoBot(CONFIG['username'],CONFIG['password'])
    xmpp.connect()
    xmpp.process()

