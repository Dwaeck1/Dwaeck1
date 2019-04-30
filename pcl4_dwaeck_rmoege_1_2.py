#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# PCL ex4 Aufgabe 1.2
# Dejan Wäckerlin, Ruben Mögel

import gzip, random, lxml.etree as et

def split_corpus(corpus, targetdir='.', n=1000):
    """note: this function relies on the lxml library and outpath is only availeable on unix-like systems"""
    with gzip.open(corpus,"rb") as new:
        with gzip.open(targetdir+"/abstracts.txt.training.gz","wb") as new_file:
            list = knut_algorithm(new,new_file,2*n)
    with gzip.open(targetdir+"/abstracts.txt.test.gz","wb") as second_file:
        for element in list[:n/2-1]:
            second_file.write(element.encode("utf-8")+"\n".encode("utf-8"))
    with gzip.open(targetdir+"/abstracts.txt.development.gz","wb") as third_file:
        for element in list[n/2-1:]:
            third_file.write(element.encode("utf-8")+"\n".encode("utf-8"))

def extract(new):
    for _, document in et.iterparse(new, tag='document'):
        sentence = ' '.join(name.text for name in document.iterfind('.//sentence'))
        yield sentence
        document.clear()

def knut_algorithm(new, new_file, k):
    reservoir = []
    for t, element in enumerate(extract(new)):
        print(t)
        if t < k:
            reservoir.append(element)
        else:
            m = random.randint(0,t)
            if m < k:
                new_file.write(reservoir[m].encode("utf-8")+"\n".encode("utf-8"))
                reservoir[m] = element
    return reservoir

def main():
    split_corpus("abstracts.xml.gz", "", 2000)

if __name__ == "__main__":
    main()