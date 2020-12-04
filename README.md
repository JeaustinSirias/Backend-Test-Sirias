# Cornershop's Backend Test solution

Hi there! In this repository you will find my implementation for the **Cornershop's Backend Test**. 


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
This project uses **Docker compose integration** to build a time saving container. It's highly recommended to build it this way, so you won't have to complain about your python and your libraries version. Make sure you have already installed **Docker** and **Docker compose** before keep ready this documentation. If not, you can get involved with it for a quick tutorial at:

* [Install Docker service](https://docs.docker.com/get-docker/)
* [Install Docker compose service](https://docs.docker.com/compose/install/)

## Building instructions
### Step 1: Cloning the repository
Start by cloning this repository to your computer by typing the next instruction in your command lines window:

```command
git clone https://github.com/JeaustinSirias/Backend-Test-Sirias.git
```
Once this gets done move to the cloned repository path.

### Step 2: Setting up your Slack enviroment



