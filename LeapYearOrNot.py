
""" These helper functions help determine if a given year  is a leap
    in the Julian and Gregorian calenders respectively
"""

def findJulLeapYear(year:int)->bool:
    """ [Bool] whether or not a given year is leap in the Julian callender"""
    return year%4==0

    
def findGregLeapYear(year:int)->bool:
    """whether or not a given year is leap in the Gregorian callender"""
    return year%400==0 or (year%4==0 and year%100!=0)
