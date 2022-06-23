def calc_rest(num_in, zahlensystem_in):
    rest_out = num_in % zahlensystem_in
    num_in = (num_in - rest_out) / zahlensystem_in
    return rest_out, num_in

def main():
    print_array_rest = []
    print_array_num = []
    num_io = int(input("Gimme Number.\n>"))
    num_tmp = num_io
    zahlensystem = int(input("Gimme Zahlensystem.\n>"))
    while True:
        rest_tmp, num_tmp = calc_rest(num_tmp, zahlensystem)
        print_array_rest.append(int(rest_tmp))
        print_array_num.append(int(num_tmp))
        if num_tmp == 0:
            print(num_io)
            for i in range(0, len(print_array_num)):
                print(print_array_num[i], "\t", print_array_rest[i])
            break

if __name__ == "__main__":
    main()
