import gc

from utils.client import BotPool

gc.collect()

pool = BotPool()

pool.setup()
