# ASSIGNMENT 6

## Difference Between Asynchronous Programming and Synchronous Programming
In synchronous programming, if an event occurs, users must wait while the page loads the response. Therefore, the operations takes place sequentially.
This behaviour means that long-runnning operations are "blocking" or frames or blocks of data are sent. Unlike Asynchronous Programming, its antithesis,
user can still proceed with their activities while an event is occuring. Different than its former, data are transmitted using bytes or characters.

## Event-Driven Programming
Event-Driven Programming is an approach in which code is written to respond to events. The flow of the program depends upon events. An example of this
would be is when a key/click has been pressed. It consists of designing programming language that partly depends on user interaction to control program execution.

## Implementation of Asynchronous Programming in AJAX.
By using AJAX, the user's request will be processed while the user can still do their activity on the page. This means that the page won't reload to wait for the response.
AJAX (Asynchronous JavaScript and XML) is aimed to create
better and faster interactive web apps by combining several programming tools.
The process will occur as follows:
1. An event occurs on a page
2. Javascript will then create an XMLHTTPRequest object
3. That object will continue to send request to the web server
4. The server processes the responds and sends a response back to the client
5. Javascript reads the response and do the appropriate action depending on the event

## Implementation
