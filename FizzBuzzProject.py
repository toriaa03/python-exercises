# def fizzbuzz_project(max_number):
#     for num in max_number(1, 101, 3):
#         print('Fizzbuzz')
#     elif 100 % 5
#         print('Fizz')

# fizzbuzz_project(100)




def fizz_buzz(max_num):
    for num in range(1, max_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

fizz_buzz(100)