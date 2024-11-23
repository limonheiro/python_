import re

with open("arquivo_texto.txt", "r") as f:
    line = f.readline()
    words = {}
    while line:
        l = line.split()
        for word in l:
            reWord = re.sub(r'[,.:!\?/\\@\'\"\{\}\(\)\[\]-]', '', word)
            if not reWord in words:
                words[reWord]=0
            words[reWord]+=1
        line = f.readline()

print(f"Total de palavras : {sum(words.values())}")
print(f'Palavras distintas: {len(words.keys())} ' )
print(f'Ocorrência da palavra "texto": { words['texto'] if 'texto' in words else 0}')
        