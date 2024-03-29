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
# https://realpython.com/python-f-strings/
# https://www.geeksforgeeks.org/python-bitwise-operators/

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
    print("These are the duo binary eleemnts of the list:")
    print(binary_list)
    for index in binary_list:
        binary_str_DNA = binary_str_DNA + index# Puts all the DNA binary characters back to one string as binary
    print("The current binary DNA List Argument: ", binary_str_DNA)
    return binary_str_DNA

def convertDNAList(list_arg, nucleicDict):
    print("This is the dictionary of bases:", nucleicDict)# Check and ensure the bases dictionary was carried through correctly as an argument
    binary_bases_list = []# New list that will have the binary form of the bases
    len(list_arg)
    for index in list_arg:#For each character in the list_arg
        if index in nucleicDict:#If that
           binary_bases_list.append(nucleicDict[index])#Appending the binary forms of the characters
        else:
            print(index);#Displays the character that threw the error
            print("Anomaly present.")
            #print("Exitting now!")
            #exit()# Immediately ends the script upon the detection of an error
            binary_bases_list.append(randomDNAConstructSingleChar())
    print("The current DNA List Argument: ", binary_bases_list) # binary list of the DNA bases that were retrieved
    return binary_bases_list # Returns the list of binary bases.

def convertBinaryToDNA(binaryStrArg,binaryNucleicDict):# The function convertBinaryToDNA is used to convert the binary pairings into the respective nucleic acids
    binaryStrArgList = textwrap.wrap(binaryStrArg, 2)#Separates each pairing of binary digits
    dnaCharList = convertBinaryDNAList(binaryStrArgList,binaryNucleicDict)#Acquiring the nucleic acids as one complete nucleic acid string
    dnaCharStr = ""#Placeholder string
    for element in dnaCharList:#For each nucleic acid, add them eo a single common string
        dnaCharStr = dnaCharStr + element
    print("The current DNA character string: ", dnaCharStr)
    return dnaCharStr

def convertBinaryDNAList(binaryStrArgList,binaryNucleicDict):#The converBinaryDNAList function takes the list of binary digits to convert each pairing to a nucliec acid and checking to make sure that if anomalies are present, a temporary fix is applied
    dna_bases_list = []#The list is initiated
    for element in binaryStrArgList:#For each element within the binary digits pairing list
        if element in binaryNucleicDict:#Going through each pairing of binary digits
            dna_bases_list.append(binaryNucleicDict[element])#Appending the binary pairings to a list
        else:
            print(element)
            print("Anomaly present.")
            #print("Exitting now!")
            #exit()
            dna_bases_list.append(binaryNucleicDict[element+randomBinaryDigit()])#Appending then nucleic bases
    print("The current DNA Characters List: ", dna_bases_list)
    return dna_bases_list

def charArrayConversion(target_char_arr):# Function for transforming the character tothe byte form
    charlist = []#The list is created
    for index in range(len(target_char_arr)):#Going through each char in the list
        num_charlist.append(bin(int.from_bytes(target_char_arr[index].encode(), "big")))#Encoding the char to its byte form
    for index in range(len(charlist)):#Going through each index of the list
        binary_val = bin(index)#Now getting the binary format into a readable, manipulable format
        #index = binary_val[2:]
    binary_string =""#Placeholder string
    for index in range(len(charlist)):#Going through the elements of thhe list
        binary_string = binarystring + index#Appending the binary numbers
    print("Here is the binary string of the message: ", binary_string)
    return binary_string

def messageToBinary(messageStr):#The function messageToBinary is used to convert the message to its binary equivalent
    print("\n")
    print(messageStr)
    messageStrBinary = bin(int.from_bytes(messageStr.encode(), "big"))#Encode the message to binary
    print("Message: " +messageStr+ "; now converted to: " +messageStrBinary+ "; in binary.")
    newMessageStrBinary = removeBytePrefix(messageStrBinary)#Removes the unnecessary prefix
    print("The length of the message in binary:")
    print(len(newMessageStrBinary))
    listOfMessageStrBinary = textwrap.wrap(newMessageStrBinary,8)#Separate the binary character eauivalents of the message
    print("A wonderful binary construct: ")
    print(listOfMessageStrBinary)
    for indexString in listOfMessageStrBinary:#Get the element from the list of binary strings
        indexString = removeBytePrefix(indexString)
    return listOfMessageStrBinary

def messageGenerator():#Function for inputting a message from the user
    print("Input message.")
    message = input()#Input the message
    print("Here is the inputted message.")
    print(message)
    paddedmessage = message+ " "#Pads the message with an extra space
    newBinaryMessage = messageToBinary(paddedmessage)#Convert the inputted the message to binary equivalent
    print("There is the indicated message: ")
    print(newBinaryMessage)
    return newBinaryMessage

