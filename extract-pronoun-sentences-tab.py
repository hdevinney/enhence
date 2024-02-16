#this pulls all sentences with pronouns and replaces the pronouns with appropriate form of hen
#.tab files in SUC don't have IDs, so we don't need to replace them

#notes:
#controls for Hans (proper noun) and does not convert such instances to 'Hens'
#corrects the morphological information for hen (which can be either subj or obj form)

#TODO BY HAND ONCE YOU'VE RUN THIS FILE:
#check 'hen eller hen' | 'hen och hen' instances and hand-correct (not all need altering)

INPUT_DIR = "</path/to>/SUC3.0/corpus/conll/"
INFILE = "suc-train.conll" 

outfilename = "suc-data/supplements/hen.conll"
devfilename = "suc-data/supplements/hen-dev.conll"
testfilename = "suc-data/supplements/hen-test.conll"

infile = open(INPUT_DIR + INFILE, "r")

outfile = open(outfilename, 'w')
devfile = open(devfilename, 'w')
testfile = open(testfilename, 'w')

count = 0
progress = 0

flag = False

sentence = ""

pronouns = ['Hon', 'hon', 'henne', 'Henne', 'hennes', 'Hennes','Han', 'han', 'honom', 'Honom', 'hans', 'Hans']

def get_replacement_pronoun(str):
    switcher = {
        'hon' : 'hen',
        'Hon' : 'Hen',
        'henne' : 'hen',
        'Henne' : 'Hen',
        'hennes' : 'hens',
        'Hennes' : 'Hens',
        'han' : 'hen',
        'Han' : 'Hen',
        'honom' : 'hen',
        'Honom' : 'Hen',
        'hans' : 'hens',
        'Hans' : 'Hens'
    }
    return switcher.get(str, '')


for line in infile:
    #if count >= 5000:
    #    break
    list = line.split('\t')
    if list[0] == '\n': #end of sentence
        progress = progress + 1
        if flag:
            count = count + 1
            if count % 10 == 0:
                devfile.write(sentence)
                devfile.write('\n')
            elif count % 5 == 0:
                testfile.write(sentence)
                testfile.write('\n')
            else:
                outfile.write(sentence)
                outfile.write('\n')
        sentence = ""
        flag = False
    else:
        if list[0] in pronouns:
            flag = True
            
            #CHECK: is it Hans the proper noun?
            if list[0] == "Hans":
                morph = list[3].split('|')
                if morph[0] == "PM": #part of speech is proper noun
                    #do NOT replace it
                    print("SKIPPING PROPER-NOUN HANS")
                    continue

            #otherwise, replace it
            list[0] = get_replacement_pronoun(list[0])

            if (list[0] == "hen") or (list[0] == "Hen"):
                #update the morphological info
                list[1] = "PN|UTR|SIN|DEF|SUB/OBJ"

            sentence = sentence + list[0] + '\t' + list[1]
        else:
            sentence = sentence + line
        
print(progress)
print(count)
    

infile.close()
outfile.close()
devfile.close()
testfile.close()
