import asyncio
from accounts.agents import acc_producer


def main():
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(acc_producer())
