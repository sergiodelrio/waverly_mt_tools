
CORPORA_ARR=(aladdin drop_the_ball great_salespeople in_the_dark lazy_gift mulan pizza serial carve_in_stone give_an_inch hanif lazy_aldi lazy_reads netflix rocket_science uber)

for CORPUS in ${CORPORA_ARR[@]}
do

	cp ../corpora_preprocessed/"$CORPUS"/en-es/"$CORPUS"_edited_split.en \
		../corpora_preprocessed/"$CORPUS"/en-es/"$CORPUS"_edited_split.en-es.en

	cp ../corpora_preprocessed/"$CORPUS"/en-es/"$CORPUS"_edited_split.es \
		../corpora_preprocessed/"$CORPUS"/en-es/"$CORPUS"_edited_split.en-es.es

done



