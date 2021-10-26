"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
import math
import sys


# replace this comment with your implementation of get_min_payment(),
# interest_due(), remaining_payments(), and main()
def get_min_payment(principal, annual_rate, years=30, payments_per_year=12):
    """Computes the minimum mortgage payment, A
    
    Args: 
        principal(int): the total amount of the mortgage
        annual_rate(float): the annual interest rate
        years(int): the term of the morgtage in years
        payments_per_year(int): the number of payments made per year
        
    Returns:
       A(float): the minimum mortgage payment
    """
    
    r = (annual_rate / payments_per_year)
    n = (years * payments_per_year)
    power = (1+r)** n 
    A = (principal(1+r)*power)/((1+r)**n-1)
    return math.ceil(A)
    
def interest_due(balance, annual_rate, payments_per_year):
    """Computes and returns the amount of interest due in the next payment, i
    
    Args:
        balance(int): the balance of the mortgage
        annual_rate(float): the annual interest rate
        payments_per_year(int): the number of payments made per year
        
    Returns: 
        i(float): the amount of interest due in the next payment
    """
    rate_per_payment = annual_rate / payments_per_year
    interest_due = balance * rate_per_payment
    return interest_due
       
    def remaining_payments(balance, annual_rate, target, payments_per_year):
        """Computes and returns the number of payments required to pay off the mortgage
        
        Args: 
            balance(int): the balance of the mortgage
            annual_rate(float): the annual interest rate
            target(int): the amount the user wants to pay per payment
            payments_per_year(int): the number of payments made per year
        
        Returns:
            Remaining(int): the number of payments to be made until the mortgate is paid off
        """
        
        remaining_payments = 0
        while balance > 0:
            interest = interest_due(balance, annual_rate, payments_per_year)
            payment = target - interest_due
            balance -= payment 
            remaining_payments += 1
            return returning_payments
           
           
    def main(principal, annual_rate, years=30, payments_per_year=12, target=None):
        """computes the minimum payment, displays the minimum payment to the user, sets the target payment to the minimum payment if the 
        user's target payment is equal to None, prints a statement if the user's target payment is lower than the minimum payment
        
        Args: 
            principal(int): the total amount of the mortgage
            annual_rate(float): the annual interest rate
            years(int): the term of the mortgage in years
            payments_per_year(int): the number of payments made per year
            target(int): the amount the user wants to pay per payment
            
        Returns: 
            min_payment(float): the minimum payment that can be made
        """
        min = get_min_payment(principal, annual_rate, years, payments_per_year)
        print(min)
        if target is None: 
            target = min
        if target < min:
            print(f"Your {target} is less than the {min} for this mortgage")
        else: 
            remain = remaining_payments(balance, annual_rate, target, payments_per_year)
            print(f'if you make payments of {target} you will pay off the mortgage in {total_payments} payments')

def parse_args(arglist):
    """Parse and validate command-line arguments.
    
    This function expects the following required arguments, in this order:
    
        mortgage_amount (float): total amount of a mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        
    This function also allows the following optional arguments:
    
        -y / --years (int): the term of the mortgage in years (default is 30)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
        -p / --target_payment (float): the amount the user wants to pay per
            payment (default is the minimum payment)
    
    Args:
        arglist (list of str): list of command-line arguments.
    
    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)
    
    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")
    
    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)