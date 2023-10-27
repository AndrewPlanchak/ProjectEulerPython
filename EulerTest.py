def dateTimeFormatter(time: str, check: bool) -> list[int]: #Takes Check and text and returns a split of the hour and min - and rounds them appropriately
    formattedLoginTime = time.split(":")
    returnList = []
    
    for i in formattedLoginTime:
        i = int(i)
        returnList.append(i)

    return roundFifteenMins(returnList, check)

def roundFifteenMins(rL, check): #If check == true, rounds to the next 15 mins, if check == false rounds to the last 15 mins
    if(rL[1] % 15 == 0): return rL
    else:
        if check == True:
            if rL[1] < 45: rL[1] += (15 - rL[1] % 15)
            else:
                rL[1] = 0
                if not rL[0] == 23: rL[0] += 1
                else: rL[0] = 0
        elif check == False:
            rL[1] -= rL[1] % 15

    return rL       

def compareTimes(loginTime: list[int], logoutTime: list[int]) -> int:

    #loginTime - 9, 3
    #logoutTime - 10, 0

    loginTime[1] /= 15
    logoutTime[1] /= 15

    roundsPlayed = 0

    while not loginTime == logoutTime:
        loginTime[1] += 1
        roundsPlayed += 1

        if loginTime[1] == 4: 
            loginTime[0] += 1
            loginTime[1] = 0
        
        if loginTime[0] == 24:
            loginTime[0] = 0

    return roundsPlayed

loginTime = "00:47"
logoutTime = "00:57"

formattedLoginTime = dateTimeFormatter(loginTime, True)
formattedLogoutTime = dateTimeFormatter(logoutTime, False)

print(formattedLoginTime)
print(formattedLogoutTime)

print(compareTimes(formattedLoginTime, formattedLogoutTime))



        
