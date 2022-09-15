## Link to Heroku App

Heroku App: https://assignment-2-pbp.herokuapp.com/

Catalog Page: https://assignment-2-pbp.herokuapp.com/katalog/

## _MVT Diagram_ and How Its All Interlinked

The diagram above containts the client request to the django web application and its response. It is also called the workflow of an MVT(Model-View-Template) diagram. 

1. Firstly, a user will send a request to the server through a browser. 
2. Then, Django will receive the request and will be put through _urls.py_, _urls.py_ contains the URLS a user will request for. 
3. After being processed through _urls.py_ it is then forwarded into views.py for the corresponding response/functions to the proccesed request, a view fetches data from models and renders a template. 
4. Next, if the request requires any process that includes databases, views.py will query/fetch necessary data from models.py for the particular request, which then the result will be return to _views.py_. 
5. Lastly, _views.py_ will render the HTML file which is defined in the template and show data acquired. This then will be returned to the user as a response.

## Why We Use _Virtual Environments_?

While it is not required, it is recommended to create and execute a Django application in a separate enviroment(virtual enviroment). Python has a tool called virtualenv that creates an isolated Python environment, we will  be use it to create our virtual environment for our Django application. This isolated environment isolates the package and dependencies specifically from our application. This is to deter the possibility of other versions of packages or dependencies in our computer conflicting with the ones from our application by avoiding installing Python packages globally. Therefore, the virtual envorinment is used to manage Python packages for different projects.

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

