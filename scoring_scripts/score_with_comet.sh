export CUDA_VISIBLE_DEVICES=0,1
MODEL="Unbabel/wmt22-comet-da"

# en-es

SL=en
TL=es
#CORPUS=serial
CORPUS=pizza

mkdir -p ../scoring_outputs/$CORPUS/$SL-$TL

#SRC_PATH="../corpora/$CORPUS/$SL-$TL/$CORPUS.$SL-$TL.$SL"
SRC_PATH="../corpora_preprocessed/$CORPUS/$SL-$TL/$CORPUS.$SL-$TL.$SL"
#REF_PATH="../corpora/$CORPUS/$SL-$TL/$CORPUS.$SL-$TL.$TL"
REF_PATH="../corpora_preprocessed/$CORPUS/$SL-$TL/$CORPUS.$SL-$TL.$TL"
TRG_PREFIX="../mt_postprocessed/$CORPUS/$SL-$TL"
OUT_PATH="../scoring_outputs/$CORPUS/$SL-$TL/comet-score.$CORPUS.$SL-$TL.txt"

echo "Writing scores to $OUT_PATH"
comet-score \
	-s $SRC_PATH \
	-r $REF_PATH \
	-t $TRG_PREFIX/$CORPUS.$SL-$TL.aws.$TL \
	   $TRG_PREFIX/$CORPUS.$SL-$TL.deepl.$TL \
	   $TRG_PREFIX/$CORPUS.$SL-$TL.gt.$TL \
	   $TRG_PREFIX/$CORPUS.$SL-$TL.msft.$TL \
	   --quiet --gpus 2 \
	   --model $MODEL \
	   > $OUT_PATH

	   #$TRG_PREFIX/$CORPUS.$SL-$TL.openai.$TL \
