def prime_checker(num):
#counter is for dividing num until it reaches num value, loop for ending loop when #conditions met, prime_result for checking if modulo == 0, num_divisible list to #check if num has more than 2 divisible numbers
  counter = 0
  loop = True
  prime_result = 0
  num_divisible = []
  while loop:       
    counter += 1
    prime_result = num % counter
#this if num == 1 exception is only for num == 1
    if num == 1:
      print("Not")
      loop = False
#check if prime num has more than 2 divisible numbers
    elif prime_result == 0:
      num_divisible.append(counter)
      if len(num_divisible) == 3:
        print("Not")
        loop = False
#if counter reaches num value then num / counter == 1, and it is prime
      elif prime_result == 0 and num / counter == 1:
        print("Prime")
        loop = False

user_num_input = int(input("Check number if prime:\n"))
prime_checker(num = user_num_input)

