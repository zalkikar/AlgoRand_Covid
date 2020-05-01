# AlgoRand_Covid
Data Project on COVID-19 survey transactions on the Algorand Blockchain in Python via PureStake API.

[IReport-Covid](https://ireport.algorand.org/en) leverages the Algorand blockchain to provide anyone with the means to inform their community and world-at-large of their experience with COVID-19 in a timely and anonymized way. Here I demonstrate how to scrape and process IReport-Covid survey data from the Algorand blockchain in Python and begin analyzing the data. 

* The Algorand_coviddata.ipynb notebook is a demo of bulk survey transaction scraping from the Algorand mainnet via PureStake API and the py_algorand.py script
* The Algorand_process.ipynb notebook is a demo of basic survey data processing.
* The Algorand_eda.ipynb notebook is a demo of basic exploratory data analysis with the processed data.

After cloning, navigate to the local repo directory in your terminal and run notebooks cell by cell in the Jupyter IDE by typing '''python jupyter notebook''' to start. Otherwise, in your terminal run ipython '''python ipython''' and then '''python %run notebook_name.ipynb'''

Some Prelim Stats as of April 29th 2020:

1272 surveys with information

From 1259 valid responses : 61.48% reported being quarantined

From those that reported being quarantined 68.6% left temporarily

From 164 people who are symptomatic
* 6.1% got care at the doctor's office
* 3.05% got care at a walk in clinic
* 7.32% got virtual care
* 4.27% got care at the hospital/ER
* 46.95% reported a fever
* 67.07% reported a cough
* 34.15% reported difficulty breathing
* 67.07% reported fatigue
* 57.32% reported sore throat