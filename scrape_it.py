#!/usr/bin/env python3

from scraper import ResultScraper as RS
from argparse import ArgumentParser
from getpass import getpass

def main():
    """main method"""
    parser = ArgumentParser(
            description='Fetch Student Results using Delta\'s server'
            )
    parser.add_argument(
            "-r",
            "--roll_number",
            dest="uname",
            help="NITT Rollnumber",
            type=str,
            required=True
            )
    # parser.add_argument(
    #         "-p",
    #         "--password",
    #         action='store_true',
    #         dest="pwd",
    #         help="Webmail or Octa Password",
    #         )
    args = parser.parse_args()
    

    if args.uname is None:
        print("Please enter roll number")
    else:
        password = getpass()
        if password is None:
            print("Please enter roll number and password again")
        else:
            data = dict()
            data['uname'] = args.uname
            data['pwd'] = password
            rCls = RS(data)
            rCls.print_results()

if __name__ == "__main__":
    main()
