# Don't Remove Credit @CRAZY_XYZ
# Subscribe YouTube Channel For Amazing Bot @CRAZY_XYZ
# Ask Doubt on telegram @CRAZY_XYZ


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20699247")

API_HASH = os.environ.get("API_HASH", "a1271e4ecc86745a62d222b62be8ba96")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6730798172:AAEHSbIc_PLUkF7pf4O3hDYsjhfVapGbUHU") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Nayak_Utkarsh") 

             # Don't Remove Credit @CRAZY_XYZ
             # Subscribe YouTube Channel For Amazing Bot @NAYAKKIPATHSHALA
             # Ask Doubt on telegram @CRAZY_XYZ

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://baga3621:lWQ9Qfk9pbck6aOd@cluster0.wdddbhn.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1543124151').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
