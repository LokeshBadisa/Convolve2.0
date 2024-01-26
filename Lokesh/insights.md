* Most of the people with 0 income have some of the columns as nan.
* People with country nan didn't do fraud which is not the case with other columns. -> If you use this property, you can remove another 3800 rows.
* Fraud accounts did do any transactions in middle of timeframes.
* 21847 datapoints from non-fraud have nan as first 79 transactions. Similarly, 129 datapoints from fraud.
* 21833 non-fraud have all transactions nan. 114 fraud have all transactions nan.
    -> Using this, removed 15315 rows for cleantrain.csv and 6632 rows for cleantest.csv
* others_42, others_43, others_44, others_45 can be removed. : High percent of nan around 99%
  * 