#!/usr/bin/env python3

import requests
from warnings import catch_warnings, filterwarnings
from bs4 import BeautifulSoup

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
        self.response = "\nRoll  Number: " + self.postData["uname"]

        # For each table row, we now process
        for tr in table.find_all('tr'):
            self.response += "\n"

            # If there is a header
            for th in tr.find_all('th'):
                self.response += th.text + "\t"

            # For each data(column) in this row, add it to the response
            for td in tr.find_all('td'):
                self.response += td.text + "\t"

        # Print the GPA and the CGPA on separate lines
        gpa_data = soup.find_all('span', {'class', 'gpa'})
        for gpa in gpa_data:
            self.response += "\n" + gpa.text


    def print_results(self):
        """Function to print the data on the terminal"""
        self.__fetchData()
        self.__parseFetchData()
        print(self.response)