def genFirstKey():#Generates the first key for the encryption
    randKey = random.randrange(1,20,1)#Generates a random number between 1 and 20
    print("First key generated", randKey)
    binaryRandKey = keyToBinary(randKey)#Co0nversts the key to binary
    return binaryRandKey

def keyToBinary(numberKey):# The keyToBinary function converts the generated key to its binary equivalent
    binaryTransform = f'{numberKey:08b}'#Formatting the binary representation
    return binaryTransform

def binaryXOR(binaryArg1, binaryArg2):#Does the Binary XOR operation
    print("The value fo the first argument that is binary: ")
    binaryArgInteger1 = convertStringToInteger(binaryArg1)#Converts the first binary argument to its integer equivalent
    print(binaryArg1)
    print(type(binaryArg1))
    print(binaryArgInteger1)
    print("The value of the second argument that is binary: ")
    binaryArgInteger2 = convertStringToInteger(binaryArg2)#Converts second binary argument to its integer equivalent
    print(binaryArg2)
    print(type(binaryArg2))
    print(binaryArgInteger2)
    integerXORResult = binaryArgInteger1 ^ binaryArgInteger2#Get the XOR result from the first binary argument and second binary argument
    print("The XOR Result: ")
    print(integerXORResult)
    binaryXORResult = bin(integerXORResult)#Get the binary equivalent of the XOR result
    print(binaryXORResult)
    return binaryXORResult

def convertStringToInteger(suspectedStrInsteadOfInteger):
    if type(suspectedStrInsteadOfInteger) == str:
        newIntegerCreated = int(suspectedStrInsteadOfInteger,2)
        return newIntegerCreated
    else:
        return suspectedStrInsteadOfInteger

def randomDNAConstruct(length_of_message):
    dnaStr = ""
    r_multiplier = random.randrange(21,100,1)
    total_random_dna_size = length_of_message *r_multiplier
    random_dna_length = random.randrange(length_of_message,total_random_dna_size,1)
    for index in range(total_random_dna_size):
        dnaStr += choice("ACTG")
    return dnaStr

def randomDNAConstructSingleChar():
    dna_char = ""
    for index in range(1):
        dna_char += choice("ACTG")
    return dna_char

def randomBinaryDigit():
    bin_char = ""
    for index in range(1):
        bin_char += choice("01")
    return bin_char

def removeBytePrefix(byteStr):
    if "0b" in byteStr:
        str_byte_prefix_removed = byteStr[0]+byteStr[2:]
        return str_byte_prefix_removed
    else:
        return byteStr

def convertStrListToIntList(strListArg):
    for index in strListArg:
        index = int(index,2)
    return strListArg

def formatBinaryStringList(binaryStrListArg):
    formattedBinaryStrListArg = []
    print("Is the binary String Argument being passed corrctly:")
    print(binaryStrListArg)
    for element in binaryStrListArg:
        newFormattedElementInt = int(element,2)
        print(element)
        print("Formatted binary element: ")
        print(newFormattedElementInt)
        newBinaryReturnString = f'{newFormattedElementInt:08b}'
        print("New string value is here:")
        print(newBinaryReturnString)
        formattedBinaryStrListArg.append(newBinaryReturnString)
    print("This is the formatted binary eleements within a list:")
    print(formattedBinaryStrListArg)
    return formattedBinaryStrListArg


def encryptMessage(firstKey, plaintextMessageList):
    print("We made it.")
    print(plaintextMessageList)
    firstKey_prefix_removed = removeBytePrefix(firstKey)
    cumulativeMessageList = []
    plaintextMessageList = convertStrListToIntList(plaintextMessageList)
    print(plaintextMessageList[0])
    firstResult = binaryXOR(firstKey_prefix_removed,plaintextMessageList[0])
    cumulativeMessageList.append(str(firstResult))
    currentResult = firstResult
    for indexNumber in range(len(plaintextMessageList)-1):
        if indexNumber == 0:
            pass
        else:
            currentResult = binaryXOR(currentResult,plaintextMessageList[indexNumber])
            cumulativeMessageList.append(currentResult)
    print("What happened to the elements of the list:")
    print(cumulativeMessageList)
    """
    with open("./binary_messagelist.txt","w") as filedesignation:
        space_str = " "
        filedesignation.write(space_str.join(cumulativeMessageList))
    """
    print("Checking values in List of XOR errors: ")
    cumulativeMessageListFormatted = formatBinaryStringList(cumulativeMessageList)
    print(cumulativeMessageListFormatted)
    return cumulativeMessageListFormatted

