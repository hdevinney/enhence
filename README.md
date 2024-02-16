# enhence
Data augmentation for adding the pronoun 'hen' to Swedish corpora

`enhence` provides support code for adjusting Swedish text corpora (such as the [Stockholm-Umeå Corpus (SUC)](https://www.ling.su.se/english/nlp/corpora-and-resources/suc)) to include examples that use the third person singular gender-neutral pronoun _hen_. It was written primarily to produce updated corpora for use in training POS taggers for [efselab](https://github.com/robertostling/efselab).

## Description

A detailed description of the approach can be found in the following paper:

Henrik Björklund and Hannah Devinney (2023). [Computer, enhence: POS-tagging improvements for nonbinary pronoun use in Swedish.](https://sites.google.com/view/lt-edi-2023/proceedings) LT-EDI 2023 -- Third Workshop on Language Technology for Equality, Diversity, and Inclusions, 54--61.

## Usage: Augmenting a Corpus

To use this code, you will need to edit some paths to point towards the data you wish to modify. `enhence` uses a relatively simple rule-based approach, which will produce a few minor errors that you may wish to hand-correct. Support code (as well as suggested corrections for SUC) has been provided to aid with this.

1. `extract-pronoun-sentences-[tab|conll].py`
   - Two versions of extract-pronoun-sentences are provided, one for .tab files and one for .conll files. Use the appropriate version for your data.
   - Modify the `INPUT_DIR` value to reflect the appropriate path before running the code (line 11)

2. `produce-combined-corpus.py`
   - Set the value of HEN_SENTENCES_NO to the number of sentences including 'hen' you would like to augment your corpus with. Preset values reflect the experiments performed in the paper. 
   - Modify the `INPUT_DIR`, `henfilename`, and `outfilename` value to reflect the appropriate paths before running the code.

3. (optional) hand correction
   - We are aware of two main errors due the rules being "overapplied", resulting in "hen eller hen" and "hen och hen"-type sentences. Fortunately, there aren't many instances of these, so they can be hand-corrected.
     - "Hen eller hen" almost always needs adjusting, either by condensing a generic "hon eller han" into just "hen"; or by reverting one "hen" back to a binary-gendered pronoun.
     - "Hen och hen" only sometimes needs adjusting, by reverting one "hen" back to a binary-gendered pronoun for clarity. Most of the time, this does not produce incorrect or unclear sentences because the string "hen och hen" actually links two clauses.


## Usage: `efselab` Taggers

Generally speaking, the usual instructions for esfelab apply. You can create a new `build_*.py` file, or just edit the paths, and then build a tagger. To use this tagger in a pipeline, simply change the imports in `tagger.py` to point towards your new module.

If you wish to use an augmented version of SUC, we also suggest the following changes to supporting files:

* `saldo.txt`
  - add the following line:
  ```
hen    hen	      PN|UTR|SIN|DEF|SUB/OBJ	0
```
* `swe-brown100.txt`
  - add the following lines:
  ```
  hen    23
  hen	    73
  hens	    15
  ```
* `suc-blogs.tab`
  - either run `extract-pronoun-sentences` and `produce-combined-corpus` or
  - find/replace the 9 instances of han/hon with hen 



## Credits

This package is co-written with [Henrik Björklund](https://github.com/henrikb-umu).
