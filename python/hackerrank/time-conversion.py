def timeConversion(s):
    c_time = s[0:2]
    if(s[-2] == "A"):
        if c_time == "12":
            return "00"+s[2:-2]
        return s[:-2]
    else:
        if c_time == "12":
            return s[:-2]
        return str(int(c_time)+12) + s[2:-2]