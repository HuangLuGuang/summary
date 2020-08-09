# -*- coding: utf-8 -*-
# @createTime    : 2020/8/9 0:53
# @author  : Huanglg
# @fileName: await_demo.py
# @email: luguang.huang@mabotech.com
import asyncio
import time

async def others():
    print('start1 coroutine')
    res = await asyncio.sleep(2)
    print('end1 coroutine')
    return time.time()

async def func():
    print('start call coroutine')
    resp = await others()
    print("IO stop", resp)
    resp2 = await others()
    print("IO stop", resp2)

if __name__ == '__main__':
    asyncio.run(func())
