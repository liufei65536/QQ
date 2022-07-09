from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
BZ = on_command('help',aliases={'帮助'},priority=5)
@BZ.handle()
async def bz (bot:Bot,event:GroupMessageEvent):
    await BZ.send('1. /官网 \n2. /入库 \n3. /签到 \n4. /点歌\n5. /抽签\n6. /解签 \n7. /积分查询')