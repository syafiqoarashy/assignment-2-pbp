# ASSIGNMENT 2

## Link to Heroku App!

Heroku App: https://assignment-2-pbp.herokuapp.com/

Catalog Page: https://assignment-2-pbp.herokuapp.com/katalog/

## _MVT Diagram_ and How Its All Interlinked

![diagram](https://user-images.githubusercontent.com/101589777/190297274-eab2da6e-f7f9-4680-a126-6e210b5ae3f2.png)

The diagram above containts the client request to the django web application and its response. It is also called the workflow of an MVT(Model-View-Template) diagram. 

1. Firstly, a user will send a request to the server through a browser. 
2. Then, Django will receive the request and will be put through _urls.py_, _urls.py_ contains the URLS a user will request for. 
3. After being processed through _urls.py_ it is then forwarded into _views.py_ for the corresponding response/functions to the proccesed request, a view fetches data from models and renders a template. 
4. Next, if the request requires any process that includes databases, _views.py_ will query/fetch necessary data from _models.py_ for the particular request, which then the result will be return to _views.py_. 
5. Lastly, _views.py_ will render the HTML file which is defined in the template and show data acquired. This then will be returned to the user as a response.

## Why We Use _Virtual Environments_?

While it is not required, it is recommended to create and execute a Django application in a separate environment(virtual environment). Python has a tool called virtualenv that creates an isolated Python environment, we will  be use it to create our virtual environment for our Django application. This isolated environment isolates the package and dependencies specifically from our application. This is to deter the possibility of other versions of packages or dependencies in our computer conflicting with the ones from our application by avoiding installing Python packages globally. Therefore, the virtual envorinment is used to manage Python packages for different projects.

## Implementation

Step 1: Create a function on _views.py_

<img width="383" alt="Screen Shot 2022-09-15 at 6 33 50 AM" src="https://user-images.githubusercontent.com/101589777/190280746-d6f893fa-7970-4c3c-9662-8b189652b588.png">

First, In the beginning of the file we imported the CatalogItem class from _models.py_. This class will be used to retrieve data from the database. Next, we create a function on _views.py_ that is capable of querying into models and returning the date into the HTML file. This function accepts request as its parameter, request in this context are HttpRequest from the user's browser. This function will then retrieve all the data from CatalogItem, then put into the variable context as a dictionary with key-value pair. Lastly, it will return a the render with parameter request, the html file, and the context variable to map data to the html file.

Step 2: Create a routing in _urls.py_

<img width="323" alt="Screen Shot 2022-09-15 at 6 51 15 AM" src="https://user-images.githubusercontent.com/101589777/190282365-dec7787e-0c9b-4a21-8823-ffcefc01e2b7.png">

In step two, we need to create a routing that maps the function from _views.py_. Firstly ofcourse, we must import the _show_katalog_ function from _views.py_. Afterwards, we create a new path in url patterns with the name of our HTML page and the function.

Step 3: Mapping the Data

<img width="466" alt="Screen Shot 2022-09-15 at 7 04 19 AM" src="https://user-images.githubusercontent.com/101589777/190283529-06f37796-9e2f-4513-8420-6479ce27d369.png">

To map the data, first we open the HTML file we created in our templates folder. Create a loop in our table that iterates over _list_item_ as our container from the context variable. Then, change the content of the HTML file accordingly to call the specific variable/attribute name of the object in the container to call the data. In this, we use Django's template syntax to map the data that has been rendered and display it on the HTML page.

Step 4: Heroku Deployment

To deploy to Heroku, firstly we create a file called _Procfile_ that will be used by Heroku to read the log activity of our application. Since, the _Procfile_ file has already been provided in our template, we will be using that. Afterwards, we have to create a file named _dpl.yml_, this is used by GitHub Actions to carry out the deployment by runner. A few configurations must also be added to our _settings.py_ file but it is also already done by the template. Futhermore, fetch your Heroku API Key and application name. In our GitHub repository, open the Secrets section and add a new repository secret variable for our deployment. These variable will be called HEROKU_API_KEY that contains the API Key and HEROKU_APP_NAME that contains the application name. After storing those variables, don't forget to open re-run the failed workflow. Now, the application is now accessible throuth the link.

# ASSIGNMENT 3

## Difference betweeen HTML, XML, and JSON

#### Each Definition

###### HTML

HTML (Hyper Text Markup Language) is a markup language that is used as the most basic building block of the Web. It's a set of markup symbols or codes used to display on the Internet. It defines the meaning and structure of web content.

###### XML

XML (eXtensible Markup Language) is also a markup language, but XML is used to store data and no predefined tags. A simple text-based format for representing structured information: documents, data, configuration, books, transactions, invoices, and much more.

###### JSON

JSON (JavaScript Object Notation) is a lightweight format used to store and transport data, a simple data interchange format. It is based on the JavaScript programming language and easy to understand and generate.

#### Differences

HTML is the outlier with the differences while XML and JSON is much more similar in use. HTML is more used to structure and design where things are supposed to be placed on a page. Just like their definitions both XML and JSON are used as data transfer and storage formats. Now the difference between XML and JSON is that XML is based on SGML while JSON is based on JavaScript.

| HTML | XML | JSON |
| --- | --- | --- |
| Uses predefined tags | User defined tags | - |
| Static | Dynamic | Dynamic |
| Derived from SGML | Derived from SGML | Derived from JavaScript | 
| Comments are supported | Comments are supported | Comments are not supported |
| Used to display data | Used to store data | Used to store data |
| HTML does not carry data, it only displays it | XML carries the data | JSON carries the data |
| Closing tags are not necessary | Closing tags are necessary | It doesn't use end tag |

## Why We Need Data Delivery

Data delivery is very important in platform-based development. The use of data is very prominent and ofcourse we need data to be displayed in our web pages. If there was no HTML file, then there would be no way for the Django application to display the data we've created. If there was no XML/JSON file, there would be no place to store and carry out the data. If there were no data delivery, the web page we created for this assignment would be futile and empty. The World Wide Web is about communication between web clients and web servers. It does an HTTP Request-Response cycle which is apart of the Data Delivery protocol. As we see, Data Delivery is _essential_ to be implemented on a platform.

## How It Was Completed

Firstly we create a new app called _mywatchlist_ from our Django Project using
``` python
python3 manage.py startapp mywatchlist
```
After creating the app, open _settings.py_ and add our new app _mywatchlist_ in the _INSTALLED_APPS_ list.

<img width="272" alt="Screen Shot 2022-09-22 at 12 10 45 AM" src="https://user-images.githubusercontent.com/101589777/191568349-bc2587eb-6d43-49ef-9e11-ec29ec5bb20e.png">

Afterwards, we need to implement routing to our new app so that it can be accessed. We can do this by registering _mywatchlist_ application into _urls.py_. This will be the code implemented in _urls.py_

<img width="506" alt="Screen Shot 2022-09-22 at 12 16 42 AM" src="https://user-images.githubusercontent.com/101589777/191569464-30b1b6e8-2b00-4809-b158-225bb974174e.png">

Now we move into the _models.py_ file in our application folder. Create a new class called _MyWatchList_, within it create the attributes as requested:

<img width="406" alt="Screen Shot 2022-09-22 at 8 02 15 AM" src="https://user-images.githubusercontent.com/101589777/191635884-df0b1855-579f-4452-9e81-4a3acd07f436.png">

Continue by migrating the model schema into the local Django database with
```python
python3 manage.py makemigrations
```
and then deploy the created model schema into the local Django database with 
```python
python3 manage.py makemigrate
```

After that I create the JSON file containing the data for the application,

<img width="722" alt="Screen Shot 2022-09-22 at 8 07 15 AM" src="https://user-images.githubusercontent.com/101589777/191636369-f584f372-1c08-4bbb-bf39-822db930ac6a.png">

then I load the data with

```python
python3 manage.py loaddata initial_mywatchlist_data.json
```

Then I create a funciton inside the views.py that is supposed to render the web page along with the data I've created within the JSON file. Not only that, I also implement 4 other functions. The function is used to return data in XML/JSON Form with and without ID.

<img width="692" alt="Screen Shot 2022-09-22 at 8 10 43 AM" src="https://user-images.githubusercontent.com/101589777/191636712-6d4740f2-1791-4795-9ed1-98528ffc97a1.png">

We'll also fill in the html file according to the fields inside our _models.py_. In this one, I've modified the column for the watched to display icons depending on the boolean value.

<img width="722" alt="Screen Shot 2022-09-22 at 8 14 21 AM" src="https://user-images.githubusercontent.com/101589777/191637027-db4438fc-1028-4904-9c0b-63b89b6e5c51.png">

Then continue to implement the URL routing inside _urls.py_ for each path HTML, JSON, and XML. Then put the functions we created before in views into each respective url path.

<img width="570" alt="Screen Shot 2022-09-22 at 8 18 34 AM" src="https://user-images.githubusercontent.com/101589777/191637375-9d71f280-7d3f-4aa5-82e7-36f2198b8820.png">

Lastly we need to deploy it into Heroku, we've succesfully done that with last week assignment and because there we're using the same repository as the previous assignment. There is no need to implement deployment again. The Heroku app has been configured to automatically update depending on the latest commit. However, if we were to go through the steps again. We'd have to create an app in our Heroku account and fetch its app name and our account API key. Then create 2 new repository secrets containing those 2 stuff. Lastly, don't forget to rerun the failed deployment. Our app should be accessible now.

## Screenshots from Postman

###### HTML Variant

![image](https://user-images.githubusercontent.com/101589777/191459488-8eadcf14-ee5c-4ca9-9f46-2f0ea14cb7e1.png)

###### XML Variant

<img width="1435" alt="Screen Shot 2022-09-21 at 3 52 01 PM" src="https://user-images.githubusercontent.com/101589777/191460338-4b09926c-3c9e-493b-bd79-85a6c9e61d12.png">

###### JSON Variant

<img width="1435" alt="Screen Shot 2022-09-21 at 3 53 13 PM" src="https://user-images.githubusercontent.com/101589777/191460585-be7dcf55-f87e-4681-a889-021c898b3916.png">
