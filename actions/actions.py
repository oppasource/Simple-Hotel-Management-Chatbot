# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import datetime

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
# from rasa_sdk.forms import FormAction


class ActionRoomBookResults(Action):
    def name(self) -> Text:
        return "action_room_book_results"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        num_room = tracker.get_slot("number")
        type_room = tracker.get_slot("type_room")

        dispatcher.utter_message("You have chosen to book " + str(num_room) + " " + str(type_room) + " rooms")
        return [Restarted()]


class ActionCleanRoomResults(Action):
    def name(self) -> Text:
        return "action_clean_room_results"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        raw_clean_time = tracker.get_slot("time")
        try:
        	clean_time = dict(tracker.get_slot("time"))
        	clean_time = clean_time['from']
        except:
        	clean_time = tracker.get_slot("time")

        date = clean_time[0:10]
        time = clean_time[11:19]

        # ist = datetime.datetime.strptime(str(date) + ' ' + str(time), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=5, minutes=30)
        ist = datetime.datetime.strptime(str(date) + ' ' + str(time), '%Y-%m-%d %H:%M:%S')
        ist_now = datetime.datetime.now()

        difference = ist - ist_now
        # print(raw_clean_time)
        # print(ist)
        # print(ist_now)
        # print(difference.total_seconds())
        # print(difference.days)
        # print('===================')

        day_difference = (ist - ist_now.replace(hour=0, minute=0, second=0)).days

        if difference.total_seconds() <= 60:
            dispatcher.utter_message("Sure, I will send someone to your room right away.")
            return [Restarted()]

        if int(day_difference) == 0 :
        	formatted_time = ist.strftime("%I:%M %p")
        	dispatcher.utter_message("Sure, I have scheduled a cleaning for " + str(formatted_time) + " today.")
        	return [Restarted()]
        elif int(day_difference) == 1:
        	formatted_time = ist.strftime("%I:%M %p")
        	dispatcher.utter_message("Sure, I have scheduled a cleaning for " + str(formatted_time) + " tomorrow.")
        	return [Restarted()]
        else:
        	formatted_time = ist.strftime("%I:%M %p on %d %b %Y.")
        	dispatcher.utter_message("Sure, I have scheduled a cleaning at " + str(formatted_time))
        	return [Restarted()]


# class HotelBookForm(FormAction):

#     def name(self):
#         return "hotel_book_form"


#     @staticmethod
#     def required_slots(tracker):
#         return ["number", "type_room"]


#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:

#         dispatcher.utter_message("Thanks, great job!")
#         return []

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
