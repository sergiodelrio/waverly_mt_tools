# waverly_mt_tools

Created by Andrew Wilkinson (Sorenson)

This repo is to illustrate how I have found it useful to organize and run an MT research project.  Example scripts are provided to use the Amazon, DeepL, Google, and Microsoft translate APIs, as well as one for OpenAI that can be used to translate with GPT-3 (<tt>text-davinci-003</tt>) or GPT-4 with prewritten prompts that I have found to work.  (Just set the <tt>model</tt> variable to <tt>gpt-3</tt> or <tt>gpt-4</tt> in <tt>openai_translate_api.py</tt>.)

The example corpus used is the Workshop on Machine Translation Spanish-English test set from 2013, which is one of the standard test sets in the field of MT.  It is one which the Sacrebleu tool can download, which one can run with <tt>download_example_corpus.sh</tt>.

Example scripts are also provided to run scoring with Sacrebleu (to produce BLEU, TER, and chrF2++ scores) and with COMET's <tt>wmt22-comet-da</tt> model.

The scripts to run different vendor's APIs will, of course, require one to have an API key for each.  I have the scripts set up to get these from one's environment variables.


