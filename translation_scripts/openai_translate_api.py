import os
import openai
import sys
import time

openai.api_key = os.getenv("OPENAI_API_KEY")

source_file = sys.argv[1]
target_file = sys.argv[2]
language_pair = sys.argv[3]
#model = sys.argv[4]

model = "gpt-3"

lp = language_pair.split("-")
source_language = lp[0]
target_language = lp[1]


def translate_gpt3(tl, text, sleep_base, sleep_exponent):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Translate this into 1. {}:\n\n{}\n\n1.".format(tl, text),
            temperature=0.3,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

        return response

    except Exception as oops:
        print("\n{}.  Retrying in {} seconds…".format(oops, str(sleep_base**sleep_exponent)))
        time.sleep(sleep_base**sleep_exponent)
        sleep_exponent += 1
        return translate_gpt3(tl, text, sleep_base=2, sleep_exponent=1)


def translate_gpt4(text, prompt, sleep_base, sleep_exponent):
    try:
        response = openai.ChatCompletion.create(
	model="gpt-4",
	temperature=0.3,
	max_tokens=4000,
	top_p=1,
	frequency_penalty=0,
	presence_penalty=0,
	messages=[
	    {"role": "system",
	     "content": prompt
	     },
	    {"role": "user",
	     "content": text
	     }
	]
	)
        return response

    except Exception as oops:
        print("\n{}.  Retrying in {} seconds…".format(oops, str(sleep_base**sleep_exponent)))
        time.sleep(sleep_base**sleep_exponent)
        sleep_exponent += 1
        return translate_gpt4(text, prompt, sleep_base, sleep_exponent)


with open(source_file, "r", encoding="utf-8") as fo, open(target_file, "w", encoding="utf-8") as fw:

    lines = fo.readlines()
    lines = [line.strip() for line in lines]
    fo.close()

    line_counter = 0
    for line in lines:
        line_counter += 1
        sys.stdout.write('%s\r' % line_counter)

        if model == "gpt-3":

            result = translate_gpt3(tl=target_language, text=line, sleep_base=2, sleep_exponent=1)
            translation = result["choices"][0]["text"]

        elif model == "gpt-4":

            prompt_baseline_03 = "Translate the following {} text into {}.".format(sl, tl)
            prompt_verbose_01 = "You are an expert translator and skilled in converting {} into {}. Translate the following {} text into {}.".format(sl, tl, sl, tl)

            if language_pair == "en-es":
                prompt = prompt_verbose_01
            elif language_pair == "es-en":
                prompt = prompt_baseline_03
            else:
                print("Invalid language pair.")
                exit()

            result = translate_gpt4(text=line, prompt=prompt, sleep_base=2, sleep_exponent=1)
            translation = result["choices"][0]["message"]["content"]

        else:
            print("Invalid model name.")
            exit()

        translation = translation.replace("\n", " ")
        translation = translation.replace("\r", " ")
        translation = translation.strip()

        fw.write(translation + "\n")




