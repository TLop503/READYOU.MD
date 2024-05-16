# READYOU.MD
Simple API for a class project that returns word count and time to read for an inputted document.

## Setup
Clone the repo or download app.py. To start the API, call `python3 app.py` on the file (note you must `pip install Flask` if you haven't already). If you would like to change the port being used by the API, edit the `app.run` line to specify `port=####`. 

# Contacting the API.
Because this is a REST Api, data is requested and recieved in the same line. To contact the API, first structure data in this format with the text you would like analyzed:

`{'text' = 'your text here'}`

Then, `POST` the data to `host:port/read`. By default this will be `HTTP://localhost:5000/read`. You will recieve a response in the following format if all goes well, along with a `200` response:

```json
{
    'count' : int,
    'time_minutes' : int,
    'complexity' : "int/5"
}
```

If the request fails, you will recieve a 400 response from the API. 

## Example Python Call
To see an example of how to call this API in Pyhon, check the `/tests/example.py` script.

# UML Diagram
![UML Diagram summarizing the API instructions](/embeds/image.png)
