#!/usr/bin/python



from __future__ import division

from datetime import datetime



import csv



header = "------------------------------------------------------\n"

longspace = "                            "



#find out winning percentage for jockeys and trainers

def CalcWinPCT(starts,wins):

        if int(starts) > 0:

            pct = (int(wins) / int(starts)) * 100

            pct = round(pct)

            pct = int(pct)

            pct = str(pct)

            return pct

        else:

            pct = "0"

            return pct

#convert race distance to readable format

def ConvertDistance(distance):

        if distance == "1100":

            distance = "5F"

        if distance == "1210":

            distance = '5.5F'

            return distance

        if distance == "1320":

            distance = '6F'

            return distance

        if distance == "1430":

            distance = '6.5F'

            return distance

        if distance == "1540":

            distance = '7F'

            return distance

        if distance == "1650":

            distance = '7.5F'

            return distance

        if distance == "1760":

            distance = '1M'

            return distance

        if distance == "1830":

            distance = '1M 70yds'

        if distance == "1870":

            distance = '1M 1/16'

        if distance == "1980":

            distance = '1M 1/8'

            return distance

        if distance == "2200":

            distance = "1M 1/4"

            return distance

        if distance =="2530":

            distance = '1M 7/16'

            return distance

        else:

            return distance

        

#Update track abbreviations here        

def LookupTrack(track):

    if track == "GP":

        track = "Gulfstream Park"

        return track

    if track == "BEL":

        track = "Belmont Park"

        return track

    if track == "AQU":

        track = "Aqueduct"

        return track

#Update surface types here    

def LookupSurface(surface):

    if surface == "":

        return surface

    if surface == "D":

        surface = "Dirt"

        return surface

    if surface == "d":

        surface = "Inner Dirt"

    if surface == "h":

        surface = "Hunt"

    if surface == "s":

        surface = "Steeplechase"

    if surface == "t":

        surface = "Inner Turf"

        return surface

    if surface == "T":

        surface = "Turf"

        return surface

    if surface == ' ':

        surface = ' '

    else:

        #surface = "UPDATE THIS SURFACE TYPE!!!"

        return surface



#Convert date to mm/dd/yyyy format

def ConvertDate01(date):

    fixed_date = datetime.strptime(date, '%Y%m%d')

    fixed_date = fixed_date.strftime('%m-%d-%Y')

    return fixed_date



def ConvertDate02(date):

    if date == '':

        date = " "

        return date

    else:

        fixed_date = datetime.strptime(date, '%Y%m%d')

        fixed_date = fixed_date.strftime('%d%b%Y')

        return fixed_date



def CheckSurface(surface):

    if surface == "SY":

        surface = "SLOPPY"

        return surface

    else:

        return surface



def CheckFinish(finish,entrants):

    if finish == "1":

        finish = "WON " + finish + "/" + entrants

        return finish

    else:

        finish = finish + "/" + entrants

        return finish



def CheckForEmpty(past_race):

    if past_race == "":

        past_race = " "

        return past_race

    else:

        return past_race

    

def ConstructPP(numSpeedFigure01,strPastRaceDate01fixed,strPastRaceTrack01,strPastRaceDistance01fixed,

                strPastRaceSurface01fixed,strPastRaceSurfaceCondition01fixed,strPastRaceType01,strPastRaceFinish01fixed):

        if numSpeedFigure01 == "":

            numSpeedFigure01 = "NA"

            print (numSpeedFigure01 + ": " + strPastRaceDate01fixed + strPastRaceTrack01 + "," + strPastRaceDistance01fixed +"," 

                   + strPastRaceSurface01fixed + "," + strPastRaceSurfaceCondition01fixed + ", " + strPastRaceFinish01fixed + "," 

                   + strPastRaceType01)

        else:

            print (numSpeedFigure01 + ": " + strPastRaceDate01fixed + strPastRaceTrack01 + "," + strPastRaceDistance01fixed +"," 

                   + strPastRaceSurface01fixed + "," + strPastRaceSurfaceCondition01fixed + ", " + strPastRaceFinish01fixed + "," 

                   + strPastRaceType01)



