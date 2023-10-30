def monies():
    """function to get and validate user input """

    val = input("Value: ")

    if val.isdigit():
        return round(float(val), 2)
    else:
        print("Please enter a valid value!")
        return monies()


def client_information():
    """
    function to get client's information
    return index [{0:name, 1:address, 2:mortgage_price}]
    """

    name = str(input("Client's Name:\t"))
    address = str(input("Clients' Address\t"))

    return {"Name": name, "Address": address, "Property price": monies()}


def payment_percentage(property_price):
    """"
    Function to calculate the Payment Percentage
    """
    pprice = property_price
    payment_amount = None

    if pprice <= 500_000:
        payment_amount = .05 * pprice

    if 500_000 <= pprice < 1_000_000:
        payment_amount = (pprice * .05) + ((pprice - 500_000) * .05)

    if pprice > 1_000_000:
        payment_amount = (pprice * .2)

    total_amount = (payment_amount/pprice) * 100

    return round(total_amount, 3)


def down_payment(purchase_price, payment_percent):
    """
    Calculate Down payment amount
    """
    return (purchase_price * payment_percent) / 100


def insurance_rate(_percentage):

    if 5 < _percentage <= 10:
        return 4
    if 10 < _percentage <= 15:
        return 3.1
    if 15 < _percentage <= 20:
        return 2.8
    else:
        return 1


def insurance_cost(pp, dp):
    """
    Calculate Down payment amount
    dp = down payment
    pp = property price
    """












