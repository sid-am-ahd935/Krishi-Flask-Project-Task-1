# Krishi-Flask-Project-Task-1

This project is for submission under Krishi Network under SDE Internship Problem Statement 2022. This project uses flask to handle the API endpoints and has two main features, checking weather for a given lattitude and longitude point, and post or retrieve tweet message for that location given.

It uses PostgreSQL database for storing and retrieving data which only consists of the tweet messages that are sent to its POST API. While retrieving tweet messages, it orders all the tweets based on how close they are with the given location on retrieving. This feature also contains pagination of size 10.

The link to the API example in JSON format is given below:

For shorter and more readable JSON: https://github.com/sid-am-ahd935/Krishi-Flask-Project-Task-1/blob/main/Sample_API_Data.json

For the JSON based on all the features of the Web App: https://github.com/sid-am-ahd935/Krishi-Flask-Project-Task-1/blob/main/API_Data.json
