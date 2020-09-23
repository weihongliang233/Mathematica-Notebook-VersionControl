import difflib

file1 = open('exported.html', 'r',encoding='UTF-8').readlines()
file2 = open('exported-no.html', 'r',encoding='UTF-8').readlines()

htmlDiffer = difflib.HtmlDiff()
htmldiffs = htmlDiffer.make_file(file1, file2)

with open('comparison.html', 'w',encoding='UTF-8') as outfile:
    outfile.write(htmldiffs)