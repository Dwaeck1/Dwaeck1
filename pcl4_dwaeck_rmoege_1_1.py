#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# PCL ex4 Aufgabe 1.1
# Dejan Wäckerlin, Ruben Mögel

import bz2, gzip, json


def mk_meme_corpus(infile, outfile, min_score: int=100, min_len: int=1, max_len: int=50):
    """Spits out the worst, the internet has to offer. All you need are some .gzip compressed reddit comments"""
    print("you better get some coffee")

    def iter_json(stream, min_score, min_len, max_len):
        for line in stream:
            line = json.loads(line)
            if line['ups'] >= min_score and len(line['body']) >= min_len and len(line['body']) <= max_len:
                yield line['body']


    def test_hash(element, sentence_hashes):
        sentence_hash = hash(element)
        if sentence_hash not in sentence_hashes:
            sentence_hashes.add(sentence_hash)
            return True
        else:
            return False

    with bz2.open(infile, mode='rt', encoding="utf-8") as inp, \
            gzip.open(outfile, mode='wt') as outfil:
        sentence_hashes = set()
        json_element = iter_json(inp, min_score, min_len, max_len)
        for element in json_element:
            if test_hash(element, sentence_hashes) is True:
                outfil.write(element.replace("\n", " "))
                outfil.write("\n")


def main():
    mk_meme_corpus("Korpusdaten/RC_2012-06.bz2", "something_random.gz")


if __name__ == "__main__":
    main()