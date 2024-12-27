import os
from notion_client import Client
from datetime import datetime

results = notion.databases.query(
    **{
        "database_id": database_id,
    }
).get("results")


for page in results:
    print(page)
