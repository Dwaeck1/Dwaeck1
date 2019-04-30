#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# PCL ex4 Aufgabe 2
# Dejan Wäckerlin, Ruben Mögel

def longest_substrings(word_1: str, word_2: str):
    word_1 = word_1.lower()
    word_2 = word_2.lower()
    matrix = [[0 for j in range(len(word_1)+1)] for i in range(len(word_2)+1)]
    matrix[0][0] = 0
    check_box = 0
    word_list = []
    for i in range(len(word_1)):
        for j in range(len(word_2)):
            if word_1[i] == word_2[j]:
                matrix[j+1][i+1] = matrix[j][i]+1
                if matrix[j+1][i+1] > check_box:
                    check_box = matrix[j+1][i+1]
                    word_list = [word(check_box,word_1,word_2,j+1,i+1)]
                if matrix[j+1][i+1] == check_box:
                    if word(check_box, word_1, word_2, j+1, i+1) not in word_list:
                        word_list.append(word(check_box, word_1, word_2, j+1, i+1))
    if word_list == []:
        print('none')
    else:
        print(word_list)

def word(length, word_1, word_2, j , i):
    new_word = ""
    if len(word_1) >= len(word_2):
        for x in range(length):
            new_word += word_1[i-length+x]
    elif len(word_2) > len(word_1):
        for x in range(length):
            new_word += word_2[j-length+x]
    return new_word


def main():
    longest_substrings("aaabbb", "bbbaaaa")


if __name__ == "__main__":
    main()