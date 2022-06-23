def fib_rec(num_in, fib_cache = {1:1, 2:1}): 
    if num_in in fib_cache:
        return(fib_cache[num_in])
    else:
        rec_return = fib_rec(num_in - 1) + fib_rec(num_in - 2)
        if rec_return not in fib_cache:
            fib_cache[num_in] = rec_return
        return rec_return

def fib_iter(num_in, fib_cache = {1:1, 2:1}):
    for i in range(3, num_in + 1):
        fib_cache[i] = fib_cache[i - 1] + fib_cache[i - 2]
    return fib_cache[num_in]

def fib_iter_range(num_in, fib_cache = {1:1, 2:1}):
    for i in range(3, num_in + 1):
        fib_cache[i] = fib_cache[i - 1] + fib_cache[i - 2]
    return fib_cache


def mode():
    while True:    
        try:
            io_mode = int(input("Recursive (1), Iterative (2), Range (3)\n>"))
            if io_mode in [1, 2, 3]:
                return io_mode
            else:
                raise ValueError
        except ValueError:
            print("1, 2 or 3")
            continue
        except KeyboardInterrupt:
            print("\nbb")
            exit()

def main():
    curr_mode = mode()
    while True:
        try:
            user_val = int(input("Gimme Number\n>"))
            if user_val < 1:
                raise ValueError
        except ValueError:
            print("Positive integer plx")
            continue
        except KeyboardInterrupt:
            print("\nbb")
            exit()
        if curr_mode == 1:
            print(fib_rec(user_val))
        if curr_mode == 2:
            print(fib_iter(user_val))
        if curr_mode == 3:
            tmp_dict = fib_iter_range(user_val)
            for number in tmp_dict.values():
                print(number)

main()
