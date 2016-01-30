# twitter
Sample twitter program to demonstrate the twitter API.  
Use it as a guide for your first programming assignment: writing a twitter sentiment analysis program

You will create a Python program named sentiment.py.  The program will

Prompt the user to enter two search terms.
Search the twitter stream for the first 1000 tweets that contain the first search term.
Calculate a sentiment score for the first search term
Search the twitter stream for the first 1000 tweets that contain the second search term.
Determine which search term currently has the most positive sentiment on twitter and print the results.
To search the twitter stream you will have to get OAuth 1.0 authentication credentials to use in your program.  To do this:

Create a twitter directory in the public_html directory of your home directory on www1.chapman.edu
Create a twitter account if you do not already have one.
Go to https://dev.twitter.com/apps and log in with your twitter credentials.
Click "create an application".  
- For the "Name" put  "Sentiment username"  where "username" is replaced with your actual Chapman username (this will make sure that all the names are distinct)
-  For the "Description" put anything you want.
-  For the "Website" put  put "https://www1.chapman.edu/~username/twitter/index.html" where "username" is replaced with your actual Chapman username
-  For the "Callback URL" put "https://www1.chapman.edu/~username/twitter/callback.html" where "username" is replaced with your actual Chapman username
Agree to the terms. 
On the next page,click the "Keys and Access Tokens" tab.
Scroll down to "Token Actions" and click "Create My  Access Token"
Copy your "Consumer Key (API Key)",  your "Consumer secret (API secret)", your "Access Token" and your "Access Token Secret" to use in your  sentiment.py application.
You can Read more about Oauth authorization at https://dev.twitter.com/docs/auth
