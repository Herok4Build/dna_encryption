#Thomas Hilton Johnson III
#3/15/2019
#Applied Cryptography
#Dr. Sengupta
#DNA Encryption Algorithm
#reference :https://stackoverflow.com/questions/22571259/split-a-string-into-n-equal-parts
#reference:https://stackoverflow.com/questions/32554527/typeerror-list-indices-must-be-integers-or-slices-not-str
#reference:https://stackoverflow.com/questions/10059554/inserting-characters-at-the-start-and-end-of-a-string
#reference: https://docs.python.org/2/library/functions.html#bin
#reference: https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
#https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa author jfs
# https://stackoverflow.com/questions/21205836/generating-random-sequences-of-dna
import textwrap
import random
from random import choice

def inputStringDNA():#Function for generating String from user input
    string_DNA = input("Type in the DNA String.\n")
    print(string_DNA)
    return string_DNA

def splitString(strArg):#Function for splitting string into separate parts
    separation_factor = eval(input("Please enter the number of characters to keep per string.\n"))#Input of the number of characters that will be allocated to each partition
    list_of_str = textwrap.wrap(strArg, separation_factor)#Breaks the string into a list of substrings, sized determined by the separation_factor variable
    print(list_of_str)
    return list_of_str

def addCharacter(listArg, charArrayArg):#Can add a character to the beginning of ech partition of the of the substrings that make uyp the larger string
    listSize = len(listArg)#Stores the number of partitions (substrings) of the original string
    for index in range(listSize):#The for loop iterates through the list, selecting each substring
        #charInput = input("Input character.\n")#Input a character
        listArg[index] = charArrayArg[index] + listArg[index]#Adds an inputted character at the beginning of the string
        index = index+1# iterates index up
    print(listArg)

def convertDNABinary(strDNA, nucleicDict):
    separation = 1 # Variable for determing the separation of the message
    list_of_acids = textwrap.wrap(strDNA, separation) # Takes the String of DNA characters and separate them individually
    binary_list = convertDNAList(list_of_acids, nucleicDict)# Transforms the list of DNA character elements to binary
    binary_str_DNA = ""
    for index in binary_list:
        binary_str_DNA = binary_str_DNA + index# Puts all the DNA binary characters back to one string as binary
    print("The current binary DNA List Argument: ", binary_str_DNA)
    return binary_str_DNA

def convertDNAList(list_arg, nucleicDict):
    print("This is the dictionary of bases:", nucleicDict)# Check and ensure the bases dictionary was carried through correctly as an argument
    binary_bases_list = []# New list that will have the binary form of the bases
    for index in list_arg:#For each character in the list_arg
        if index in nucleicDict:#If that
           binary_bases_list.append(nucleicDict[index])#Appending the binary forms of the characters
        else:
            print(index);#Displays the character that threw the error
            print("Anomaly present.")
            print("Exitting now!")
            exit()# Immediately ends the script upon the detection of an error
    print("The current DNA List Argument: ", binary_bases_list) # binary list of the DNA bases that were retrieved
    return binary_bases_list # Returns the list of binary bases.

def convertBinaryToDNA(binaryStrArg,binaryNucleicDict):
    binaryStrArgList = textwrap.wrap(binaryStrArg, 2)
    dnaCharList = convertBinaryDNAList(binaryStrArgList,binaryNucleicDict)
    dnaCharStr = ""
    for element in dnaCharList:
        dnaCharStr = dnaCharStr + element
    print("The current DNA character string: ", dnaCharStr)
    return dnaCharStr

def convertBinaryDNAList(binaryStrArgList,binaryNucleicDict):
    dna_bases_list = []
    for element in binaryStrArgList:
        if element in binaryNucleicDict:
            dna_bases_list.append(binaryNucleicDict[element])
        else:
            print(element)
            print("Anomaly present.")
            print("Exitting now!")
            exit()
    print("The current DNA Characters List: ", dna_bases_list)
    return dna_bases_list

