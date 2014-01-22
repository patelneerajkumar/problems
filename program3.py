
'''this is my program'''
def  myfunction():
	n=60085
	list=[]
	list1=[]
	for m in range(2,n):
		count=0
		for i in range(1,m):
			if(m%i == 0):
				count=count+1
		if(count == 1):
			list.append(m)
	print list
	a=len(list)
	print a
	print list[a-1]

if __name__=='__main__':
	myfunction()	 

'''varun code problem 3.......................

def largest_prime():
        num = 600851475143L
        new_num = num
        largest_prime = 0
        counter = 2
        while(counter * counter <= new_num):
                if(new_num%counter ==0):
                        new_num = new_num / counter
                        largest_prime = counter
                else:
                        counter += 1
        if new_num > largest_prime:
                largest_prime = new_num
        print largest_prime

if __name__ == '__main__':
        largest_prime()'''
