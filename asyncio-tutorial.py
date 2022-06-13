# From https://docs.python.org/3/library/asyncio.html

import asyncio
import logging


async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")


logging.basicConfig(level=logging.DEBUG)
asyncio.run(main(), debug=True)
