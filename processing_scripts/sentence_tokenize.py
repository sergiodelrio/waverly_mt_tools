import sys
import nltk

in_file = sys.argv[1]
out_file = sys.argv[2]
sl = sys.argv[3]

if sl == "en":
    lang = "english"
elif sl == "es":
    lang = "spanish"
else:
    print("Invalid language code.  Exiting.")
    exit()


with open(in_file, "r", encoding="utf-8") as fo, open(out_file, "w", encoding="utf-8") as fw:

    in_text = fo.read()
    in_text = in_text.replace("\n\n", "\n")
    in_text = in_text.replace("\n\n", "\n")
    in_text = in_text.replace("\n\n", "\n")

    #in_lines = fo.readlines()

    in_lines = in_text.split("\n")

    lines_joined = " ".join([line.strip() for line in in_lines])
    lines_sentence_tokenized = nltk.sent_tokenize(lines_joined, language=lang)

    for line in lines_sentence_tokenized:
        fw.write("{}\n".format(line))
    
    




