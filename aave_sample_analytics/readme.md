# Sample Analysis

Analysis of a project using a variety of data sources; only uses sources that allow real-time analysis. 

Total Value Locked: measuring the total dollar value locked in all smart contracts across the protocol. Gathered and charted in tvl.py
Outstanding Borrow: total value of assets borrowed in the protocol
Oustanding Collateral: total value of assets lent in the protocol 
Utilization: measures the percent of assets borrowed against collateral, calculated as borrow/collateral
Unique Users: total number of unique addresses that have interacted with the protocol 

## Infura/Alchemy API Keys

Some files include a line of code that connects to Infura or Alchemy nodes. I use the python-dotenv library to save environment variables.

You can read about python-dotenv [here.](https://pypi.org/project/python-dotenv/)