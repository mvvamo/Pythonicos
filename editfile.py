#!/usr/bin/env python

path = raw_input('Digite o caminho absoluto do arquivo: ')
print path
print ''

payload = raw_input('Conteudo a ser inserido no arquivo: ')

print ''
print payload

with open(path,"a") as file:
    file.write(payload);
    file.write("\n");
