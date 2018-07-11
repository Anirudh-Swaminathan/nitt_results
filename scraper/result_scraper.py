#!/usr/bin/env python3

import requests

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
        self.response = None

    def __fetchData(self):
        """Function to fetch data using a post request
        
        # Arguments
            postData - dictionary
                Data to be sent via POST request

        # Returns
            response - Response to the request
        """
        headers = dict()
        headers["referer"] = """https://delta.nitt.edu/\
                results/checkResult.html"""
        headers["host"] = "delta.nitt.edu"
        r = requests.post(
                "https://delta.nitt.edu/results/results.php",
                headers=headers,
                data=self.postData,
                verify=False
                )
        self.response = r.text

    def print_results(self):
        """Function to print the data on the terminal"""
        self.__fetchData()
        print("\n" + self.response)
