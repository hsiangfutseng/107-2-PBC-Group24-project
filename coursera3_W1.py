"""calculate midterm answer situation"""

import csv

class Time:
    """
    def isvalidTime(self):
        if 0 <= self.hr < 13 and 0 <= self.min <= 59 and 0 <= self.sec <= 59:
            return True
        else:
            return False
    """

    def tostring(self):
        timestr = str(self.hr) if self.hr > 9 else "0" + str(self.hr)
        timestr += ":"
        timestr += str(self.min) if self.min > 9 else "0" + str(self.min)
        timestr += ":"
        timestr += str(self.sec) if self.sec > 9 else "0" + str(self.sec)
        return  timestr

    def isLaterThan(self, aTime):
        if self.hr > aTime.hr:
            return True
        elif self.hr == aTime.hr:
            if self.min > aTime.min:
                return True
            elif self.min == aTime.min:
                if self.sec >= aTime.sec:
                    return True
        return False

    def __str__(self):
        return self.tostring()


def strtoTime(sub):
    t = Time()
    hr, min, sec = sub.split(":")
    t.hr = int(hr)
    t.min = int(min)
    t.sec = int(sec)
    return t

file = "/Users/hanson/Desktop/PBC/PPT/part3/Data/a9hFZVIQEeiR6g55Hcwzvg_6cb00730521011e8b326d555fde3a78c_midterm2.csv"
fh1 = open(file, "r", newline='', encoding='utf-8')
csv1 = csv.DictReader(fh1)
cname1 = csv1.fieldnames

submit1, submit2 = input().split()

submit1 = strtoTime(submit1)
submit2 = strtoTime(submit2)

result1 = {"Accepted":0, "Compile Error":0, "Runtime Error":0, "Time Limit Exceed":0, "Wrong Answer":0}
result2 = {"Accepted":0, "Compile Error":0, "Runtime Error":0, "Time Limit Exceed":0, "Wrong Answer":0}
result3 = {"Accepted":0, "Compile Error":0, "Runtime Error":0, "Time Limit Exceed":0, "Wrong Answer":0}
result4 = {"Accepted":0, "Compile Error":0, "Runtime Error":0, "Time Limit Exceed":0, "Wrong Answer":0}

for aline in csv1:
    sub = strtoTime(aline[cname1[6]])
    if sub.isLaterThan(submit1) and submit2.isLaterThan(sub):
        if int(aline[cname1[2]]) == 1:
            result1[str(aline[cname1[3]])] += 1
        if int(aline[cname1[2]]) == 2:
            result2[str(aline[cname1[3]])] += 1
        if int(aline[cname1[2]]) == 3:
            result3[str(aline[cname1[3]])] += 1
        if int(aline[cname1[2]]) == 4:
            result4[str(aline[cname1[3]])] += 1

fh1.close()
list1 = list(result1.values())
list2 = list(result2.values())
list3 = list(result3.values())
list4 = list(result4.values())

print(*list1, sep=" ", end=";")
print(*list2, sep=" ", end=";")
print(*list3, sep=" ", end=";")
print(*list4, sep=" ", end=";")
