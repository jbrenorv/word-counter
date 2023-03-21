from collections import Counter
from os import path
import argparse
import re


def word_conter(file_path):

  if not path.exists(file_path):
    print(f'Erro: Arquivo {file_path} nao encontrado.')
    exit()

  file = open(file_path)
  file_content = file.read()
  words = list(filter(lambda word: word != '', re.split(r'[\s\W]+', file_content)))
  
  if len(words) > 0:
    frequency = sorted(Counter(words).items(), key=lambda item:item[1], reverse=True)
    for word, count in frequency:
      print(f'{count} {word}')
  
  else:
    print('Nenhuma palavra encontrada.')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', default="sample.txt", type=str)
  args = parser.parse_args()
  file_path = args.p

  word_conter(file_path)
