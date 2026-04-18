n=int(input("Enter number of values: "))

x=[]
p=[]

print("Enter values of x: ")
for i in range(n):
  x.append(float(input()))

print("Enter probabilities: ")
for i in range(n):
  p.append(float(input()))

mean=0
for i in range(n):
  mean+=x[i]*p[i]

ex2=0
for i in range(n):
  ex2+=(x[i]**2)*p[i]

variance=ex2-mean**2
print("Mean= ",mean)
print("Variance= ",variance)
