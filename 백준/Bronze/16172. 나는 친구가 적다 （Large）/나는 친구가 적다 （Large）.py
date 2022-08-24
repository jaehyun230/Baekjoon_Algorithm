import re

if __name__ == "__main__":
    s = input()
    k = input()
    t = re.sub('[0-9]','',s)
    if k in t :
        print('1')
    else :
        print('0')