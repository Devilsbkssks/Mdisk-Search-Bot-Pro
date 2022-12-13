import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 15823382))
    API_HASH = os.getenv("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5918078029:AAFAuWGqmVOIIp2-VtLQNxD9De6vR9NUgm4")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BVtsOHwBuy4OZcxnH1MvykOPtJGpwWd1LzsAGPQDbT8ja1xJs9JDUDCbmGAJx_91dHHmNk0FpEMVTNIERQe8Sj_us6zBEz7y4jJAK7hsixmaDaMYD7q22uE9WjWdZkzUTi0AXPE4kMhF7zR6Y4Oon62MbFuiAsCJWRZjSQe7BxAwLAsbs9AEXW8B-8t21IltZSdeqUEZT4lFIBVQNcRznfrYF81uNsmFOWaoG3MDuarVkisdiGYUo_pAuc0-5ROXXhujEvoh-jdyW19zXgxopECqFnpITnawDayU2sKVXWhmBcnwIwlN39DlkypA3F0IFaChn_YchUd_hXi2MEXDZ1ldVBFvig4=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -1001631279048))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Mdisk_search_re_bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "5104293442"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "tlgbotsowner")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "-1001696028695")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", 'Just Search 👻')
    START_PHOTO = os.getenv("START_PHOTO", "False")
    HOME_TEXT = os.getenv("HOME_TEXT", 'False')
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001696028695")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://W9Uyj61afEXSw601:W9Uyj61afEXSw601@cluster0.zsxso.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001683642795"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "False")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "Mdiskbotsupport")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "XXgy4PoF35VECI7kZgTb")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", 'False')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", 'False')