def decryptMessage(firstKey, encryptedMessageList):
    print("Decryption has started: ")
    firstKey_prefix_removed = removeBytePrefix(firstKey)
    encryptedMessagePassStr = listToString(encryptedMessageList)
    encryptedMessageList = textwrap.wrap(encryptedMessagePassStr,8)
    cumulativeMessageList = []
    print("WHat we are decrypting: ")
    print(encryptedMessageList)
    firstResult = binaryXOR(firstKey_prefix_removed,encryptedMessageList[0])
    cumulativeMessageList.append(firstResult)
    currentResult = ""
    for indexNumber in range(len(encryptedMessageList)-1):
        if indexNumber == 0:
            pass
        else:
            currentResult = binaryXOR(encryptedMessageList[indexNumber],encryptedMessageList[indexNumber-1])
            print("XOR Result for the decryption path: ")
            print(currentResult)
            cumulativeMessageList.append(currentResult)
    cumulativeMessageListFormatted = formatBinaryStringList(cumulativeMessageList)
    print("Checking for any misformatting issues in list: ")
    print(cumulativeMessageListFormatted)
    decryptedMessageStr = listToString(cumulativeMessageListFormatted)
    return decryptedMessageStr

def listToString(strInListArg):
    compiledStringVar =""
    for element in strInListArg:
        if (type(element) == str):
            compiledStringVar+= element
        else:
            elementStringInstance = str(element)
            compiledStringVar+= elementStringInstance
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
    print("Printing the broken binary dna now:")
    print(brokenBinaryDNA)
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
        capturedStr = brokenBinaryDNAWithMessage[indexPosition]
        significantBitExtract = capturedStr[:1]
        decryptedStrList.append(significantBitExtract)
        #print("The current decrypted string list: ")
        #print(decryptedStrList)
    decryptedStrList
    print("Decrypted Message within this list:")
    print(decryptedStrList)
    return decryptedStrList
    #maxLimit = range(len(binaryDNA))-1
    #for index in range(0,maxLimit,randomKey2):

def convertDecryptedStrToMessage(extractedSignificantBitMessageStrArg, lastPositionForDecryption):
    eightBitByteElementsList = textwrap.wrap(extractedSignificantBitMessageStrArg,8)
    print("Broken list of the byte elements:")
    print(eightBitByteElementsList)
    messageCharacterList = []
    for binaryElement in range(lastPositionForDecryption):#eightBitByteElementsList:
        newlyGeneratedInteger = convertStringToInteger(eightBitByteElementsList[binaryElement])
        print("Checking if integer Conversion worked")
        print(newlyGeneratedInteger)
        characterRetrieve = newlyGeneratedInteger.to_bytes((newlyGeneratedInteger.bit_length()+7) // 8, "big").decode()
        print("This is the character retrieved: ")
        print(characterRetrieve)
        messageCharacterList.append(characterRetrieve)
    print(messageCharacterList)
    messageCharactersFromDecryption =listToString(messageCharacterList)
    return messageCharactersFromDecryption


def main():
    dnaDict = {"A":"00", "C": "01", "G": "10", "T": "11"}
    binaryDnaDict = {"00":"A", "01": "C", "10": "G", "11": "T"}
    binMessage = messageGenerator()
    startDNA = randomDNAConstruct(len(binMessage))
    binary_DNA = convertDNABinary(startDNA,dnaDict)
    print("Length of Binary DNA:")
    print(len(binary_DNA))
    firstKeyForEncryption = genFirstKey()
    encryptedBinaryList = encryptMessage(firstKeyForEncryption, binMessage)
    decryptLimit = (len(encryptedBinaryList))
    encryptedBinaryString = listToString(encryptedBinaryList)
    secondKeyForEncryption,encryptedBinaryMessageComplete = insertBitElements(binary_DNA, encryptedBinaryString)
    print("The final encrypted message in binary is:" + str(encryptedBinaryMessageComplete))
    fullDNAEncryptedCharacterString = convertBinaryToDNA(encryptedBinaryMessageComplete,binaryDnaDict)
    print("Full DNA Xharacter Encrypted String: "+fullDNAEncryptedCharacterString)
    main2(firstKeyForEncryption, secondKeyForEncryption, fullDNAEncryptedCharacterString, dnaDict, binaryDnaDict,decryptLimit)

def main2(firstEncryptionKey,secondEncryptionKey,encryptedDNAMessage, dnaDict, binaryDNAdict, limitationForDecryption):
    print("Length of Encrypted DNA Message:")
    print(len(encryptedDNAMessage))
    encryptedBitsFromDNA = convertDNABinary(encryptedDNAMessage, dnaDict)
    significantBitExtractionList = extractBitElements(encryptedBitsFromDNA, secondEncryptionKey)
    extractedSignificantBitMessageStr = decryptMessage(firstEncryptionKey, significantBitExtractionList)
    print("The extracted message:")
    print(extractedSignificantBitMessageStr)
    finalDecryptedMessage = convertDecryptedStrToMessage(extractedSignificantBitMessageStr,limitationForDecryption)
    print("Final result of decryption: ")
    print(finalDecryptedMessage)

main()
