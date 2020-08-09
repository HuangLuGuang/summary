# -*- coding: utf-8 -*-
# @createTime    : 2020/8/9 21:36
# @author  : Huanglg
# @fileName: future_demo.py
# @email: luguang.huang@mabotech.com
import asyncio

async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result(100)

async def main():
    loop = asyncio.get_running_loop()

    # 创建一个future对象
    fut = loop.create_future()

    await loop.create_task(set_after(fut))
    data = await fut
    print(data)

if __name__ == '__main__':
    asyncio.run(main())
