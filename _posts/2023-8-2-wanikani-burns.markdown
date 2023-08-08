---
layout: post
title: "Use Wanikani API to List all Kanji by Date Burned"
summary: "In Python"
---


# Motivation

Once I've burned a kanji, I add it to my Anki writing deck.
The Wanikani website shows the Kanji burned 
(advanced to the last level at which point the cards are retired) 
in the last 30 days, 
but if you want to see further back in time, 
then it is necessary to do something custom with the API.

## Generating API Key

* Open the [API Tokens Screen on the Wanikani Website](https://www.wanikani.com/settings/personal_access_tokens) (User → Settings → API Tokens)
* Click *"Generate new Token"* then *"Generate Token"*

## The Script

[Download wani_burns.zip](/dl/wani_burns.zip) and extract. (Contains `wani_burns.py` script and `requirements.txt`)

## Running the Script

From a folder containing the `wani_burns.py` script and `requirements.txt`, run the following in the terminal:

Replace `<API_KEY>` with your wanikani API Key.

```shell
python3 -m venv env               # Create Virtual Environment
source env/bin/activate           # Activate Virtual Environment
pip install -r requirements.txt   # Install Dependencies

python wani_burns.py <API_KEY>    # Run the Script
```
