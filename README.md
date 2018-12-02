Py Me Up, Charlie
Background

Well... you've made it!

It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this homework assignment, you'll be using the concepts you've learned to complete 2 Python Challenges, PyBank and PyPoll. Both of these challenges encompasses a real-world situation where your newfound Python scripting skills can come in handy. These challenges are far from easy so expect some hard work ahead!

Before You Begin

Create a new GitHub repo called python-challenge. Then, clone it to your computer.

Inside your local git repository, create a directory for both of the Python Challenges. Use folder names corresponding to the challenges: PyBank and PyPoll.

Inside of each folder that you just created, add a new file called main.py. This will be the main script to run for each analysis.

Push the above changes to GitHub.

PyBank

Revenue

In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset

The total net amount of "Profit/Losses" over the entire period

The average change in "Profit/Losses" between months over the entire period

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in losses (date and amount) over the entire period

As an example, your analysis should look similar to the one below:

Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

