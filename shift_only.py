"""
def check(num_list):
    for n,i in enumerate(num_list):
        if float(i)%2==1:
            return 0
    return 1

def div_list(num_list):
    for n,i in enumerate(num_list):
        num_list[n]=str(float(i)/2)
    return num_list
    
def main():
    num=input()
    integer=input()
    integer = integer.split()
    count=0
    while check(integer):
        div_list(integer)
        count+=1
    print(count)
    
main()
"""
n=input()
integer=list(map(int,input().split()))
count=0
while all(num%2==0 for num in integer):
    count+=1
    integer=[num/2 for num in integer]
print(count)