def charArrayConversion(target_char_arr):# Function for transforming the
    charlist = []
    for index in range(len(target_char_arr)):
        num_charlist.append(bin(int.from_bytes(target_char_arr[index].encode(), "big")))
    for index in range(len(charlist)):
        binary_val = bin(index)
        #index = binary_val[2:]
    binary_string =""
    for index in range(len(charlist)):
        binary_string = binarystring + index
    print("Here is the binary string of the message: ", binary_string)
    return binary_string

def messageToBinary(messageStr):
    print("\n")
    print(messageStr)
    messageStrBinary = bin(int.from_bytes(messageStr.encode(), "big"))
    print("Message: " +messageStr+ "; now converted to: " +messageStrBinary+ "; in binary.")
    newMessageStrBinary = removeBytePrefix(messageStrBinary)
    listOfMessageStrBinary = textwrap.wrap(newMessageStrBinary,8)
    print("A wonderful binary construct: ")
    print(listOfMessageStrBinary)
    for indexString in listOfMessageStrBinary:
        indexString = removeBytePrefix(indexString)
    return listOfMessageStrBinary

def messageGenerator():
    print("Input message.")
    message = input()
    print("Here is the inputted message.")
    print(message)
    newBinaryMessage = messageToBinary(message)
    print("There is the indicated message: ")
    print(newBinaryMessage)
    return newBinaryMessage

def genFirstKey():
    randKey = random.randrange(1,20,1)
    print("First key generated", randKey)
    binaryRandKey = keyToBinary(randKey)
    return binaryRandKey

def keyToBinary(numberKey):
    binaryTransform = f'{numberKey:08b}'
    return binaryTransform

def binaryXOR(binaryArg1, binaryArg2):
    binaryXORResult = int(binaryArg1,2) ^ int(binaryArg2,2)
    return binaryXORResult

def randomDNAConstruct():
    dnaStr = ""
    for index in range(200000):
        dnaStr += choice("ACTG")
    return dnaStr

def removeBytePrefix(byteStr):
    if "0b" in byteStr:
        str_byte_prefix_removed = byteStr[0]+byteStr[2:]
        return str_byte_prefix_removed
    else:
        return byteStr

def encryptMessage(firstKey, plaintextMessageList):
    print("We made it.")
    firstKey_prefix_removed = removeBytePrefix(firstKey)
    cumulativeMessageList = []
    print(plaintextMessageList[0])
    firstResult = binaryXOR(firstKey_prefix_removed,plaintextMessageList[0])
    cumulativeMessageList.append(firstResult)
    currentResult = firstResult
    for indexNumber in range(len(plaintextMessageList)-1):
        if indexNumber == 0:
            pass
        else:
            currentResult = binaryXOR(currentResult,plaintextMessageList[indexNumber])
            cumulativeMessageList.append(currentResult)
    return cumulativeMessageList

def decryptMessage(firstKey, encryptedMessageList):
    firstKey_prefix_removed = removeBytePrefix(firstKey)
    cumulativeMessageList = []
    print(encryptedMessageList[0])
    firstResult = binaryXOR(firstKey_prefix_removed,encryptedMessageList[0])
    cumulativeMessageList.append(firstResult)
    currentResult = firstResult
    for indexNumber in range(len(encryptedMessageList)-1):
        if indexNumber == 0:
            pass
        else:
            currentResult = binaryXOR(currentResult,encryptedMessageList[indexNumber])
            cumulativeMessageList.append(currentResult)
    decryptedMessageStr = listToString(cumulativeMessageList)
    return decryptedMessageStr

def listToString(strInListArg):
    compiledStringVar =""
    for element in strInListArg:
        compiledStringVar+= element
    return compiledStringVar

