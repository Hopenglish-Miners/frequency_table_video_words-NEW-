import json
f_v=open('vocabulary.json')
vocab = json.load(f_v)

f_w=open('videoData_vs_WordList.json')
v_word = json.load(f_w)

writeToFile=open('HellO.json','w')

wordList = []
#wordOfNumber = 0
tag = 1

for x in range(0, 235):
    for word in v_word[x]['wordList']:
        #print (word)
        for tempWord in wordList:
            if(tempWord == word):
                #print word
                tag = 0
                break
            tag = 1
        if(tag == 1):
            wordList.append(word)
            #print word
            #wordOfNumber = wordOfNumber + 1

#print (wordOfNumber)


wordOfFrequency = [0]*12008
Choser = 0
     


for tempWord in wordList:
    for x in range(0, 235):
        for word in v_word[x]['wordList']:
            if(tempWord == word):
                wordOfFrequency[Choser] = wordOfFrequency[Choser] + 1        
    Choser = Choser + 1

summ = 0
    
for x in wordOfFrequency:
    #print x
    summ = summ + x

#print (summ)

writeToFile.write("[")
count=0
wordListIndex=-1

for i in wordList:
    wordListIndex = wordListIndex +1 
    find=False  #not find
    for level in range(1,7):
        if not find:
            for j in vocab['LEVEL'+str(level)]["words"]:
                if(i==j):
                    if(wordListIndex!=0):
                        writeToFile.write(",")
                    json.dump({'word':str(i),'frequency': str(wordOfFrequency[wordListIndex]),'Level':str(level)},writeToFile)
                    #print i,wordOfFrequency[wordListIndex],level
                    #count=count+1
                    find=True #find the word in dictionary
                    break
                elif(i!=j and level==6 and j==vocab['LEVEL'+str(level)]["words"][vocab['LEVEL'+str(level)]["total"]-1]):
                    if(wordListIndex!=0):
                        writeToFile.write(",")
                    json.dump({'word':str(i),'frequency': str(wordOfFrequency[wordListIndex]),'Level':"-1"},writeToFile)
                    #print i,wordOfFrequency[wordListIndex],-1
                    count=count+1

writeToFile.write("]")
writeToFile.close()
print count
#print wordList[104]
#print len(wordList)
