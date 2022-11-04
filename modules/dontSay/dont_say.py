from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()
channel.name("don't say")
channel.author("kimori")
channel.description(
    '''
    当在群组中收到”你好“时，发送：不要说你好，来点色图
    '''
)

def run():
    
    @channel.use(ListenerSchema(listening_events=[GroupMessage]))
    async def dontSay(app: Ariadne, group: Group, message: MessageChain):
        if message.display=="你好":
            await app.send_message(
                group,
                MessageChain(f"不要说{message.display}，来点色图"),
            )