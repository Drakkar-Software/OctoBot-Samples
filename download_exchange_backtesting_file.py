#  Drakkar-Software OctoBot
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import asyncio
import logging

from octobot_commons.enums import TimeFrames
from tentacles import ExchangeHistoryDataCollector


async def run_exchange_history_collector(config, exchange_name, symbols, time_frames):
    collector = ExchangeHistoryDataCollector(config=config,
                                             exchange_name=exchange_name,
                                             tentacles_setup_config=None,
                                             symbols=symbols,
                                             time_frames=time_frames)
    await collector.initialize()
    await collector.start()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run_exchange_history_collector({}, "binance",
                                               ["BTC/USDT", "ETH/USDT", "LTC/USDT"],
                                               [TimeFrames.ONE_MINUTE, TimeFrames.FIVE_MINUTES, TimeFrames.ONE_HOUR]))