def insertBitElements(binaryDNA, encryptedMessageBinaryPrefix):
    randomKey2 = random.randrange(1,20,1)
    encryptedMessageBinaryPrefixList = textwrap.wrap(encryptedMessageBinaryPrefix,1)
    for element in encryptedMessageBinaryPrefixList:
        if element == "b":
            encryptedMessageBinaryPrefixList.remove(element)
    print("Binary formatted list that may have errors: ")
    print(encryptedMessageBinaryPrefixList)
    encryptedMessageBinary = listToString(encryptedMessageBinaryPrefixList)
    brokenBinaryDNA = textwrap.wrap(binaryDNA, randomKey2)
    brokenEncryptedMessageBinary = textwrap.wrap(encryptedMessageBinary, 1)
    encryptedStrList =[]
    for indexPosition in range(len(brokenBinaryDNA)-1):
        if indexPosition < len(brokenEncryptedMessageBinary):
            print(encryptedMessageBinary)
            print("List elements of DNA and Encrypted message:\n")
            print(brokenBinaryDNA[indexPosition])
            print(brokenEncryptedMessageBinary[indexPosition])
            print("\n")
            temporaryStr = brokenEncryptedMessageBinary[indexPosition] + brokenBinaryDNA[indexPosition]
            encryptedStrList.append(temporaryStr)
            print(encryptedStrList)
        else:
            encryptedStrList.append(brokenBinaryDNA[indexPosition])
    newEncryptedBinaryStr= listToString(encryptedStrList)
    print("NewEncrypted Message:")
    print(newEncryptedBinaryStr)
    return randomKey2, newEncryptedBinaryStr

def extractBitElements(decryptedMessageBinaryPrefix, secondEncryptionKey):
    decryptedMessageBinaryPrefixList = textwrap.wrap(decryptedMessageBinaryPrefix,1)
    for element in decryptedMessageBinaryPrefixList:
        if element == "b":
            decryptedMessageBinaryPrefixList.remove(element)
    decryptedMessageBinary = listToString(decryptedMessageBinaryPrefixList)
    brokenBinaryDNAWithMessage = textwrap.wrap(decryptedMessageBinary, secondEncryptionKey+1)
    decryptedStrList =[]
    for indexPosition in range(len(brokenBinaryDNAWithMessage)-1):
        capturedStr = brokenDecryptedMessageBinary[indexPosition]
        significantBitExtract = capturedStr[:1]
        decryptedStrList.append(significantBitExtract)
        print("The current decrypted string list: ")
        print(decryptedStrList)
    decryptedStrList
    print("Decrypted Message within this list:")
    print(decryptedStrList)
    return decryptedStrList
    #maxLimit = range(len(binaryDNA))-1
    #for index in range(0,maxLimit,randomKey2):




def main():
    dnaDict = {"A":"00", "C": "01", "G": "10", "T": "11"}
    binaryDnaDict = {"00":"A", "01": "C", "10": "G", "11": "T"}
    startDNA = randomDNAConstruct()
    binMessage = messageGenerator()
    binary_DNA = convertDNABinary(startDNA,dnaDict)
    firstKeyForEncryption = genFirstKey()
    encryptedBinaryList = encryptMessage(firstKeyForEncryption, binMessage)
    encryptedBinaryString = listToString(encryptedBinaryList)
    secondKeyForEncryption,encryptedBinaryMessageComplete = insertBitElements(binary_DNA, encryptedBinaryString)
    print("The final encrypted message in binary is:" + str(encryptedBinaryMessageComplete))
    fullDNAEncryptedCharacterString = convertBinaryToDNA(encryptedBinaryMessageComplete,binaryDnaDict)
    print("Full DNA Xharacter Encrypted String: "+fullDNAEncryptedCharacterString)
    main2(firstKeyForEncryption, secondKeyForEncryption, fullDNAEncryptedCharacterString, dnaDict, binaryDnaDict)

def main2(firstEncryptionKey,SecondEncryptionKey,encryptedDNAMessage, dnaDict, binaryDNAdict):
    encryptedBitsFromDNA = convertDNABinary(encryptedDNAMessage)
    significantBitExtractionList = extractBitElements(encryptedBitsFromDNA, secondEncryptionKey):
    extractedSignificantBitMessageStr = decryptMessage(firstEncryptionKey, significantBitExtractionList)
    print("The extracted message:")
    print(extractedSignificantBitMessageStr)



main()
