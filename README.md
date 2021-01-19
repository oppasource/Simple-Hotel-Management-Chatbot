# Simple Hotel Management Chatbot 

This is a simple chatbot for a Hotel to handle room booking and cleaning requests along with FAQs. Built using [RASA](https://rasa.com).

## Steps to run the code
Train the NLU and Core models for chatbot
```
rasa train
```

Start the duckling entity extractor server.
```
sudo docker run -p 8000:8000 rasa/duckling
```

Run the action server
```
rasa run actions
```

Run the chatbot in command line
```
rasa shell
```

Optionally, the model can also be trained if not downloaded
```
rasa train
```
