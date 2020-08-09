# -*- coding: utf-8 -*-
# @createTime    : 2020/8/9 1:11
# @author  : Huanglg
# @fileName: tasks_demp.py
# @email: luguang.huang@mabotech.com
import asyncio
import time

async def func():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return time.ctime()

async def main():
    print('main start')

    task1 = asyncio.create_task(func())

    tast2 = asyncio.create_task(func())

    print('main stop')

    ret1 = await task1
    ret2 = await tast2
    print(ret1, ret2)

if __name__ == '__main__':
    asyncio.run(main())
