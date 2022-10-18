def prime_checker(num):
    counter = 0
    loop = True
    prime_result = 0
    num_divisible = []
    while loop:       
        counter += 1
        prime_result = num % counter
        if num == 1:
            print("Not")
            loop = False
        elif prime_result == 0:
            num_divisible.append(counter)
            if len(num_divisible) == 3:
                print("Not")
                loop = False
            elif prime_result == 0 and num / counter == 1:
                print("Prime")
                loop = False

user_num_input = int(input("Check number if prime:\n"))
prime_checker(num = user_num_input)

