# Marvel-Hero-Data

<h4> This is a REPL (Read-Evaluate-Print-Loop) application, which uses the API data of Marvel Cinematic Universe to fetch data based on user query </h4>

  <h4> How to run this application: (on console)</h4>
  
  1) Install the requirements using ```pip install -r requirements.txt```
  2) Then, run ```python3 main.py```
  3) Enter any query to get the results. Eg, enter ```iron``` to get results on Iron Man, Iron Clad, etc...
  4) While selecting choices (X, N, P) for exiting query or moving to next and previous pages respectively, make sure to enter the character and press ```enter``` on the console.

* This REPL app shows results in a paginated format based on the quantity of the available and relevat results.

* The app can take in multiple values without refreshing itself everytime a new query has been made.

* All possible unit test cases have been covered for this application in the unitTest.py file.

* Caching has been enabled for the API layer to reduce the workload of the overall application.

<h3> Images of the application </h3>

<h4> Image-1 </h4>

![Image - 1](https://github.com/vasupradharamac/Marvel-Hero-Data/blob/main/images/Terminal%201.png)

<h4> Image-2 </h4>

![Image - 2](https://github.com/vasupradharamac/Marvel-Hero-Data/blob/main/images/Terminal%202.png)

<h3> API Authentication: </h3>

To access the Marvel API data, the users have to get API keys and generate a md5 hash of timestamp, publicKey and private key.

In this app, the  ```hashlib``` library has been used to generate the md5 hash value of the timestamp and keys.
