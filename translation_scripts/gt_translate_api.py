#!/usr/bin/env python
# coding: utf-8
import sys
from google.cloud import translate
import os

source_file = sys.argv[1]
target_file = sys.argv[2]
language_pair = sys.argv[3]

lp = language_pair.split("-")
source_language_code = lp[0]
target_language_code = lp[1]

project_id = os.getenv("PROJECT_ID")
assert project_id
parent = "projects/{}".format(project_id)

with open(source_file, "r", encoding="utf-8") as fo, open(target_file, "w", encoding="utf-8") as fw:

    lines = fo.readlines()
    lines = [line.strip() for line in lines]

    client = translate.TranslationServiceClient()

    line_counter = 0
    for line in lines:
        line_counter += 1
        sys.stdout.write('%s\r' % line_counter)

        response = client.translate_text(
            contents=[line],
            source_language_code=source_language_code,
            target_language_code=target_language_code,
            parent=parent,
        )

        for translation in response.translations:
            fw.write(translation.translated_text + "\n")





