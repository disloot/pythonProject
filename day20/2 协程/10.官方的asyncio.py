# 作者: 王道 龙哥
# 2022年03月08日16时46分05秒
import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


asyncio.run(main())

