# rasa-hotel-chatbot-nov-2020-oppasource
rasa-hotel-chatbot-nov-2020-oppasource created by GitHub Classroom

Repo contains code for the assignment provided at [this link](https://github.com/Limechat/rasa-hotel-chatbot-nov-2020-NikhilGupta1997).

This is a simple chatbot for a Hotel to handle room booking and cleaning requests along with FAQs.

## Steps to run the code

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
