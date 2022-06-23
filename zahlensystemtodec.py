def umrechnung(num_in, zahlens):
    hex_conv = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
    num_out = 0
    num_in = num_in[::-1].lower()
    for index, number in enumerate(num_in):
        try: number = int(number)
        except ValueError:
            number = hex_conv[number]
        number = number * (zahlens ** index)
        num_out += number
    return num_out           



def main():
    num_io = input("Gimme number.\n>")
    zahlens_io = int(input("Gimme zahlensystem.\n>"))
    num_dec = umrechnung(num_io, zahlens_io)
    print(num_dec)

if __name__ == "__main__":
    main()
