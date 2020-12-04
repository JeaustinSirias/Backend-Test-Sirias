# Cornershop's Backend Test solution

Hi there! In this repository you will find my implementation for the [Cornershop's Backend Test](https://github.com/JeaustinSirias/Backend-Test-Sirias/blob/main/docs/enunciated.md). 

![user_interfase](https://res-3.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco/v1457824623/x0qk4ds6je7usxll6vhk.png)


## Resume
This project threats about a webpage to manage daily lunch menus for a comunity of Cornershop employees. Its implementation has been developed using the python Django framework for web developmet. In the next sections you will find the documentation, building instructions and another activities!


## Video
You can find a full walkthrough video to see the project features.

[![Watch the video](https://i.imgur.com/wEHDbPs.png)](https://youtu.be/RND7s5csZW0)

## Specifications

This project uses background tasks to operate **Slack channels integration**. In consecuence this development is a sinergy of many microservices that help to create a final result:

* [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
* [RabbitMQ](https://www.rabbitmq.com/)
* [Slack](https://slack.com/intl/en-cr/)
* [Django](https://www.djangoproject.com/)
* [Docker](https://www.docker.com/)

## Before you continue
### About Docker use
This project uses **Docker compose integration** to build a time saving container. It's highly recommended to build it this way, so you won't have to complain about your python and your libraries version. Make sure you have already installed **Docker** and **Docker compose** before keep reading this documentation. If not, you can get involved with it for a quick tutorial at:

* [Install Docker service](https://docs.docker.com/get-docker/)
* [Install Docker compose service](https://docs.docker.com/compose/install/)

## Building instructions
### `Step 1:` Cloning the repository
Start by cloning this repository to your computer by typing the next instruction in your command lines window:

```command
$ git clone https://github.com/JeaustinSirias/Backend-Test-Sirias.git
```
Once this gets done move to the cloned repository path.

### `Step 2:` Setting up your Slack enviroment
Slack service depends on the group of users where it is running and it requires authentication from the channel administrator, so to integrate this feature to your project you first need to set up your slack enviroment. You can read about how to install a Slack app [here](https://api.slack.com/apps). In case you already have your **Slack token** ([OAuth token](https://slack.com/intl/en-cr/help/articles/215770388-Create-and-regenerate-API-tokens)) with all granted [channel scope permissions](https://api.slack.com/scopes), then all you have to do is edit the [setup.py](https://github.com/JeaustinSirias/Backend-Test-Sirias/blob/main/main/setup.py) file inside the project's directory with your credentials:

```python
'''Modifiable parameters of the project'''

# The Slack app token
OAUTH_TOKEN = '<your_token_here>' 

# The Slack channel name
SLACK_CHANNEL = '#<your_channel_name>'

# The hour limit for employees to request their menu
HOUR = 11 # AM CLT
```
Once you've done this, then save changes and let's continue with the next steps!

### `Step 3:` Running the project using Docker service
Make sure you are in the project's root directory and by using your terminal again type the following makefile instruction to **build and run** the web Cornershop's Backend test:

```command
$ make docker
```
The image may take some minutes to get done as it downloads all its dependences. If everything went as expected you should be seeing now the HTTP direction of the devepment server as usual in Django projects as the next image shows:

![bash_terminal](https://i.imgur.com/p4i1i0B.png)

Then go to <http://0.0.0.0:8000/> to start navigating in the web project.

### `Step 4:` Administration credentials
So at this point the developmet server has you redirected to an authentication page. This is what Nora would actually see if she were the administrator. To login use the next superuser credentials:

* **username**: nora
* **password**: admin
 
As you get it done so you will be in front of the main administrative page for Nora just like the next image:

![web](https://i.imgur.com/4wfFlj6.png)

Now you can start discovering the webpage features such as creating a menu for today and sending the Slack reminder to the channel you specified in the **Step 2**. If the project is currenty running OK and the Slack backgroun integration was successfully made, so you will be seeing something like this in in your Slack channel as you set up the today's menu:

![bash_terminal](https://i.imgur.com/AKK1Gat.png)

At this point if you want to interact as an employee (insted of Nora), so you can use the next common users (non admins) to request today's menu or something:

* **username**: jose, **password**: jose12345
* **username**: ana, **password**: ana12345

### `Step 5:` Running unittests (optional)
The project counts with a list of unitary tests to make sure that its `views`, `forms`, `models` and `celery tasks` are running as expected. You can run unittests from the same docker container by typing the next instruction in your bash terminal:

```command
$ make dockerUnittest
```

## Just in case definitely you do not want to user Docker service
If you do not want (or can) use the Docker services, then you can also build a virtual enviroment [venv](https://docs.python.org/3/tutorial/venv.html) (python 3.7+) as traditionally is made. **Make sure you are in the cloned project root directory**. In any case you will have to install the project's [dependences](https://github.com/JeaustinSirias/Backend-Test-Sirias/blob/main/requirements.txt) by using the next command:

```command
$ make requirements
```
And to run the Django project, as you usually know, from your local or virtual enviroment, type:

```command
$ make run
```
If you also want to run unittests this way, then use:

```command
$ make unittest
```
I hope you liked this walkthrough. See you the next time! :)


