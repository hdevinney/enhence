#THIS ONE IS FOR THE conllu FILES PROVIDED BY UD SWEDISH TALBANKEN (https://github.com/UniversalDependencies/UD_Swedish-Talbanken/blob/master/sv_talbanken-ud-test.conllu)
#notes:
#"sv_talbanken-ud.conllu" is just the train/dev/test files glued together...
#we don't retain any of the comment lines (sent_id, text)

#update notes:
#controls for Hans (proper noun) and does not convert such instances to 'Hens'
#corrects the morphological information for hen (which can be either subj or obj form)

#TODO BY HAND ONCE YOU'VE RUN THIS FILE:
#check 'hen eller hen' | 'hen och hen' instances and hand-correct (not all need altering)


INPUT_DIR = "suc-data/supplements/udt/"
INFILE = "sv_talbanken-ud.conllu" 

outfilename = "suc-data/supplements/udt/sv_talbanken-hen.conllu"
devfilename = "suc-data/supplements/udt/sv_talbanken-hen-dev.conllu"
testfilename = "suc-data/supplements/udt/sv_talbanken-hen-test.conllu"

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
    elif list[0][0] == "#": #comment/ignore this line
        print(list)
        continue
    else:
        print(list)
        #list[1] is the token as it appears in the text
        if list[1] in pronouns:
            flag = True

            #CHECK: is it Hans the proper noun?
            if list[1] == "Hans":
                if list[3] == "PROPN": #part of speech is proper noun
                    #do NOT replace it
                    print("SKIPPING PROPER-NOUN HANS")
                    continue
            
            list[1] = get_replacement_pronoun(list[1]) #replace token
            list[2] = get_replacement_pronoun(list[2]) #also replace the gloss

            if (list[1] == "hen") or (list[1] == "Hen"):
                #update the morphological info (line[4] and line[5])
                list[4] = "UTR|SIN|DEF|SUB/OBJ" #as with 'den'
                list[5] = "Definite=Def|Gender=Com|Number=Sing|PronType=Prs" #this is also just 'den's morph info :)


            
            replaced = '\t'.join(list) 
            sentence = sentence + replaced
        else: #not a personal pronoun, do nothing
            replaced = '\t'.join(list)
            sentence = sentence + replaced
        
print(progress)
print(count)
    

infile.close()
outfile.close()
devfile.close()
testfile.close()
