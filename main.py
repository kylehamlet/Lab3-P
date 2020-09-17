#Author Kyle Hamlet kjh6064@psu.edu    
#Collaborator Ethan Moyer epm5482@psu.edu
#Collaborator Qikun Xuan qzx5031@psu.edu
#Collaborator Greg Dorazio gmd5474@psu.edu
#Section 5
#Breakout 11

def sum_n(n):
  if (n >= 1):
    return n + sum_n(n-1)
  else:
    return n

def print_n(s,n):
  if (n >= 1):
    print(s)
    print_n(s,n-1)
  else:
    return 0

def run():
  n = int(input("Enter an int: "))
  s = str(input("Please enter a string: "))
  print(f"The sum is {sum_n(n)}")
  print_n(s,n)

if __name__ == "__main__":
  run()