def FormatComments(comments,events,pct,roi):  

    pct = pct[:2] + "%" 

    formatted_comments = comments + "(" + events + " " + pct + " " + roi + ") " 

    return formatted_comments

    

# opens file so we can fuck with it

with open('BEL0906.csv', 'rb') as csvfile:

    reader = csv.reader(csvfile, delimiter=',',)

    for item in reader:

        #Race Information

        strTrackName = item[0].strip()

        strTrackNamefixed = LookupTrack(strTrackName)

        strDate = item[1].strip()

        strDatefixed = ConvertDate01(strDate)

        strRaceNumber = item[2].strip()

        strHorseNumber = item[3].strip()

        strDistance = item[5].strip()

        strDistancefixed = ConvertDistance(strDistance)

        strSurface = item[6].strip()

        strSurfacefixed = LookupSurface(strSurface)

        strRawRaceType = item[10].strip()

        strRaceTypefixed = strRawRaceType

        strRawPurseAmount = item[11].strip()

        strPurseAmountfixed = "$" + strRawPurseAmount

        strRaceSummary = item[224]

        strEarlyPar = item[213].strip()

        strMidPar = item[214].strip()

        strLatePar = item[217].strip()

        strOverallPar = item[216].strip()

        

        #Horse

        strHorseName = item[44].strip()

        strRunningStyle = item[209].strip()

        strEarlySpeedPoints = item[210].strip()

        

        #Jockey

        strJockeyName = item[32].strip()

        numJockeyStartsTrack = item[34]

        numJockeyWinsTrack = item[35]

        numJockeyPlacesTrack = item[36]

        numJockeyShowsTrack = item[37]

        strJockeyWinPCT = CalcWinPCT(numJockeyStartsTrack,numJockeyWinsTrack)

        

        #Trainer

        strTrainerName = item[27].strip()

        numTrainerStartsTrack = item[28]

        numTrainerWinsTrack = item[29]

        numTrainerPlacesTrack = item[30]

        numTrainerShowsTrack = item[31]

        strTrainerWinPCT = CalcWinPCT(numTrainerStartsTrack,numTrainerWinsTrack)

        

        if strHorseNumber == "1":

            print(header)

            print strTrackNamefixed + longspace + strDatefixed + "\n"

            print"Race " + strRaceNumber + ": " + strDistancefixed + ", " + strSurfacefixed + "\n"

            print strRaceTypefixed + ", " + "PURSE: " + strPurseAmountfixed + "\n"

            print strRaceSummary         

            print header + "\n"

            print"PARS\n" 

            print"Early: " + strEarlyPar + ", " + "Mid: " + strMidPar + ", " + "Late: " + strLatePar + "\n"

            print"Overall: " + strOverallPar + "\n"

            

        print strHorseNumber + ") " + strHorseName + " (" + strRunningStyle + " " +  strEarlySpeedPoints + ")\n"

        print ("J: " + strJockeyName + " (" + numJockeyStartsTrack + " " + numJockeyWinsTrack + "-" + numJockeyPlacesTrack + "-" 

               + numJockeyShowsTrack + " " + strJockeyWinPCT + "%)" + " Tr: " + strTrainerName + " (" + numTrainerStartsTrack + " " 

               + numTrainerWinsTrack + "-" + numTrainerPlacesTrack + "-" + numTrainerShowsTrack + " " + strTrainerWinPCT + "%)\n")

        

        #Speed Figures

        numSpeedFigure01 = item[845]

        numSpeedFigure02 = item[846]

        numSpeedFigure03 = item[847] 

        numSpeedFigure04 = item[848]

        numSpeedFigure05 = item[849]

        

        #Dates of last races

        strPastRaceDate01 = item[255].strip()

        strPastRaceDate02 = item[256].strip()

        strPastRaceDate03 = item[257].strip()

        strPastRaceDate04 = item[258].strip()

        strPastRaceDate05 = item[259].strip()

        strPastRaceDate01fixed = ConvertDate02(strPastRaceDate01)

        strPastRaceDate02fixed = ConvertDate02(strPastRaceDate02)

        strPastRaceDate03fixed = ConvertDate02(strPastRaceDate03)

        strPastRaceDate04fixed = ConvertDate02(strPastRaceDate04)

        strPastRaceDate05fixed = ConvertDate02(strPastRaceDate05)

        

        #Distances of last races

        strPastRaceDistance01 = item[315].strip()

        strPastRaceDistance02 = item[316].strip()

        strPastRaceDistance03 = item[317].strip()

        strPastRaceDistance04 = item[318].strip()

        strPastRaceDistance05 = item[319].strip()

        strPastRaceDistance01fixed = ConvertDistance(strPastRaceDistance01)

        strPastRaceDistance02fixed = ConvertDistance(strPastRaceDistance02)

        strPastRaceDistance03fixed = ConvertDistance(strPastRaceDistance03)

        strPastRaceDistance04fixed = ConvertDistance(strPastRaceDistance04)

        strPastRaceDistance05fixed = ConvertDistance(strPastRaceDistance05)

        

        #Surfaces of last races

        strPastRaceSurface01 = item[325].strip()

        strPastRaceSurface02 = item[326].strip()

        strPastRaceSurface03 = item[327].strip()

        strPastRaceSurface04 = item[328].strip()

        strPastRaceSurface05 = item[329].strip()

        strPastRaceSurface01fixed = LookupSurface(strPastRaceSurface01)

        strPastRaceSurface02fixed = LookupSurface(strPastRaceSurface02)

        strPastRaceSurface03fixed = LookupSurface(strPastRaceSurface03)

        strPastRaceSurface04fixed = LookupSurface(strPastRaceSurface04)

        strPastRaceSurface05fixed = LookupSurface(strPastRaceSurface05)

        

        #Surface conditions of last races

        strPastRaceSurfaceCondition01 = item[305].strip()

        strPastRaceSurfaceCondition02 = item[306].strip()

        strPastRaceSurfaceCondition03 = item[307].strip()

        strPastRaceSurfaceCondition04 = item[308].strip()

        strPastRaceSurfaceCondition05 = item[309].strip()

        strPastRaceSurfaceCondition01fixed = CheckSurface(strPastRaceSurfaceCondition01)

        strPastRaceSurfaceCondition02fixed = CheckSurface(strPastRaceSurfaceCondition02)

        strPastRaceSurfaceCondition03fixed = CheckSurface(strPastRaceSurfaceCondition03)

        strPastRaceSurfaceCondition04fixed = CheckSurface(strPastRaceSurfaceCondition04)

        strPastRaceSurfaceCondition05fixed = CheckSurface(strPastRaceSurfaceCondition05)

        

        #Type of last races

        strPastRaceType01 = str(item[535].strip())

        strPastRaceType02 = str(item[536].strip())

        strPastRaceType03 = str(item[537].strip())

        strPastRaceType04 = str(item[538].strip())

        strPastRaceType05 = str(item[539].strip())

 

        #Finish in last races

        strPastRaceFinish01 = item[615].strip()

        strPastRaceFinish02 = item[616].strip()

        strPastRaceFinish03 = item[617].strip()

        strPastRaceFinish04 = item[618].strip()

        strPastRaceFinish05 = item[619].strip()

        strPastRaceEntrants01 = item[345].strip()

        strPastRaceEntrants02 = item[346].strip()

        strPastRaceEntrants03 = item[347].strip()

        strPastRaceEntrants04 = item[348].strip()

        strPastRaceEntrants05 = item[349].strip()

        strPastRaceFinish01fixed = str(CheckFinish(strPastRaceFinish01,strPastRaceEntrants01))

        strPastRaceFinish02fixed = str(CheckFinish(strPastRaceFinish02,strPastRaceEntrants02))

        strPastRaceFinish03fixed = str(CheckFinish(strPastRaceFinish03,strPastRaceEntrants03))

        strPastRaceFinish04fixed = str(CheckFinish(strPastRaceFinish04,strPastRaceEntrants04))

        strPastRaceFinish05fixed = str(CheckFinish(strPastRaceFinish05,strPastRaceEntrants05))

        

        strPastRaceTrack01 = item[275].strip()

        strPastRaceTrack02 = item[276].strip()

        strPastRaceTrack03 = item[277].strip()

        strPastRaceTrack04 = item[278].strip()

        strPastRaceTrack05 = item[279].strip()

            

        #Build Past Performances

        ConstructPP(numSpeedFigure01,strPastRaceDate01fixed,strPastRaceTrack01,strPastRaceDistance01fixed,

                    strPastRaceSurface01fixed,strPastRaceSurfaceCondition01fixed,strPastRaceType01,strPastRaceFinish01fixed);

        ConstructPP(numSpeedFigure02,strPastRaceDate02fixed,strPastRaceTrack02,strPastRaceDistance02fixed,

                    strPastRaceSurface02fixed,strPastRaceSurfaceCondition02fixed,strPastRaceType02,strPastRaceFinish02fixed);

        ConstructPP(numSpeedFigure03,strPastRaceDate03fixed,strPastRaceTrack03,strPastRaceDistance03fixed,

                    strPastRaceSurface03fixed,strPastRaceSurfaceCondition03fixed,strPastRaceType03,strPastRaceFinish03fixed);

        ConstructPP(numSpeedFigure04,strPastRaceDate04fixed,strPastRaceTrack04,strPastRaceDistance04fixed,

                    strPastRaceSurface04fixed,strPastRaceSurfaceCondition04fixed,strPastRaceType04,strPastRaceFinish04fixed);

        ConstructPP(numSpeedFigure05,strPastRaceDate05fixed,strPastRaceTrack05,strPastRaceDistance05fixed,

                    strPastRaceSurface05fixed,strPastRaceSurfaceCondition05fixed,strPastRaceType05,strPastRaceFinish05fixed);

        

        print(longspace)

        

        

        #Input Brisnet Comments

        strComments01 = item[1336].strip()

        strComments01events = item[1337].strip()

        strComments01pct = item[1338].strip()

        strComments01roi = item[1340].strip()

        strComments02 = item[1341].strip()

        strComments02events = item[1342].strip()

        strComments02pct = item[1343].strip()

        strComments02roi = item[1345].strip()

        strComments03 = item[1346].strip()

        strComments03events = item[1347].strip()

        strComments03pct = item[1348].strip()

        strComments03roi = item[1350].strip()

        strComments04 = item[1351].strip()

        strComments04events = item[1352].strip()

        strComments04pct = item[1353].strip()

        strComments04roi = item[1355].strip()

        strComments05 = item[1356].strip()

        strComments05events = item[1357].strip()

        strComments05pct = item[1358].strip()

        strComments05roi = item[1360].strip()

        

        #Print Brisnet Comments

        strComments01fixed = FormatComments(strComments01,strComments01events,strComments01pct,strComments01roi)

        strComments02fixed = FormatComments(strComments02,strComments02events,strComments02pct,strComments02roi)

        strComments03fixed = FormatComments(strComments03,strComments03events,strComments03pct,strComments03roi)

        strComments04fixed = FormatComments(strComments04,strComments04events,strComments04pct,strComments04roi)

        strComments05fixed = FormatComments(strComments05,strComments05events,strComments05pct,strComments05roi)

        print strComments01fixed + strComments02fixed + strComments03fixed + strComments04fixed + strComments05fixed + "\n"

