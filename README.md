#   Project Description

A web application for downloading videos on [LinkedIn](https://www.linkedin.com).
Built using Flask, HTML, CSS and Javascript.


# Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/linkedin_video_downloader.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install virtualenv:

[Virtualenv](https://izudada.medium.com/how-to-create-a-virtual-environment-in-python-a47f401506db)

Then install the dependencies by running the below command:

```sh
$ pip install -r requirements.txt
```

Before starting the flask server, you will need to set some environmental values via the terminal:

```sh
$ export FLASK_APP=main   #   tells flask where to find the entry application file
$ export FLASK_ENV=DEBUG    #   tells flask what environment you want to run or start
```

Start the server with:
```sh
$ flask run
```
Open your browser and navigate to `http://127.0.0.1:5000/`



### Useful resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x)
- [Box Shadow Generator](https://getcssscan.com/css-box-shadow-examples)