import os

class Settings:
    TABLE_NAME = os.getenv("TABLE_NAME", "pharmacy-table")
    AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "eu-west-2")
    LOW_STOCK_QUEUE_URL = os.getenv("LOW_STOCK_QUEUE_URL", "")
    EVENT_BUS_NAME = os.getenv("EVENT_BUS_NAME", "")

settings = Settings()