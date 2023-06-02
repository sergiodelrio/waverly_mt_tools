#!/usr/bin/env python
# coding: utf-8
import sys
import os
import deepl

auth_key = os.getenv("DEEPL_API_KEY")
translator = deepl.Translator(auth_key)

source_file = sys.argv[1]
target_file = sys.argv[2]
language_pair = sys.argv[3]

lp = language_pair.split("-")
source_language_code = lp[0]
target_language_code = lp[1]

if target_language_code == "en":
    target_language_code = "EN-US"

with open(source_file, "r", encoding="utf-8") as fo, open(target_file, "w", encoding="utf-8") as fw:

    lines = fo.readlines()
    lines = [line.strip() for line in lines]

    line_counter = 0
    for line in lines:
        line_counter += 1
        sys.stdout.write('%s\r' % line_counter)

        result = translator.translate_text(line, source_lang=source_language_code, target_lang=target_language_code)

        fw.write(result.text + "\n")


