import re
from os import listdir
from os.path import isfile, join

mypath = '.'
outfilename = 'portfolio.csv'
outfile = open(join(mypath, outfilename), "w")
outfile.write("Filename,Mode,Ticker,Value\n")

def process_file(line, mode):
        if f == 'StudentName.md':
                return

        if 'BUY' in line or 'Buy' in line:
                if line[0:2] != '##':
                        mode = 'BUY'
        elif 'SELL' in line or '# Sell' in line:
                mode = 'SELL'

        if line[0] != '#':
                matches = re.match("([A-z]*)[\s-]*([0-9,$]+)", line)
                if(matches):
                        split = matches.groups()
                        outfile.write(f + "," + mode + "," + split[0]+ "," + re.sub("[,$]", "", split[1]) + "\n" )

        return mode
            
for f in listdir(mypath):
   mode = "?"
   if isfile(join(mypath, f)) and (f[-2:] == 'md' or f[-3:] == 'txt'):
        print(f)
        filedata = open(join(mypath, f), "r")

        for line in filedata:
                mode = process_file(line, mode)