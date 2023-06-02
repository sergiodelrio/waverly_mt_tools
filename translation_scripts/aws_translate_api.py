#!/usr/bin/env python
# coding: utf-8
import sys
from os import environ
import boto3

source_file = sys.argv[1]
target_file = sys.argv[2]
language_pair = sys.argv[3]

lp = language_pair.split("-")
source_language_code = lp[0]
target_language_code = lp[1]

with open(source_file, "r", encoding="utf-8") as fo, open(target_file, "w", encoding="utf-8") as fw:

    lines = fo.readlines()
    lines = [line.strip() for line in lines]

    translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

    line_counter = 0
    for line in lines:
        line_counter += 1
        sys.stdout.write('%s\r' % line_counter)

        result = translate.translate_text(Text = line, \
            SourceLanguageCode = source_language_code, \
            TargetLanguageCode = target_language_code)

        TranslatedText = result.get("TranslatedText")

        fw.write(TranslatedText + "\n")



