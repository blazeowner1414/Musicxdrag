import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# REQUIRED VALUES

API_ID = 33462523
API_HASH = "bd72f77058b3707f23ade6049517259b"
BOT_USERNAME = "@BLAZE_M_USICBOT"
BOT_TOKEN = "7987969240:AAGgN7LnogXpoDFb-pHb7Fy86JjcbNW77Ho"

SESSION_STRING = "AQH-mPsAjrdj-LbelCKqFSgjZNMtMjzlVSCS2-ipFNiiTyD8Smc3Uulr8L5jQwulNP8bCT02PhiwaMLyR_TMfrNQWDQGmFwllnTmYlqsEfciDdZjzlg9FAMp33wHZrlFRMIzhklCKb9veOTf4VOnTr5VZmHXJHL7cE3MdZoLvTOVbg396SDyfx_wOnoBIyNLaZXTBp1yU0gJdGS1R06Fv6CeGWVCYcP4zndzMJTNxhwp0NmmtFG0TI_OTiWskytYJAkQbNm2o6BGcS49invIHTa534r_ovoCgKUVhUbNmLDOzezKq9WlwPQfLxOduMa3Iykq51oxTcPfMIg3CifDuFBK7GH1XwAAAAHxPUcYAA"
ASS_SESSION = "AQH-mPsAjrdj-LbelCKqFSgjZNMtMjzlVSCS2-ipFNiiTyD8Smc3Uulr8L5jQwulNP8bCT02PhiwaMLyR_TMfrNQWDQGmFwllnTmYlqsEfciDdZjzlg9FAMp33wHZrlFRMIzhklCKb9veOTf4VOnTr5VZmHXJHL7cE3MdZoLvTOVbg396SDyfx_wOnoBIyNLaZXTBp1yU0gJdGS1R06Fv6CeGWVCYcP4zndzMJTNxhwp0NmmtFG0TI_OTiWskytYJAkQbNm2o6BGcS49invIHTa534r_ovoCgKUVhUbNmLDOzezKq9WlwPQfLxOduMa3Iykq51oxTcPfMIg3CifDuFBK7GH1XwAAAAHxPUcYAA"

LOGGER_ID    = -1003443144562
LOG_GROUP_ID = -1003443144562
OWNER_ID = 8258688313
SUDO_USERS = [8258688313]

ASS_USERNAME = "FLASH_RGB"
ASS_ID = 8258688313

# OPTIONAL VALUES

MONGO_DB_URI = "mongodb+srv://BLAZE-MUSIC:Poipoi12@cluster0.s9qsrem.mongodb.net/AnonXMusic?retryWrites=true&w=majority"
DURATION_LIMIT_MIN = 200
SERVER_PLAYLIST_LIMIT = 300

API_URL = "https://api.thequickearn.xyz"
API_KEY = None

HEROKU_APP_NAME = None
HEROKU_API_KEY = None

UPSTREAM_REPO = "https://github.com/taslim19/musicxdrag"
UPSTREAM_BRANCH = "main"
GIT_TOKEN = None

SUPPORT_CHANNEL = "https://t.me/BLAZE_ERA"
SUPPORT_CHAT = "https://t.me/BLAZE_FIGHTERS"

AUTO_LEAVING_ASSISTANT = False

SPOTIFY_CLIENT_ID = "48037b43459c4bacbce6c61be2575ade"
SPOTIFY_CLIENT_SECRET = "103c89540301422aa880a462ca556416"

PLAYLIST_FETCH_LIMIT = 300
TG_AUDIO_FILESIZE_LIMIT = 1610612736
TG_VIDEO_FILESIZE_LIMIT = 1610612736

STRING1 = "AQH-mPsAjrdj-LbelCKqFSgjZNMtMjzlVSCS2-ipFNiiTyD8Smc3Uulr8L5jQwulNP8bCT02PhiwaMLyR_TMfrNQWDQGmFwllnTmYlqsEfciDdZjzlg9FAMp33wHZrlFRMIzhklCKb9veOTf4VOnTr5VZmHXJHL7cE3MdZoLvTOVbg396SDyfx_wOnoBIyNLaZXTBp1yU0gJdGS1R06Fv6CeGWVCYcP4zndzMJTNxhwp0NmmtFG0TI_OTiWskytYJAkQbNm2o6BGcS49invIHTa534r_ovoCgKUVhUbNmLDOzezKq9WlwPQfLxOduMa3Iykq51oxTcPfMIg3CifDuFBK7GH1XwAAAAHxPUcYAA"
STRING2 = None
STRING3 = None
STRING4 = None
STRING5 = None

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = "https://files.catbox.moe/8rwzc8.jpeg"
PING_IMG_URL = "https://files.catbox.moe/uopqdn.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:0"))
START_IMG_URL = "https://files.catbox.moe/8rwzc8.jpeg"
PING_IMG_URL = "https://files.catbox.moe/uopqdn.jpg"
PLAYLIST_IMG_URL = "https://telegra.ph/file/8d7b534e34e13316a7dd2.jpg"
STATS_IMG_URL = "https://files.catbox.moe/nge71y.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"
YTDLP_COOKIES = "/home/codespace/.config/yt-dlp/cookies.txt"
