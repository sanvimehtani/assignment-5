lower = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))
n = int(input("Enter number:"))
for i in range(lower, upper+1):
    if i % n == 0:
        print(i)
