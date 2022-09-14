## Link to Heroku App

Heroku App: https://assignment-2-pbp.herokuapp.com/
Catalog Page: https://assignment-2-pbp.herokuapp.com/katalog/

## MVT Diagram and How Its All Interlinked

The diagram above containts the client request to the django web application and its response. It is also called the workflow of an MVT(Model-View-Template) diagram. 

1. Firstly, a user will send a request to the server through a browser. 
2. Then, Django will receive the request and will be put through urls.py, urls.py contains the URLS a user will request for. 
3. After being processed through urls.py it is then forwarded into views.py for the corresponding response/functions to the proccesed request, a view fetches data from models and renders a template. 
4. Next, if the request requires any process that includes databases, views.py will query/fetch necessary data from models.py for the particular request, which then the result will be return to views.py. 
5. Lastly, views.py will render the HTML file which is defined in the template and show data acquired. This then will be returned to the user as a response.

## Why We Use Virtual Environments?

While it is not required, it is recommended to create and execute a Django application in a separate enviroment(virtual enviroment). Python has a tool called virtualenv that creates an isolated Python environment, we will  be use it to create our virtual environment for our Django application. This isolated environment isolates the package and dependencies specifically from our application. This is to deter the possibility of other versions of packages or dependencies in our computer conflicting with the ones from our application by avoiding installing Python packages globally. Therefore, the virtual envorinment is used to manage Python packages for different projects.

## Implementation

Step 1: Create a function on views.py
<img width="383" alt="Screen Shot 2022-09-15 at 6 33 50 AM" src="https://user-images.githubusercontent.com/101589777/190280746-d6f893fa-7970-4c3c-9662-8b189652b588.png">
First, In the beginning of the file we imported the CatalogItem class from models.py. This class will be used to retrieve data from the database. Next, we create a function on views.py that is capable of querying into models and returning the date into the HTML file. This function accepts request as its parameter, request in this context are HttpRequest from the user's browser. This function will then retrieve all the data from CatalogItem, then put into the variable context as a dictionary with key-value pair. Lastly, it will return a the render with parameter request, the html file, and the context variable to map data to the html file.

Step 2: Create a routing in urls.py
<img width="323" alt="Screen Shot 2022-09-15 at 6 51 15 AM" src="https://user-images.githubusercontent.com/101589777/190282365-dec7787e-0c9b-4a21-8823-ffcefc01e2b7.png">
