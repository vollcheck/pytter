#!/usr/bin/python

import aiohttp
# import asyncio

GITTER_BASE_URL = 'https://api.gitter.im/v1/'
GITTER_STREAM_URL = 'https://stream.gitter.im/v1/'


async def stream():
    reader, writer = await asyncio.open_connection(GITTER_STREAM_URL)
    data = await reader.read()
    async for m in data:
        print(m)
