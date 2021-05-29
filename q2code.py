def leapyear(username):
    if (username % 400) == 0 :
        return("is a leap year")
    else:
        if (username % 100) == 0 :
            return("is not a leap year")
        else:
            if (username % 4) == 0 :
                return("is a leap year")
            else:
                return("is not a leap year")

