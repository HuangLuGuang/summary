# -*- coding: utf-8 -*-
# @createTime    : 2020/8/9 0:43
# @author  : Huanglg
# @fileName: basic.py
# @email: luguang.huang@mabotech.com
import asyncio

async def func():
    print('call coroutine')


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(func())
# asyncio.run(func())
