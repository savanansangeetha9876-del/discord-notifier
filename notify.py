import requests
import os
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

message = {
    "embeds": [
        {
            "title": "📢 Liquidity Reset Update",
            "description": (
                "Clean up previous liquidity zones and refresh your ILQ, TLQ, EPA markings "
                "on the **1H** and **4H** charts.\n\n"
                "➡️ New levels = New opportunities.\n"
                "➡️ Trade with clarity."
            ),
            "color": 5814783
        }
    ],
    "username": "Market Notifier"
}

requests.post(WEBHOOK_URL, json=message)
