

CORPORA_ARR=(give_an_inch lazy_aldi lazy_reads rocket_science)
VENDORS_ARR=(aws deepl gt msft openai)


for CORPUS in ${CORPORA_ARR[@]}
do
	cat corpora/"$CORPUS"/en-es/"$CORPUS".en-es.en >> corpora/questionable/en-es/questionable.en-es.en
	cat corpora/"$CORPUS"/en-es/"$CORPUS".en-es.es >> corpora/questionable/en-es/questionable.en-es.es
done


for VENDOR in ${VENDORS_ARR[@]}
do
	for CORPUS in ${CORPORA_ARR[@]}
	do


		cat mt_outputs/"$CORPUS"/en-es/"$CORPUS".en-es."$VENDOR".es >> mt_outputs/questionable/en-es/questionable.en-es."$VENDOR".es

	done
done

