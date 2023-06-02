# waverly_mt_tools

Created by Andrew Wilkinson (Sorenson)

### Overview

This repo is to illustrate how I have found it useful to organize and run an MT research project.  Example scripts are provided to use the Amazon, DeepL, Google, and Microsoft translate APIs, as well as one for OpenAI that can be used to translate with GPT-3 (<tt>text-davinci-003</tt>) or GPT-4 with prewritten prompts that I have found to work.  (Just set the <tt>model</tt> variable to <tt>gpt-3</tt> or <tt>gpt-4</tt> in <tt>translation_scripts/openai_translate_api.py</tt>.)

This is <b>not</b> intended to be a prescription for how things must be done, but rather a suggestion, guide, reference, or resource.

I have already downloaded the example corpus and run translation, postprocessing, and scoring <b>for the es-en direction</b>.  To run steps using a new/different corpus, or the same corpus from English to Spanish, one would edit the <tt>CORPUS</tt> and associated path variables in each of <tt>translation_scripts/translate.sh</tt>, <tt>processing_scripts/postprocess.sh</tt>, <tt>scoring_scripts/score_with_comet.sh</tt>, and <tt>scoring_scripts/score_with_sacrebleu.sh</tt> to reflect the new name.

### Organization and naming
The way I do things is to have, within the main directory of the repo, separate directories for translation scripts, processing scripts, and scoring scripts, as well as separate directories for the corpus, for translation outputs, for (pre- and) postprocessing outputs, and for scoring outputs.  The whole pipeline is run in <tt>run_all.sh</tt>, and reflects this procedure:

1. Get the base corpus—both the source and the reference(s) (for this example, by running <tt>download_example_corpus.sh</tt>); results are saved within the <tt>corpora</tt> directory structure;
2. Run preprocessing if necessary (not necessary for this example);
3. Get the source document from within the <tt>corpora</tt> directory (or the source document after preprocessing from within the <tt>corpora_preprocessed</tt> directory), and translate it with each MT system under consideration using <tt>translation_scripts/translate.sh</tt>; results are saved within the <tt>translation_outputs</tt> directory structure;
4. Get the translated documents from within the <tt>translation_outputs</tt> directory, and postprocess them as necessary using <tt>processing_scripts/postprocess.sh</tt>; results are saved within the <tt>mt_postprocessed</tt> directory structure;
5. Get the postprocessed documents from within the <tt>mt_postprocessed</tt> directory, and score them with each of <tt>scoring_scripts/score_with_comet.sh</tt> and <tt>scoring_scripts/score_with_sacrebleu.sh</tt>; results are saved within the <tt>scoring_outputs</tt> directory structure.

The <tt>corpora</tt>, <tt>translation_outputs</tt>, and <tt>mt_postprocessed</tt> directories contain the same substructure within them, which is <tt>…/name_of_corpus/language_direction/</tt>.  In this case, that's <tt>…/wmt13/es-en/</tt>.  The language direction is the two-letter ISO 639-1 code for the source language, followed by a hyphen, then the target language.  The text files themselves are named as <tt>name_of_corpus.language_direction.language</tt>, where <tt>language</tt> is the language present in that individual document.

This convention is somewhat redundant, and necessitates the creation of some nested directories.  In my experience, this significantly reduces confusion and ambiguity down the road.

Note what the following filepaths mean, in context:

&nbsp;&nbsp;&nbsp;&nbsp;<tt>corpora/wmt13/es-en/wmt13.es-en.es</tt>: source file for es-en direction

&nbsp;&nbsp;&nbsp;&nbsp;<tt>corpora/wmt13/es-en/wmt13.es-en.en</tt>: target file for es-en direction

&nbsp;&nbsp;&nbsp;&nbsp;<tt>corpora/wmt13/en-es/wmt13.en-es.en</tt>: source file for en-es direction

&nbsp;&nbsp;&nbsp;&nbsp;<tt>corpora/wmt13/en-es/wmt13.en-es.es</tt>: target file for en-es direction

&nbsp;&nbsp;&nbsp;&nbsp;<tt>translation_outputs/wmt13/es-en/wmt13.es-en.aws.en</tt>: results of translating the source file for es-en direction from Spanish to English using Amazon Translate

&nbsp;&nbsp;&nbsp;&nbsp;<tt>translation_outputs/wmt13/en-es/wmt13.en-es.aws.es</tt>: results of translating the source file for en-es direction from English to Spanish using Amazon Translate

### Get example corpus
The example corpus used is the Workshop on Machine Translation Spanish-English test set from 2013, which is one of the standard test sets in the field of MT.  It is one which the Sacrebleu tool can download, which one can run with <tt>download_example_corpus.sh</tt>.

### Postprocessing
Using these particular vendors' translation APIs, using the same source document as input, does not necessitate any preprocessing, or much postprocessing, in order for the outputs to all be in a consistent format with each other.  These systems all are able to take in natural (untokenized) text and output natural text in return.  This is <i>not necessarily the case</i> for all MT systems out there.  It is important to visually check all MT outputs to see if there are any formatting problems that would lead to inaccurate MT evaluation scores if not corrected.

The only issue I have caught is that Google Translate returns the HTML tag version of the apostrophe / single quote (<tt>&#39</tt>), and so I have provided a postprocessing script (<tt>processing_scripts/postprocess.py</tt>) whose only current function is to replace the tag with the correct character.  If more issues are discovered, or if any system used in the pilot project needs more consistent postprocessing, this step can be expanded to take care of that.

### Translating
The scripts to run different vendors' APIs will, of course, require one to have an API key for each.  I have the scripts set up to get these from one's environment variables.

The scripts for OpenAI and Microsoft provide error handling, using exponential backoff (OpenAI in particular throws frequent HTTP errors, because it's in such high demand).  If this is needed for the other vendors' services, it should be straightforward to implement the same paradigm in the respective scripts.

### Scoring
The COMET scoring script is set up to use one's system's Nvidia GPUs, if present.  Set the <tt>CUDA_VISIBLE_DEVICES</tt> variable to reflect the IDs of available GPUs (which can be discovered by running <tt>$ nvidia-smi</tt>).  <i>E.g.</i>, <tt>CUDA_VISIBLE_DEVICES=0,1,2</tt>.  The <tt>--gpus</tt> flag in the <tt>comet-score</tt> command reflects the number of GPUs specified by <tt>CUDA_VISIBLE_DEVICES</tt> (not their IDs, but how many there are).  <i>E.g.</i>, <tt>--gpus 3</tt>.

To disable GPUs and run COMET with CPUs instead, specify <tt>--gpus 0</tt>.

COMET will output one score per candidate translation per line.  The aggregated scores are the last <i>n</i> lines of the document, where <i>n</i> is the number of candidates specified in the <tt>comet-score</tt> command in <tt>score_with_comet.sh</tt>.  BLEU is not calculated per line, but only in aggregate.

Note that COMET uses both the source and reference from the base corpus for scoring, while Sacrebleu uses only the reference.




