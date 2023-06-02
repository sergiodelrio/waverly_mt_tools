import sys

in_file = sys.argv[1]
out_file = sys.argv[2]

fo = open(in_file, "r", encoding="utf-8")
fw = open(out_file, "w", encoding="utf-8")

with open(in_file, "r", encoding="utf-8") as fo, open(out_file, "w", encoding="utf-8") as fw:

    lines = fo.readlines()

    for line in lines:
      line = line.replace("&#39;", "'")
      line = line.replace("&quot;", '"')
      fw.write(line)

