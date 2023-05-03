from os import getenv
from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAOJNzzsXn4zeJHJsh-IcFkkTKrejVpzZpUK2KCkZL9bKUJMlbfoWXrRzV3XA_iIom-s618n6ff4D6MjvSGJiyfaRE8A-kfmpkQ6FmqCNGXeP_8teEkxBIgr479nNaYIx6QUegozETN2YLBKLndRpXHVIwwxEsOAxhpPXshCT-an79JyomtNFfO6bIZrLsO5pcF8JSRkE3dfr8NwcwcnEGWQC8NyN3GZEb-Z2V26mHOsJoSYLH_Z6xQudMLQX-BfOcSM0AKg-nT7-X3Es28v45aZv5ImkbeiSCTokua9i7v70JCRBTo5luZN4t4grlrVE3nOEycErbCjPEfv0IX5Pfzfk4hRgA")
BOT_TOKEN = getenv("BOT_TOKEN","6247378865:AAG1Fyol1pTsAm2WlShD8YatkbI_NoKoxLY")
CLONER_TOKEN = getenv("CLONER_TOKEN","6141153194:AAG6V50NtE3MdQzflA1xU4RoAwaH7PRBMmM")
BOT_NAME = getenv("BOT_NAME","MUSIC CLONER")
BOT_USERNAME = getenv("BOT_USERNAME","Teakadaimusicbot")
ASSID = int(getenv("ASSID","2119049542"))
ASSNAME = getenv("ASSNAME","assit")
ASSUSERNAME = getenv("ASSUSERNAME","PREMIUMMUSICPLAYER1")
BOT_ID = int(getenv("BOT_ID","5780461107"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/FUCKTHEATTITUDE/T")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH","clone")
HEROKU_API_KEY = getenv("HEROKU_API_KEY","")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","")
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Try:20092001@cluster0.486gohy.mongodb.net/?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID","29695856"))
API_HASH = getenv("API_HASH","f34cdc766c57e18d52e1509abe0c5054")
OWNER_ID = int(getenv("OWNER_ID","5927820595"))
UPDATE = getenv("UPDATE", "HowToCloneourbot")
SUPPORT = getenv("SUPPORT", "GroupsGuardSupport")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5927820595").split()))
START_PIC = getenv("START_PIC", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
OWNER_USERNAME = getenv("OWNER_USERNAME","alpha_romeo_06")
IMG_1 = "https://telegra.ph/file/3505f3c0abf6008b3f6b9.jpg"
