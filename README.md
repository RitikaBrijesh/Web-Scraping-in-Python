# Python-Web-Scraping

In this task I have scraped hundred of urls and displayed the following data
1. Product Title
2. Product Image URL
3. Price of the Product
4. Product Details

if the url is not found simply print {url} is not available. 

Here is the approach I followed to achieve this goal
In Step 1, I selected one of the country and ASIN values from the CSV file.
STEP 2: Using the BS4 module, I fetched the required data from the respective url.
STEP 3: The resulting data is stored in a dictionary.
STEP 4: I used the json module to convert this list of dictionary entries into a json file (output.json).

STEP 5: The resultant data has been stored in a MySQL datab
