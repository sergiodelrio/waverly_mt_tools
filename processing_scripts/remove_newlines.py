import sys

in_file = sys.argv[1]
out_file = sys.argv[2]


def remove_double_newlines(text):

    text = text.replace("\n\n", "\n")
    return text



with open(in_file, "r", encoding="utf-8") as fo, open(out_file, "w", encoding="utf-8") as fw:

    in_doc = fo.read()

    # Do thrice to remove breaks of greater than two newlines (up to four)
    doc_with_replacements = remove_double_newlines(in_doc)
    doc_with_replacements = remove_double_newlines(doc_with_replacements)
    doc_with_replacements = remove_double_newlines(doc_with_replacements)

    fw.write(doc_with_replacements)



