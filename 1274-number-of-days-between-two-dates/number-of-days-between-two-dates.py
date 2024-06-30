class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if (date1 > date2):
            return handleDefference(date1, date2)
        return handleDefference(date2, date1)

def handleDefference(date1, date2):
    count = 0

    def addDays(day1, day2):
        count = 0
        count += day1 - day2
        return count
    
    def addMonths(year, month1, month2, day1, day2):
        count = 0
        for i in range(month2, month1):
                count += months.get(i)
                if (i == 2 and year % 4 == 0 and year != 2100):
                    count += 1
        return count + addDays(day1, day2)

    def addYears(year1, year2, month1, month2, day1, day2):
        count = 0
        for i in range(year2, year1):
            if (i % 4 == 0 and i != 2100):
                count += 366
            else:
                count += 365
        return count + addMonths(year1, month1, month2, day1, day2)

    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    year1, month1, day1 = map(int, date1.split('-'))
    year2, month2, day2 = map(int, date2.split('-'))

    if year1 == year2:
        if month1 == month2:
            if day1 == day2:
                return count
            else:
                return count + addDays(day1, day2)
        else:
            return count + addMonths(year1, month1, month2, day1, day2)   
    else:
        count += addMonths(year2, 12, month2, 31, day2)
        count += 1
        year2 += 1
        month2 = 1
        day2 = 1
        if year2 == year1:
            if month2 == month1:
                if day2 == day1:
                    return count
                else:
                    return count + addDays(day1, day2)
            else:
                return count + addMonths(year1, month1, month2, day1, day2)

        else:
            return count + addYears(year1, year2, month1, month2, day1, day2)

