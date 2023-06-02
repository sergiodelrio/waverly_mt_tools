#!/usr/bin/env python
# coding: utf-8
import requests
import uuid
import json
import sys
import os

source_file = sys.argv[1]
target_file = sys.argv[2]
language_pair = sys.argv[3]

lp = language_pair.split("-")
source_language_code = lp[0]
target_language_code = lp[1]
key = os.getenv("MSFT_API_KEY")
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "eastus"
path = '/translate'
constructed_url = endpoint + path

params = {
           'api-version': '3.0',
           'from': source_language_code,
           'to': [target_language_code]
         }

headers = {
            'Ocp-Apim-Subscription-Key': key,
            # location required if you're using a multi-service or regional (not global) resource.
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
          }

def translate_msft(text, constructed_url, params, headers, sleep_base, sleep_exponent):

    try:
        body = [{"text": line}]
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        translated_text = response[0]["translations"][0]["text"]

        return translated_text

    except Exception as oops:
        print("\n{}.  Retrying in {} seconds…".format(oops, str(sleep_base**sleep_exponent)))
        time.sleep(sleep_base**sleep_exponent)
        sleep_exponent += 1
        return translate_msft(text, constructed_url, params, headers, sleep_base, sleep_exponent)


with open(source_file, "r", encoding="utf-8") as fo, open(target_file, "w", encoding="utf-8") as fw:

    lines = fo.readlines()
    lines = [line.strip() for line in lines]
    fo.close()

    line_counter = 0
    for line in lines:
        line_counter += 1
        sys.stdout.write('%s\r' % line_counter)

        translated_text = translate_msft(text=line, constructed_url=constructed_url, params=params, headers=headers, sleep_base=2, sleep_exponent=1)

        fw.write(translated_text + "\n")
        
