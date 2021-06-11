def countWordsFromFile():
    fileName =  input("Enter the file name:- ")

    numberOfWords = 0

    file =  open(fileName, 'r')
    for line in file:
        words = line.split()
        
        numberOfWords = numberOfWords + len(words)
        print ("Your file name:") 
        print (fileName)
    print("Number of words in your file:")
  
    print(numberOfWords)


countWordsFromFile()
