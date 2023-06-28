# en-es

SL=en
TL=es
CORPUS=$1


# does not include "great_salespeople", … , as they are already split up by phrase
#CORPORA_ARR=(give_an_inch lazy_aldi lazy_reads rocket_science)

#for CORPUS in ${CORPORA_ARR[@]}
#do
#
#	mkdir -p ../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"
#
#	# Process source-language file
#	python sentence_tokenize.py \
#		../corpora/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$SL" \
#		../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$SL" \
#		"$SL"
#
#	# Process target-language file
#	python sentence_tokenize.py \
#		../corpora/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$TL" \
#		../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$TL" \
#		"$TL"
#done


python sentence_tokenize.py \
	../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"_edited."$SL" \
	../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"_edited_split."$SL" \
	"$SL"

python sentence_tokenize.py \
	../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"_edited."$TL" \
	../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"_edited_split."$TL" \
	"$TL"


#PRESPLIT_CORPORA_ARR=(great_salespeople)
#
#for CORPUS in ${PRESPLIT_CORPORA_ARR[@]}
#do
#
#	mkdir -p ../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"
#
#	cp ../corpora/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$SL" \
#		../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$SL"
#
#	cp ../corpora/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$TL" \
#		../corpora_preprocessed/"$CORPUS"/"$SL"-"$TL"/"$CORPUS"."$SL"
#
#done





