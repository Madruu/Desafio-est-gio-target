def count_as(s):
    count = s.lower().count('a')
    return count

palavra = input("Insira uma palavra: ")

count = count_as(palavra)

if(count > 0):
    print(f'A palavra {palavra} possui {count} letra(s) A.')
else:
    print(f'A palavra {palavra} não possui letra A.')