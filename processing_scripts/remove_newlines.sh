# en-es

SL=en
TL=es
CORPUS=$1

#CORPORA_ARR=(give_an_inch lazy_aldi great_salespeople lazy_reads rocket_science)

CORPORA_ARR=($CORPUS)

for CORPUS in ${CORPORA_ARR[@]}
do

	mkdir -p ../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"

	# Process source-language file
	python remove_newlines.py \
		../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"_edited."$SL" \
		../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"_edited_2."$SL"

	# Process target-language file
	python remove_newlines.py \
		../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"_edited."$TL" \
		../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"_edited_2."$TL"

done

