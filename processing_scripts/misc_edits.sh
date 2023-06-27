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
	python misc_edits.py \
		../corpora/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$SL"-"$TL"."$SL" \
		../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$SL"-"$TL"."$SL"

	# Process target-language file
	python misc_edits.py \
		../corpora/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$SL"-"$TL"."$TL" \
		../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$SL"-"$TL"."$TL"

done


