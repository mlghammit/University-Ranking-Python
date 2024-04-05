# The function of this program is to read data from the capitals.csv and TopUni.csv files and output into the output.txt file

# the function getInformation outputs all information when given a specific country
def getInformation(selectedCountry, TopUni="input.dat", capitals="input.dat"):
    # open the output.txt file in writing mode
    o = open("output.txt", "w", encoding='utf8')
    # open the capitals.csv file in reading mode
    c = open("capitals.csv", "r", encoding='utf8')
    # skip the first line of the file
    next(c)
    # open the TopUni.csv file in reading mode
    t = open("TopUni.csv", "r", encoding='utf8')
    # skip the first line of the file
    next(t)

    # all the universities are put into this list
    uniList = []
    # all the countries are put into this list
    countList = []
    # this list has countries and its corresponding continent
    finalList = []
    # all the continents are put into this list
    contList = []
    # this list keeps track of the university ranks
    uniRank = []
    # this list keeps tracks of the scores of the universities of a specific country
    totalCount = []
    # this list keeps tracks of the 'capital' universities
    capUniList = []

    # for loop that goes through the lines in TopUni.csv
    for line in t:
        # changes the line to all upper case letters, and gets rid of newline characters and splits between commas
        line = line.upper().strip("\n").split(",")
        # append all uni to the end of unilist
        uniList.append(line[1])
        # append all countries to the end of countList
        if line[2] not in countList:
            countList.append(line[2])

    # for loop goes through the lines in capitals.csv
    for line in c:
        # changes the line to all upper case letters, and gets rid of newline characters and splits between commas
        line = line.upper().strip("\n").split(",")
        # appends the countries and its corresponding continent right after it
        finalList.append(line[0])
        finalList.append(line[5])

    # for loop runs for the length of countList
    for i in range(len(countList)):
        # add the continents of the universities in the order that they show up in the university list
        if finalList[(finalList.index(countList[i])) + 1] not in contList:
            contList.append(finalList[(finalList.index(countList[i])) + 1])

    # for loop goes through the final list, only going through the continents
    for i in range(len(finalList), 2):
        # add continents to the continent list
        if finalList[i] not in contList:
            contList.append(finalList[i])

    # write the total number of universities in the output.txt file
    o.write("The total number of universities => {}\n".format(len(uniList)))
    # write the available countries in the output.txt file
    o.write("Available countries => {}\n".format(countList))
    # write the available continents in the output.txt file
    o.write("Available continents => {}\n".format(contList))

    # python is case-sensitive, uppercase country the user inputs
    selectedCountry = selectedCountry.upper()
    # program only works if the file is opened again (even though it was never closed to begin with)
    with open('TopUni.csv', 'r') as t:
        # count = 0
        c = 0
        # for loop goes through lines in TopUni.csv
        for line in t:
            # changes the line to all upper case letters, and gets rid of newline characters and splits between commas
            line = line.upper().strip("\n").split(",")
            # look for selectedCountry in topUni file and find the international and national rank
            if line[2].upper() == selectedCountry:
                if c == 0:
                    # output international rank to output.txt file
                    o.write("At international rank => {} The university name is => {}\n".format(line[0], line[1]))
                    # count is changed to 1 so international rank will not print more than once
                    c += 1
                    # only output the national rank if the selectedCountry is ranked 1 nationally
                if line[3] == "1":
                    # output national rank to output.txt file
                    o.write("At national rank => {} The university name is => {}\n".format(line[3], line[1]))
                    break
    # program only works if the file is opened again (even though it was never closed to begin with)
    with open('TopUni.csv', 'r') as t:
        # for loop goes through lines in TopUni.csv
        for line in t:
            # changes the line to all upper case letters, and gets rid of newline characters and splits between commas
            line = line.upper().strip("\n").split(",")
            # go through the topUni file until it finds the selectedCountry, then append the uni ranking
            if line[2] == selectedCountry:
                uniRank.append(line[8])
        # turns the uni rank strings into integers
        uniRankNum = [eval(i) for i in uniRank]
        # finds the total uniRank
        uniRankTotal = sum(uniRankNum)
        # output the average score to the output.txt file
        o.write("The average score => {}%\n".format(uniRankTotal / len(uniRankNum)))

    # program only works if the file is opened again (even though it was never closed to begin with)
    with open('TopUni.csv', 'r') as t:
        # skip the first line of the file
        next(t)
        # gets the continent of the selectedCountry
        cont = (finalList.index(selectedCountry) + 1)
        # for loop goes through the lines in TopUni
        for line in t:
            # changes the line to all upper case letters, and gets rid of newline characters and splits between commas
            line = line.upper().strip("\n").split(",")
            # check the index of the continent that the country is in from the list previously read
            contCheck = (finalList.index(line[2]) + 1)
            # if the indexes match then it adds the score for that particular continent
            if finalList[contCheck] == finalList[cont]:
                totalCount.append(line[8])
        # turns the score strings into integers
        highscore = [eval(i) for i in totalCount]
        # find the max score
        maxHighscore = max(highscore)
        # calculate the average
        averageScore = uniRankTotal / len(uniRankNum)
        # calculate the relative score to the top uni in the continent
        relativeScore = (averageScore / maxHighscore) * 100
        # output the relative score into the output.txt file
        o.write("The relative score to the top university in {} is => ({} / {}) x 100% = {}%\n".format(finalList[cont], averageScore, maxHighscore, relativeScore))

    # program only works if the file is opened again (even though it was never closed to begin with)
    with open('capitals.csv', 'r') as c:
        # for loop goes through lines in capitals.csv
        for line in c:
            # changes the line to all upper case letters, and gets rid of newline characters and splits between commas
            line = line.upper().strip("\n").split(",")
            # finds the capital of the selectedCountry
            if line[0] == selectedCountry:
                capitalName = line[1]
                o.write("The capital is => {}\n".format(capitalName))

    # program only works if the file is opened again (even though it was never closed to begin with)
    with open('TopUni.csv', 'r') as t:
        # for loop goes through lines in TopUni.csv file
        for line in t:
            # changes the line to all upper case letters, and gets rid of newline characters and splits between commas
            line = line.upper().strip("\n").split(",")
            # looks for capital name in the universities
            if capitalName in line[1]:
                capUniList.append(line[1])
        # output the universities containing the capital name to output.txt file
        o.write("The universities that contain the capital name =>\n")
        for i in range(len(capUniList)):
            # outputs it in an indented list
            o.write("\t#{} {}\n".format(i + 1, capUniList[i]))

# close all files
    o.close()
    c.close()
    t.close()
