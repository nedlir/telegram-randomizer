import json
import random

from string import ascii_lowercase

import requests

from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateUsernameRequest, UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest


### API and Scraping URLs ###
FAKE_DATA_URL = r'https://randomuser.me/api/?format=json'
KANYE_QUOTE_URL = r'https://api.kanye.rest/'
BREAKINGBAD_QUOTE_URL = r'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
GENERAL_QUOTE_URL = r'https://favqs.com/api/qotd'
FAKE_IMAGE_URL = r'https://thispersondoesnotexist.com/image'


def get_data():
    print('Fetching random user data...')
    try:
        with requests.get(FAKE_DATA_URL) as response:
            source = response.json()
            fake_data = source.get('results')[0]
            print('Successfully fetched random user data!')
            return fake_data
    except:
        print('Error! Failed fetching fake user data.')


def get_first_name(data):
    first_name = data.get('name').get('first')
    min_len = 3
    if len(first_name) < min_len \
            or not first_name.isalnum() \
            or not first_name:
        new_data = get_data()
        first_name = get_first_name(new_data)
    return first_name


def get_last_name(data):
    last_name = data.get('name').get('last')
    min_len = 3
    if len(last_name) < min_len \
            or not last_name.isalnum() \
            or not last_name:
        new_data = get_data()
        last_name = get_last_name(new_data)
    return last_name


def get_username(data):
    username = random.choice(ascii_lowercase)
    username = username + data.get('login').get('username')
    username = username + str(random.randint(0, 9999))
    min_len = 5      # Telegram username limit length
    if len(username) < min_len \
            or not username.isalnum() \
            or not username:
        new_data = get_data()
        username = get_username(new_data)
    return username


def get_age(data):
    age = data.get('dob').get('age')
    return age


def get_location(data):
    city = data.get('location').get('city')
    country = data.get('location').get('country')
    return f'{city}, {country}'


def get_details(data):
    age = get_age(data)
    location = get_location(data)
    quote = get_kanye_quote()
    details = f'{age}, from {location}.'
    return details


def get_kanye_quote():
    try:
        with requests.get(KANYE_QUOTE_URL) as response:
            source = response.json()
            quote = source.get('quote')
            return quote
    except:
        print('Error! Failed to fetch Kanye quote.')


def get_breaking_bad_quote():
    try:
        with requests.get(BREAKINGBAD_QUOTE_URL) as response:
            source = response.json()
            quote = source[0].get('quote')
            return quote
    except:
        print('Error! Failed to fetch Breaking Bad quote.')


def get_general_quote():
    try:
        with requests.get(GENERAL_QUOTE_URL) as response:
            source = response.json()
            quote = source.get('quote').get('body')
            return quote
    except:
        print('Error! Failed to fetch General quote.')


def get_quote():
    quote_list = [get_breaking_bad_quote, get_kanye_quote, get_general_quote]
    quote = random.choice(quote_list)()
    return quote


def get_description(data):
    # Randomizes between fake quote or fake details
    if random.randint(1, 2) == 1:
        description = get_quote()
    else:
        description = get_details(data)
    max_len = 70     # Telegram description limit length
    if len(description) > max_len or not description:
        description = get_description(data)

    return description


def get_photo():
    print('Fetching AI generated human photo...')
    try:
        with requests.get(FAKE_IMAGE_URL) as response:
            try:
                with open('profile.jpg', 'wb') as f:
                    f.write(response.content)
                    print('Successfully saved AI photo on local folder!')
            except:
                print('Error! Failed to save profile picture.')
    except:
        print('Error! Failed to retrieve profile picture from url.')


def set_username(data, client):
    print('Setting new username...')
    try:
        user = client(UpdateUsernameRequest(
            username=get_username(data)
        ))
        print('Successfully changed username!')
    except:
        print('Error! Failed to change username.')


def set_profile(data, client):
    print('Setting new profile data...')
    try:
        profile = client(UpdateProfileRequest(
            first_name=get_first_name(data),
            last_name=get_last_name(data),
            about=get_description(data)
        ))
        print('Successfully updated profile data!')
    except:
        print('Error! Failed to change profile data.')


def set_photo(client):
    print('Uploading new profile photo...')
    try:
        photo = client(UploadProfilePhotoRequest(
            file=client.upload_file(
                'profile.jpg')
        ))
        print('Successfully uploaded photo!')
    except:
        print('Error! Failed to changed photo!')


def change_data(api_id, api_hash):
    data = get_data()
    get_photo()
    try:
        print('Establishing connection...')
        with TelegramClient('', api_id, api_hash) as client:
            set_username(data, client)
            set_profile(data, client)
            set_photo(client)
        print('Profile randomizing is finished! (:')
    except:
        print('Error! Failed to connect to Telegram.')
