def El_COVID(age):
    result =""
    if age<0:
        result = "Invalid age"
    elif age<6:
        result  = "Not eligible"
    elif age<13:
        result = "Eligible for 1 dose"
    elif age<17:
        result = "Eligible for 2 doses"
    elif age<26:
        result = "Eligible for 3 doses"
    elif age<46:
        result = "Eligible for optional dose"
    elif age<61:
        result = "Must take optional dose"
    elif age<86:
        result = "See your GP for eligibility"
    elif age>85:
        result = "Invalid age"

    return result

