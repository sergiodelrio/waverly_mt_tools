# en-es

SL=en
TL=es
CORPUS=serial
SRC_PATH="../corpora/$CORPUS/$SL-$TL/$CORPUS.$SL-$TL.$SL"

SYSTEM_ARR=(aws deepl gt msft openai)
#SYSTEM_ARR=(openai)

for SYS_NAME in ${SYSTEM_ARR[@]}
do
	echo -e "\nTranslating with $SYS_NAME\n"
	TRG_PATH="../mt_outputs/$CORPUS/$SL-$TL/$CORPUS.$SL-$TL.$SYS_NAME.$TL"
	python  "$SYS_NAME"_translate_api.py  $SRC_PATH  $TRG_PATH  $SL-$TL

done

