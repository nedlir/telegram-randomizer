import os

from dotenv import load_dotenv

import randomizer


load_dotenv()
API_HASH = os.getenv('TELEGRAM_API_HASH')
API_ID = os.getenv('TELEGRAM_API_ID')
WORKING_DIRECTORY = os.getenv('WORKING_DIRECTORY')

os.chdir(WORKING_DIRECTORY)

randomizer.change_data(API_ID, API_HASH, False)
