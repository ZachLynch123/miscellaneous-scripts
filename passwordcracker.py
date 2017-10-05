import random
import time

password = ""
attempted_password = ""
list_of_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in range(0, random.randint(10, 25)):
    password += list_of_chars[random.randint(0, 20)]


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print "The function {.__name__} took {:.15f} seconds to finish.".format(func, time.time() - start)
        return result
    return wrapper


@timeit
def solve_password(word):
    global attempted_password
    for character in word:
        for entry in list_of_chars:
            if character == entry:
                attempted_password += character
                print(attempted_password)
                continue
    return attempted_password

print "The password: {0:}\nLength of password was: {1:}\nIs correct? : {2:}".format(solve_password(password),
                                                                                    len(password),
                                                                                    attempted_password == password)