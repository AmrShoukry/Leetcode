class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if (date1 > date2):
            return handleDefference(date1, date2)
        return handleDefference(date2, date1)

def handleDefference(date1, date2):
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

    count = 0
    year1, month1, day1 = map(int, date1.split('-'))
    year2, month2, day2 = map(int, date2.split('-'))

    if year1 == year2:
        if month1 == month2:
            if day1 == day2:
                return count
            else:
                count += day1 - day2
                return count
        else:
            for i in range(month2, month1):
                count += months.get(i)
                if (i == 2 and year1 % 4 == 0 and year1 != 2100):
                    count += 1
            count += day1 - day2
            return count      
    else:
        newMonth = 12
        newDay = 31
        for i in range(month2, newMonth):
            count += months.get(i)
            if (i == 2 and year2 % 4 == 0 and year2 != 2100):
                count += 1
        # print(count)
        count += newDay - day2
        count += 1
        year2 += 1
        month2 = 1
        day2 = 1
        # print("Date1: ", year1, month1, day1)
        # print("Date2: ", year2, month2, day2)
        # print(count)
        if year2 == year1:
            if month2 == month1:
                if day2 == day1:
                    return count
                else:
                    print(count)
                    count += day1 - day2
                    return count
            else:
                for i in range(month2, month1):
                    count += months.get(i)
                    if (i == 2 and year1 % 4 == 0 and year1 != 2100):
                        count += 1
                count += day1 - day2
                return count

        else:
            for i in range(year2, year1):
                if (i % 4 == 0 and i != 2100):
                    count += 366
                else:
                    count += 365
            for i in range(month2, month1):
                count += months.get(i)
                if (i == 2 and year1 % 4 == 0 and year1 != 2100):
                    count += 1
            count += day1 - day2
            return count
