bash download_example_corpus.sh

cd translation_scripts
bash translate.sh

cd ../processing_scripts
bash postprocess.sh

cd ../scoring_scripts
bash score_with_sacrebleu.sh
bash score_with_comet.sh

cd ..

