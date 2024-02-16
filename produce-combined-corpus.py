#select proportion of hen sentences
HEN_SENTENCES_NO = 227    # 2% of SUC
#HEN_SENTENCES_NO = 1137   # 10% of SUC
#HEN_SENTENCES_NO = 9096   # 80% of SUC


INPUT_DIR = "suc-data/"
INFILE = "suc-train.tab"

henfilename =  "suc-data/supplements/hen.tab"
outfilename = "suc-data/supplements/suc-hen-" + str(HEN_SENTENCES_NO) + ".tab"

print(outfilename)

infile = open(INPUT_DIR + INFILE, "r")
henfile = open(henfilename, "r") 
outfile = open(outfilename, 'w')

count = 0
progress = 0

flag = False

sentence = ""
count = 0

while count < HEN_SENTENCES_NO:
    line = henfile.readline()
    list = line.split('\t')
    if list[0] == '\n':
        outfile.write(sentence)
        outfile.write('\n') 
        sentence = ""
        count = count + 1
    else:
        sentence = sentence + line
        
    
for line in infile:
    outfile.write(line)



    

infile.close()
outfile.close()
henfile.close()

