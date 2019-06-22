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
    parser.add_argument(
        "-s",
        "--save_result",
        dest="save_d",
        help="Save result to text file",
        action="store_true",
        required=False
    )
    args = parser.parse_args()
    if args.uname is None:
        print("Please enter roll number")
    else:
        password = getpass(prompt="Webmail or Octa Password: ")
        if password is None:
            print("Please enter roll number and password again")
        else:
            data = dict()
            data["uname"] = args.uname
            data["pwd"] = password
            rCls = RS(data)
            rCls.print_results()
            if args.save_d:
                rCls.save_to_file()


if __name__ == "__main__":
    main()
