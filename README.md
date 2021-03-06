## A simple Python script to scrape the results from the delta site

This script scrapes the semester results hosted on the delta server.
The original site for checking results is [here](https://delta.nitt.edu/results/checkResult.html)

### Requirements
- python 3
- requests
- bs4 (BeautifulSoup)
- PTable (PrettyTable)

### Usage
1. Download this whole repository
2. Install the requirements given above
    ```bash
    pip install -r requirements.txt
    ```
3. Change your directory to the root folder
4. Run the following command
```bash
python scrape_it.py -r <your_roll_number>
```
Enter your password in the hidden prompt and hit enter.

Also
```bash
python scrape_it.py -h
```
can be used to display the help message to use this script.

### Other info
This is just a small side project done by me for fun.
Please feel free to contribute to this and improve this repository if possible by sending pull requests.
