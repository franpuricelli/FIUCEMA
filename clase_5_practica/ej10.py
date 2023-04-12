import re
def get_substr(string):
    return re.findall("[@|&](.*?)[@|&]",string)

string = "afjdjfsjf@fsdfksdfk&skkdkdkd sdf @" 

print(get_substr(string))
