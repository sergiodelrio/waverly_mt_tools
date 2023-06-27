import sys

in_file = sys.argv[1]
out_file = sys.argv[2]


def remove_speaker_tags_serial(text):

    # English
    text = text.replace("(man on tape)", "")
    text = text.replace("(man)", "")
    text = text.replace("(woman)", "")
    text = text.replace("(Saad)", "")
    text = text.replace("(Mr. S)", "")
    text = text.replace("(Mr S)", "")
    text = text.replace("(interviewer", "")
    text = text.replace("(Ritz)", "")
    text = text.replace("(MacGillivary)", "")
    text = text.replace("(Buddemeyer)", "")

    # Spanish
    text = text.replace("(hombre en grabación)", "")
    text = text.replace("(hombre(", "")
    text = text.replace("(hombre)", "")
    text = text.replace("(hobre)", "")
    text = text.replace("(Señor S)", "")
    text = text.replace("(señor S)", "")
    text = text.replace("(entrevistador)", "")
    text = text.replace("(mujer)", "")

    return text

def remove_speaker_tags_hanif(text):

    text = text.replace("Brené Brown: ", "")
    text = text.replace("Hanif: ", "")
    return text

def remove_speaker_tags_pizza(text):

    text = text.replace("Nick: ", "")
    text = text.replace("Jack: ", "")
    return text

def remove_double_double_quotes(text):

    text = text.replace('""', '"')
    return text

def change_spelling(text):

    text = text.replace("jinny", "jinni")
    return text

def remove_double_line_spacing(text):

    text = text.replace("\n\n", "\n")
    return text


with open(in_file, "r", encoding="utf-8") as fo, open(out_file, "w", encoding="utf-8") as fw:

    in_doc = fo.read()

    # Left double quotation mark → quotation mark
    #doc_with_replacements = in_doc.replace('“', '"')

    # Right double quotation mark → quotation mark
    #doc_with_replacements = doc_with_replacements.replace('”', '"')

    # Left single quotation mark → apostrophe 
    #doc_with_replacements = doc_with_replacements.replace("‘", "'")

    # Acute accent → apostrophe 
    #doc_with_replacements = doc_with_replacements.replace("´", "'")

    # Right single quotation mark → apostrophe
    #doc_with_replacements = doc_with_replacements.replace("’", "'")

    doc_with_replacements = remove_double_line_spacing(in_doc)

    if "serial" in in_file or "serial" in out_file:
        doc_with_replacements = remove_speaker_tags_serial(doc_with_replacements)

    if "hanif" in in_file or "hanif" in out_file:
        doc_with_replacements = remove_speaker_tags_hanif(doc_with_replacements)
        doc_with_replacements = remove_double_double_quotes(doc_with_replacements)

    if "aladdin" in in_file or "aladdin" in out_file:
        doc_with_replacements = change_spelling(doc_with_replacements)

    if "pizza" in in_file or "pizza" in out_file:
        doc_with_replacements = remove_speaker_tags_pizza(doc_with_replacements)


    fw.write(doc_with_replacements)



