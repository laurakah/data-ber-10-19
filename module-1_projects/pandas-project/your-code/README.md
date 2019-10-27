# Data Cleaning with Pandas and Numpy
Goal: cleaning the [global shark attacks data set](https://www.kaggle.com/teajay/global-shark-attacks/version/1#GSAF5.csv) and export the clean data into a csv file.

## Inspection of the data set
After the initial import I am inspecting the unprocessed data set by
* having a look at the dataframe's head to see columns, index, values
* inspect the data set's column names
* examine the dtypes of the different column names
* checking the percentage of missing values for each column
* examine values held by every column, counting unique values per column

## Verifying assumptions based on inspection of the data set
* checking if "pdf" is contained in "href" so we can drop "href" (most of the links are dead anyway and one can easily find the pdf's over their names via e.g. Google)
* check if the Case Number is contained in the pdf file name
* check if Case Number.1 and Case Number.2 are identical before dropping them
* checking if "original order" column contains related numbers starting from 0 so we can use the column as an index column

### Conclusions: 
1. Some column names contain spaces after the name. I am going to fix this to improve processability and reduce key errors.
2. The percentage of missing values in the columns "Age" and "Species" are above 40%, which could mean that they do not provide meaningful information depending on the type of data they store. I am not going to drop them because the missing values don't affect the information held by the non missing values which are still meaningful.
3. All pdf names are contained in the corresponding href column so we can drop the href column safely.
4. ~ 98% of the case numbers are contained in the pdf name so we can safely drop the case number column.
5. Case Number.1 is identical to Case Number.2 so we can drop both columns since we already know that the case number is contained in the pdf file name which we are keeping in the data set.
6. The value count for unique values in "original order" column does not match the length of the data set. This means that there are either duplicate or missing values in the "original order" column so we won't use is as an index column. Due to the structure of the data set and the differently formated values in some rows I am assuming that this data set is a conglomerate of different data sets on the topic of shark attacks on humans. The column "original order" in this context can be interpreted as the order in which these different data sets were added to this data set. Based in this assumption I consider the "original order" column as not meaningful information and I am going to drop it. 

## What I am going to do to clean this data set
### Removing duplicate and unrelated information and renaming columns
1. removing spaces after the labels "Sex" and "Species" on "Sex " and "Species " columns
2. remove the "Case Number" column because the information is already stored in the "pdf" column inside the file name
3. removing columns "Case Number.1" and "Case Number.2" because they are duplicates from "Case Number"
4. removing columns "Unnamed: 22" and "Unnamed: 23" because they don't contain meaningful information
5. removing columns "href formula" and "href" because of duplicate information to "pdf" - the pdf files can still be found via Google by file name and most of the links in href are dead anyways
6. removing "year" column because the information is already present in the date column
7. removing column "original order" because it does not contain meaningful information and can't be used as an index column

### Cleaning values in columns
1. remove non numeric values from "Age" column
2. removing unrelated/non activity values from "Activity" column
3. removing quoting characters from values in "Activity" column
4. removing non name entries from the "Name" column: "2 males", "male", non alphabetical values, etc. 
5. capitalize values in the columns "Name", "Location", "Area", "Activity", "Injury", "Species"

### Reshaping and combining columns
1. sum up "M", "F" and "O(ther)" values in "Sex" table
2. combining "Date" and "Time" column into a "Datetime" column, replacing/processing missing values
3. group the values "Boat" and "Boating" in the "Type" column into "Boating" because the meaning should be the same
4. change "Invalid" values into np.nan values inside of "Type" column

### Changing dtypes of columns
1. change value types in "Age" column to float
2. replacing "Fatal (Y/N)" with boolean values
3. converting new "Datetime" column into datetime object

### Processing the entire data set
1. check for duplicate rows 
2. check for rows with less than 4 valid values inside
3. writing cleaned data to a csv file

## What the data set's data types should look like after the clean up
Column Name | Value dtype
------------ | -------------
Datetime | datetime
Type | object
Country | object
Area | object
Location | object
Activity | object
Name | object
Sex | object
Age | float
Injury | object
Fatal (Y/N) | bool
Species | object
Investigator or Source | object
pdf | object

## Difficulties and Learnings
1. **Context:** Cleaning a data set without having information about the further processing is quite difficult. I found it hard to decide how to process specific columns without knowing which information are going to be relevant/important in the process of analysing this data und what questions should be answered.
2. **Prioritizing:** Since the name of the victim should not be incredibly relevant when processing this data set I am not going to spend a lot of time cleaning up values which could contain values other than names by using regular expressions – because I don't know anything about the specific questions that are going to be answered during the analysis of the data set.
3. **Formatting and mixed value types:** Processing the date column appears to be quite difficult in this case. Since there are so many non numeric values and unprecise time spans I decided to replace these values with a pd.nat. If the date column is going to be extremely relevant in the process of further processing of the data set It would be a bad idea to just 'guess' the dates on the basis of inconsitent time formats or description strings. If the date column is not going to be important in the further processing, missing date values won't bother.
4. **Grouping data:** For me the values "Boating" and "Sea Disaster" in the "Type" column don't go together with the "Provoked" and "Unprovoked" typing because of being answers to two different questions. I would have prefered to seperate these Types into two different columns. But since I am not the data engineer in this case I left them as they were and only grouped up the similar values.
5. **Order of cleaning steps:** It is useful to check for duplicate rows in the data set before processing anything else because we are probably going to maipulate the data set in a way which will unintentionally produce a few duplicate rows. These rows should not be dropped as long as they have not been duplicates in the beginning.
