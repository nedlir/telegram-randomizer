# :busts_in_silhouette: Telegram Randomizer  :busts_in_silhouette:

**Telegram Randomizer is a simple script designed to update telegram account with randomized profile data, random telegram username and unique AI generated human photo as a profile picture.**

## Example :game_die:

![Image](example.gif)

## How does it work? :eyes:

The script generates the following fake data: first and last name, age, location and account username using [randomuser](https://randomuser.me/).

User description is randomly picked between a general user description, i.e. *"23. from Hamburg, Germany"* and an inspirational quote from random modern day philosophers such as Kanye West, Breaking Bad characters or classic inspirational quotes using [Kanye quotes API](https://api.kanye.rest/), [Breaking Bad quotes API](https://breaking-bad-quotes.herokuapp.com) and [favqs API](https://favqs.com/).

Finally, a unique AI automated user photo is generated and scraped from the site [this person doesn't exist](https://thispersondoesnotexist.com) and uploaded to the user profile.

In case you would like to distinct the gender of the AI photo, a usage of [generated API](https://generated.photos/) is also supported. Kindly note that free use is limited to 50 monthly calls.

Randomizing the profile is as easy as typing the following in your script:
            
    from randomizer import change_data


    change_data(API_ID, API_HASH, False)
            

For a full example please refer to [example.py](example.py).

## Requirements :key:

The script was written with as little as necessary dependecies in mind.

To install the required packages, pip install the [requirements.txt](requirements.txt) file.

APIs used in the script do not require registration except for the [telegram api](https://core.telegram.org/api/obtaining_api_id/) and the [generated API](https://generated.photos/) (not a requisite).


## License 

[MIT](LICENSE.md)
