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

    task_list = [
        # asyncio.create_task(func()),
        # asyncio.create_task(func())
        func(),
        func()
    ]
    done, pending = await asyncio.wait(task_list)
    for res in done:
        print(res.result())

if __name__ == '__main__':
    asyncio.run(main())
