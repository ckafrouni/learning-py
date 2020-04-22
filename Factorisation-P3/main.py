#!/usr/bin/python3
from helper import timer, factor

def getOutput(parser):
    for num in parser:
        tmp = ''
        for div in factor(num):
            tmp += f' {div}'
        result = f'{num}{tmp}\n'
        yield result

def parse(file):
    with open(file, 'r') as f:
        for line in f:
            number = int(line.strip('\n'))
            yield number

def writeTo(file, parser):
    with open(file, 'w') as f:
        for n in parser:
            f.write(n)

#------------------------------------#

@timer
def main(inputFile, outputFile):
    inputParser = parse(inputFile)
    outputParser = getOutput(inputParser)
    writeTo(outputFile, outputParser)

if __name__ == "__main__":
    inputFile = ".//input.txt"
    outputFile = ".//output.txt"
    main(inputFile, outputFile)
