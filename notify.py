import requests

WEBHOOK_URL = "YOUR_WEBHOOK_URL"

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

requests.post('https://discord.com/api/webhooks/1445780019535413390/35TuJ8fY0jge3Ql92jGa9YAgWtukMTadxbEvUg2BX4d_tBaO4_-TL_wSeXDXdyydzfNZ', json=message)
