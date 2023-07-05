import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6116735221:AAGAsurz-k1TR43xwk3CWbiQfu0gaRoWiLs")
API_ID = int(os.environ.get("API_ID", "23776178"))
API_HASH = os.environ.get("API_HASH", "b69598ab1d4021eb968d2db5b8bed30a")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001984763255"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1205219610").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://ego:Egobeyler99@cluster0.p00hwbq.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
