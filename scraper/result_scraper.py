#!/usr/bin/env python3

import requests
from warnings import catch_warnings, filterwarnings
from bs4 import BeautifulSoup
from prettytable import PrettyTable


class ResultScraper(object):
    """Class for scraping results
    
    This class contains all the methods for scraping the delta results page
    and then displaying the results on the terminal
    """

    def __init__(self, postData):
        """Constructor
        
        # Arguments
            postData - the user credentials to be posted to the server
        """
        self.postData = postData
        self.htmlText = None
        self.response = None

    def __fetchData(self):
        """Function to fetch data using a post request"""
        headers = dict()
        headers["referer"] = """https://delta.nitt.edu/\
                results/checkResult.html"""
        headers["host"] = "delta.nitt.edu"
        # ignore warnings due to avoiding SSL certificate verification
        with catch_warnings():
            filterwarnings("ignore")
            r = requests.post(
                "https://delta.nitt.edu/results/results.php",
                headers=headers,
                data=self.postData,
                verify=False
            )
        self.htmlText = r.text

    def __parseFetchData(self):
        """Function to parse the HTML text that has been obtained"""
        soup = BeautifulSoup(self.htmlText, 'html.parser')
        # Isolate the Table
        table_list = soup.find_all('table')

        if len(table_list) == 0:
            err_mess = soup.find_all('div', {'role', 'alert'})
            self.response = err_mess[0].text
            return

        table = table_list[0]

        # The table containing the details of grades
        self.t1 = PrettyTable()
        self.t1.title = "Roll Number: " + self.postData["uname"]

        # The table containing the detials of the GPA and CGPA
        self.t2 = PrettyTable()
        self.t2.title = "GPA details"

        sub_name = None
        # For each table row, we now process
        for tr in table.find_all('tr'):
            # If there is a header
            if len(tr.find_all('th')):
                self.t1.field_names = [th.text for th in tr.find_all('th')]
                sub_name = [th.text for th in tr.find_all('th')][1]

            else:
                # For each data(column) in this row, add it to the response
                self.t1.add_row([td.text for td in tr.find_all('td')])

        self.t1.align[sub_name] = "l"

        # Print the GPA and the CGPA as a separate table
        gpa_data = soup.find_all('span', {'class', 'gpa'})
        self.t2.field_names = ["GPA", "CGPA"]
        self.t2.add_row([gpa.text.split(":")[1] for gpa in gpa_data])

    def print_results(self):
        """Function to print the data on the terminal"""
        self.__fetchData()
        self.__parseFetchData()
        if self.response is not None:
            print(self.response)
        else:
            print(self.t1)
            print(self.t2)

    def save_to_file(self):
        """Function to save the data to file"""
        if self.t1 is not None and self.t2 is not None:
            with open(self.postData["uname"] + "_semester_results.txt", "w") as f:
                f.write(self.t1.get_string())
                f.write("\n")
            with open(self.postData["uname"] + "_semester_results.txt", "a") as f:
                f.write(self.t2.get_string())