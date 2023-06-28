#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -sL -X PUT -d "You got me!" "$1/catch_me"
