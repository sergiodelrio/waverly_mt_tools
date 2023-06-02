# waverly_mt_tools

Created by Andrew Wilkinson (Sorenson)

### Overview

This repo is to illustrate how I have found it useful to organize and run an MT research project.  Example scripts are provided to use the Amazon, DeepL, Google, and Microsoft translate APIs, as well as one for OpenAI that can be used to translate with GPT-3 (<tt>text-davinci-003</tt>) or GPT-4 with prewritten prompts that I have found to work.  (Just set the <tt>model</tt> variable to <tt>gpt-3</tt> or <tt>gpt-4</tt> in <tt>openai_translate_api.py</tt>.)

This is <b>not</b> intended to be a prescription for how things must be done, but rather a suggestion, guide, reference, or resource.

I have already downloaded the example corpus and run translation, postprocessing, and scoring.  To run steps using a new/different corpus, one would edit the <tt>CORPUS</tt> and associated path variables in each of <tt>translation_scripts/translate.sh</tt>, <tt>processing_scripts/postprocess.sh</tt>, <tt>scoring_scripts/score_with_comet.sh</tt>, and <tt>scoring_scripts/score_with_sacrebleu.sh</tt> to reflect the new name.

### Get example corpus
The example corpus used is the Workshop on Machine Translation Spanish-English test set from 2013, which is one of the standard test sets in the field of MT.  It is one which the Sacrebleu tool can download, which one can run with <tt>download_example_corpus.sh</tt>.

### Postprocessing
Using these particular vendors' translation APIs, using the same source as input, does not necessitate much postprocessing in order for them to be in a consistent format.  They all are able to take in natural (untokenized) text and output natural text in return.  This is not <i>necessarily</i> the case for all MT systems out there.

The only issue I have caught is that Google Translate returns the HTML tag version of the apostrophe / single quote (<tt>&#39</tt>), and so I have provided a postprocessing script whose only current function is to replace the tag with the correct character.  If more issues are discovered, or if any system used in the pilot project needs more consistent postprocessing, this step can be expanded to take care of that.

### Translating
The scripts to run different vendors' APIs will, of course, require one to have an API key for each.  I have the scripts set up to get these from one's environment variables.

The scripts for OpenAI and Microsoft provide error handling, using exponential backoff (OpenAI in particular throws frequent HTTP errors, because it's in such high demand).  If this is needed for the other vendors' services, it should be straightforward to implement the same paradigm in the respective scripts.

### Scoring
The COMET scoring script is set up to use one's system's Nvidia GPUs, if present.  Set the <tt>CUDA_VISIBLE_DEVICES</tt> variable to reflect the IDs of available GPUs (which can be discovered by running <tt>$ nvidia-smi</tt>).  <i>E.g.</i>, <tt>CUDA_VISIBLE_DEVICES=0,1,2</tt>.  The <tt>--gpus</tt> flag in the <tt>comet-score</tt> command reflects the number of GPUs specified by <tt>CUDA_VISIBLE_DEVICES</tt> (not their IDs, but how many there are).  <i>E.g.</i>, <tt>--gpus 3</tt>.

To disable GPUs and run COMET with CPUs instead, specify <tt>--gpus 0</tt>.

COMET will output one score per candidate translation per line.  The aggregated scores are the last <i>n</i> lines of the document, where <i>n</i> is the number of candidates specified in the <tt>comet-score</tt> command in <tt>score_with_comet.sh</tt>.  BLEU is not calculated per line, but only in aggregate.






