# text scraper

with open('text.txt', 'r', encoding='utf-8') as f:
    f_lines = f.readlines()
    print(f_lines)
    for i in f:
        ' '.split(i)
        if i == 'Float':
            print(i)

