# FetchTakeHomeAE

For part one, see the DataModel.jpeg file in home directory of the repository. Notes are included within the model. The idea of the design is to build tables per object with sub objects having their own tables as well to reduce duplicity. I have dropped fields that don't seem useful and have held onto a few precalculated fields as I think they can often be useful.

For part two, the queries are saved in the queries directory and labeled by which question they would answer if the data model were to be built, assuming sufficient data cleaning had occurred.

For part three, there are a few (not-production-ready, surely) python scripts to assess data quality in the data quality folder. There are also copies of the json files there. I decided to separate them out for ease of thinking, but if I were to put this into production, I would modularize the various data quality tests and accept a file argument. The tests are to ensure clean (free from duplicates and errors where possible), consistent (standard formatting), logical (speaks for itself ironically), and comprehensive. As this is not a full-blown assessment, per the instructions, I will not have found or checked everywhere, but the main things I did do are as follows:

- Check primary keys for uniqueness, existence in all rows, alphanumeric qualities
  - I found that not all user rows had unique IDs
- Check numeric columns for positive or 0 numeric values
  - some receipts don't appear to have items, not sure if this is a valid state.
- Check date columns for valid dates
  - Happy to report these look good where they aren't null, though they are in unix-ms...and the dates look fairly stale (2021?)
- Get a sense of data types
  - Some alphanumeric columns in the brands.json file have special characters that could cause issues.
- Get a sense of null values by column
  - some date columns will null values would be better served set to a logical date. For example lastlogin as createddate if no additional logins.
- Check for valid state codes and roles
   - I found that roles include "fetch-staff", which was not listed in the outline as a potential value
- Check out "receipt items"
   - These were really messy, there are a number of columns indicative of price and quantity as an example.
- Other
  - I did also manually look around in the json files a little bit, and I found a lot of test data. I am also confused why receipt items map to cpg collections and not to brands
 
For part four, see the message.txt file in the home directory of the repository. Of course, it is addressed to Wes, and I would like to have coffee with him, but I am quite sure he would not be the stakeholder for this data set.
