class Flight:
    def __init__(self, flight_type):
        self.flight = flight_type

    def calculate_price(self):
        if self.flight == '737':
            return 20000
        elif self.flight == '747':
            return 50000


if __name__ == '__main__':
    attempt = 0
    while attempt != 3:
        flight_number = input("Please Enter the FLight number 737 or 747:  ")
        if flight_number != '747' and flight_number != '737':
            print("Wrong Attempt")
            attempt = attempt + 1
        else:
            break
        if attempt == 3:
            print("Too many atttempts, shutting down")
            exit()

    flight = Flight(flight_number)
    price = flight.calculate_price()
    print(f"The price of the selected flight is {price} ")
