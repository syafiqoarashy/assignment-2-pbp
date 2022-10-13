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
1. Create a function on _views.py_ to display the data tasks in JSON form.

<img width="689" alt="Screen Shot 2022-10-13 at 11 29 34 AM" src="https://user-images.githubusercontent.com/101589777/195501814-9e52268c-9abc-48a9-9054-f304a810e7cf.png">

2. Create a routing in _urls.py_ for our new function.

<img width="562" alt="Screen Shot 2022-10-13 at 11 30 21 AM" src="https://user-images.githubusercontent.com/101589777/195501919-09b109c1-e7bb-46d2-99cc-ad1cb1029c1c.png">

3. Import JQuery Script

<img width="698" alt="Screen Shot 2022-10-13 at 11 33 03 AM" src="https://user-images.githubusercontent.com/101589777/195502286-8ee85885-be45-4f68-ba07-6a3ee760f1df.png">


4. Implement AJAX GET

<img width="311" alt="Screen Shot 2022-10-13 at 11 31 38 AM" src="https://user-images.githubusercontent.com/101589777/195502110-a5fc1f86-9652-449f-8a47-8f35d2580593.png">

<img width="469" alt="Screen Shot 2022-10-13 at 11 32 21 AM" src="https://user-images.githubusercontent.com/101589777/195502191-6723addf-5d89-411f-8078-a005a6c98c21.png">

5. Create for New Tasks

(I reused the new task from last assignment)

```
<div id="create_modal" class="fixed w-full min-h-screen items-center justify-center  z-50 inset-0 hidden">
        <div class="bg-[#F3F5F9] flex rounded-2xl shadow-2xl shadow-blue-500 max-w-3xl p-5 items-center">
            <div class="px-8">
                <div class="flex flex-row">
                    <h2 class="font-bold sm:text-3xl text-lg">Tell us what you're up to</h2>
                    <h2 class="font-extrabold sm:text-3xl text-lg text-[#0951A8]">.</h2>
                </div>
                <p class="text-sm mt-2">Add one of your to-do for today!</p>
                <form method="POST" action="" class="flex flex-col" id="task_form">
                    {% csrf_token %}
                    <input class="p-2 mt-4 mb-3 rounded-xl border border-white" id="title" type="text" name="title" placeholder="Title">
                    <p class="text-sm mb-2">Describe your task</p>
                        <textarea class="rounded-xl border text-black border-white mb-5" id="description" name="description"></textarea>
                    <button id="add_task" class="bg-[#0951A8] shadow-md mb-3 shadow-blue-500/50 rounded-xl text-white py-2 hover:scale-110 duration-500">New task</button>
                </form>
                {% if messages %}
                    <ul>
                        {% for message in messages %}
                            <li class="mt-4 text-center text-sm">{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}
                <div class="mt-4 grid grid-cols-3 items-center text-gray-500">
                    <hr class="border-gray-500">
                    <p class="text-center items-center">OR</p>
                    <hr class="border-gray-500">
                </div>
                <div>
                    <button class="bg-white w-full rounded-xl shadow-md shadow-gray-400 text-gray-600 text-md py-2 mt-4 border hover:scale-110 duration-500">
                        <a id="close_new_task">
                            Go back
                        </a></button>
                </div>
            </div>
        </div>
    </div>
```

6. New Task View Function and Routing

<img width="926" alt="Screen Shot 2022-10-13 at 11 35 59 AM" src="https://user-images.githubusercontent.com/101589777/195502663-1423ed74-c7e2-4aa9-8f5d-093cd7b4b0d5.png">

<img width="551" alt="Screen Shot 2022-10-13 at 11 37 17 AM" src="https://user-images.githubusercontent.com/101589777/195502804-71e2f26f-969b-4048-8a07-aee8b13a1c0d.png">

7. Implement AJAX POST

<img width="691" alt="Screen Shot 2022-10-13 at 11 38 10 AM" src="https://user-images.githubusercontent.com/101589777/195502912-8e86c191-eca8-4eff-8aa6-9c09e2bb6640.png">
