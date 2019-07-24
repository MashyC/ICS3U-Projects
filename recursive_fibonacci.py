def fib(n):
  if n==1 or n==0:return n
  else:return fib(n-1)+fib(n-2)

def main():
  try:
    val = int(input("Term #: "))
    if val<0:
      print("Positive numbers only!")
      main()
    print("The", str(val)+"th term of the Fibonacci Sequence is", fib(val))
  except ValueError:
    print("Only integers please!")
    main()

main()