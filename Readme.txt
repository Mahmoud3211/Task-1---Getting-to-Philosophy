###Task 1 - Getting to Philosophy:

to make an efficient wikipidea crawler the mission is divided into two functions , one to extract links from the pages and the other is to check if 
we reached the Philosophy article or not, so the main operation sequense is to save all the extracted links in a list by the extract_first_link functinon 
that extracts the HTML code from a URL then searchs for a div in he HTML code with id of (mw-content-text) this is where wikipidea saves the paragraph with 
the target link or the first link on the article, after that it looks for the (a) tage in the paragraph and extracts the url from it , this url is saved in list
and handed to the second function (search_target) , it checks it the link is the target link if it's not it continues the sequense unles we have reached a number of iterations that 
the users specifies as the maximum or the url was already found once and stored in the list, these two exception plus if the possibility of reaching a page with no links abort the program


note: the sleep time is set to 2 seconds because 0.5 seconds makes wikipidea blocks the operation
###Requirements
these libraries must be pre-installed:

time
bs4
requests
urllib


###Developed by :
 Mahmoud Nada

