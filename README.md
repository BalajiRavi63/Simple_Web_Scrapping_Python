# Simple_Web_Scrapping_Python
This is a simple and a small implementation of web scrapping which uses Python with Some Python Libraries like Requests, beautifulsoup, numpy and pandas. The Web Scrapping is done on IMDB Top Movies Link and the end outcome consist of a CSV File that consist of Name, Year it is released and its rating

**Program Flow:**

  1. Import the required libraries.
  2. Pass the URL That needs to be scrapped
  3. Using requests & BeautifulSoup, convert the obtained response into a HTML format and store it inside a variable.
  4. Based on the user requirment, create empty lists for storage of datas.
  5. Go to the URL, Inspect the page to see where the content that needs to be parsed is actually present 
  6. Assign a variable to the content that needs to be parsed.
  7. Using a for loop, iterate all the parsed content and as in when it gets iterated, append it to the previously created empty list.
  8. Using DataFrame, all the obtained variable is made into a Dataframe after which it can be either cleaned, converted to other format or published as a CSV for further processing.

**How to select which data to get from URL?**

 **1. Open URL Of your choice and right click on the webpage and click on Inspect Source.**
  
 **2. See which div element occupies your most of the content.**
 
 
 
  ![image](https://user-images.githubusercontent.com/51675975/114010582-dfed3500-9881-11eb-8ace-04b9451dc9f9.png)
 
 
 **3. Collapse each div element to go to the main content that contains the useful data**
 
 
  ![image](https://user-images.githubusercontent.com/51675975/114011425-d6b09800-9882-11eb-873f-4ee008b38ac5.png)
  
  
 **4. Navigate through the HTML till you see the content that you want to scrap from the webpage being highlighted.**
 
 
  ![image](https://user-images.githubusercontent.com/51675975/114011656-1d9e8d80-9883-11eb-9038-f1438e380634.png)
  
  
 **5. Note down the Tag associated with the content and the class name of the content and reference this class name and tag name to the python file.**
 
 
  ![image](https://user-images.githubusercontent.com/51675975/114012094-8980f600-9883-11eb-968b-9887498cd86b.png)
 
 
 **6. If needed make nessessary changes to the content that you'll be needing to scrap from the webpage and run the program.**
