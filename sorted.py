import argparse
import os.path
from pathlib import Path
import time


start_time = time.time()
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def lexic_sort(char_ind, file, file_out):
    mas_sorted = []  # обнуление массива для очистки памяти
    for string in file:  # для каждой строки в входном файле
        string = string.split()
        for word in string:  # для каждого слова в входном файле
            if word[0].lower() == chars[char_ind]:
                mas_sorted.append(word)  # добавление в массив только слов начинающихся с текущей буквы словаря CHARS

    # mas_sorted = sorted(sorted(mas_sorted), key=str.lower)  # сортировка массива в лексикографическом порядке
    print("[+] Char " + chars[char_ind] + " is Done")
    for word in mas_sorted:  # запись в выходной файл
        file_out.write(word)
        file_out.write(' ')


def arguments_progam():
    parser = argparse.ArgumentParser(description='Lexicographic order parser program')
    parser.add_argument('--inFile', metavar='inFile', type=str, help='Input File in txt format and utf8 encoding')
    parser.add_argument('--outFile', metavar='outFile', type=str, help='Output File')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = arguments_progam()  # обработка входных параметров
    input_file = args.inFile
    try:
        if not os.path.isfile(input_file):
            print("Error: Input file not exist")
        output_file = args.outFile
        if not os.path.isfile(output_file):
            print("Error: Output file not exist")
            print("[!] Script create this file in same directory")
    except:
        print("Error: Args is not set")
        print("Help: python script.py -h")
        print("Example: python script.py --inFile inputfile.txt --outFile outputfile.txt")
        exit()

    if Path(input_file).suffix != '.txt':
        print("Error: File must be txt format")
        exit()
    for i in range(0, len(chars)):
        f1 = open(input_file, encoding="utf8", errors="ignore")  # открываем файл на чтение
        f2 = open(output_file, 'a+', encoding="utf8", errors="ignore")  # открываем файл на запись
        lexic_sort(i, f1, f2)

    print("--- %s seconds ---" % (time.time() - start_time))
