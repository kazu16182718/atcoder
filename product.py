def check(list):
    if list[0]*list[1] % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def main():
    l=[]
    hoge=input()
    for i,num in enumerate(hoge.split(" ")):
        l.append(int(num))

    print(check(l))
    
main()