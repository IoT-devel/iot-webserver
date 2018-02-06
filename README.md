# iot-webserver
A simple example of webserver to show some iot device state.

This example needs Flask + gunicorn + jinjia2 environment.

- sudo apt-get install python-dev libmysqld-dev
- sudo apt-get install python-pip
- sudo pip install virtualenv
- mkdir pyenv
- cd pyenv
- virtualenv iot
- source ./pyenv/iot/bin/activate
- cd iot-webserver
- pip install -r requirements.txt
- ~/pyenv/iot/bin/gunicorn -c gunicorn.conf application:app

