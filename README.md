# DevChallenge2023

This project is my task completion on DevChallenge 2023


## Prerequisites

- Docker and Docker Compose installed on your system. (To run with Docker Image)
- Python latest version installed on your system.
- Virtual environment is created:
```bash
    python -m venv venv
```

- All further settings should be done in venv virtual environment:
```bash
    venv\Scripts\activate
```

- All requirements are installed properly:
```bash
    pip install -r requirements.txt
```

## How to Run

You can run it localy using Docker Image or Django delivery for DEBUG purposes only.

### Locally with Django only | Checked and ready to go

To run localy you need to make sure that all the prerequisites are done.
And don't forget that .env file should be added to your repository.
After that you can launch the app by this command:

```bash
    python manage.py runserver 8080
```

It will be available at http://127.0.0.1:8080/

To run the tests you can use this command:

```bash
    python manage.py test base
```


### Build the Docker Image | Cannot check due to WSL issues at the moment

Before running the service, build the Docker image using the following command:

```bash
    docker-compose build
```

To start the service, run the following command:
```bash
    docker-compose up
```

Django application will be available at http://localhost:8080/.

To run the test suite inside Docker, use the following command:
```bash
    docker-compose run web python manage.py test
```


### My practices and ways to make the service better

I used UpperCase Snake standart for my code together with PIP-8 best practices.
I tried to be precise and create a code that can be developed in the future.
That is why my method in views.py handles both GET and POST request.
Ofcourse, I could do it differently and set a handler seperately, but
for now it is not as necessary. I think that having only 2 URLs patterns is a good thing too.
Even though there are three tasks it would be hard and bad idea to do a pattern for each task.


For calculation I used builtin functions and methods. I tested everything manualy first, by using
PostMan tool. After that I created Unit tests, but I must say they could have been done
better. That also involves my knowledge in Dockers, it is too poor and I got some issues
with the Docker being installed on my PC. I literally cannot run it. So I hope it is working
fine. That is why I created two methods to run the app - using Django only and using Docker.
I could also involve nginx and gunicorn in the process but for such a light task I don't think
it is that critical for now.