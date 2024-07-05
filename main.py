import math



def factorial():
    s = ["выход",'exit',"close","закрыть"]
    while True:
        n = input()
        if n.lower() in s:
            break
            
        else:
            print(math.factorial(int(n)))








if __name__ == '__main__':
    factorial()