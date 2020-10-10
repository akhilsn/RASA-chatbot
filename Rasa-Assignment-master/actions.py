from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import re
import smtplib



class RestaurantForm(FormAction):
    """a custom form action"""

    res_det_rating_budg_sorted_mail = []
    upward_flag = False

    def name(self):
        return "restaurant_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["location","cuisine","budget"]

    # 3 mandatory slots which needs to be filled for form submission to be triggered
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "location": self.from_entity(entity="location"),
            "cuisine": self.from_entity(entity="cuisine"),
            "budget": self.from_entity(entity="budget")
        }

    @staticmethod
    def cuisine_db() -> List[Text]:
        return ["chinese","mexican","italian","american","south indian","north indian"] # List of cuisine

    def validate_cuisine(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],)-> Dict[Text, Any]:
        """Validate cuisine value."""
        actual_cuisine = value
        cuisine_map = {'chinese': ['chines','chinis','chnese'],'north indian':['north-indian','northindian','north indn','nrth indian'],'south indian':['south-indian','southindian','south indn','sth indian']} #alternate names not present in lookup tables

        def cuisine_synonym_checker(cuisine_to_check): # to check alternate values
            present = False
            for key, value in cuisine_map.items():
                if (cuisine_to_check in value):
                    actual_cuisine = key
                    present = True
            return present

        if ((value.lower() in self.cuisine_db()) or (cuisine_synonym_checker(value.lower()) == True)):
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"cuisine": actual_cuisine}
        else:
            dispatcher.utter_message("Sorry this cuisine type is not available :(")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"cuisine": None}

    def validate_location(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],)-> Dict[Text, Any]:
        """Validate location value."""
        with open('./lookup_tables/location.txt', encoding='utf-8', errors='ignore') as f:
            list_locations = f.read().lower().splitlines()
        actual_location = value
        location_map = {'mumbai': ['bombay'], 'bangalore': ['bengaluru', 'bengluru', 'bengalru', 'bngaluru', 'bngluru'],
                        'delhi': ['dilli', 'new delhi'], 'kolkata': ['calcutta', 'kalkata', 'calcata'],
                        'pondicherry': ['puducherry'], 'prayagraj': ['allahabad']}#alternate names not present in lookup tables

        def location_synonym_checker(location_to_check):# to check alternate values
            present = False
            for key, value in location_map.items():
                if (location_to_check in value):
                    actual_location = key
                    present = True
            return present

        if ((value.lower() in list_locations) or (location_synonym_checker(value.lower()) == True)):
            # validation succeeded, set the value of the "location" slot to value
            return {"location": actual_location}

        else:
            dispatcher.utter_message("Sorry we do not serve at this location currently :(")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"location": None}

    def validate_budget(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],)-> Dict[Text, Any]:

        """
        Budget range on offer
        1. less than '300' - 'low'
        2. between '300' and '500' - 'mid'
        3. more than '700' - 'high'

        How are we validating
        1. Extract digits in input value. Store in a list
        2. If there are more than one digit, it denotes user has given a range, e.g. 'in the range of 300-500'
        3. Use the number extracted and handle the case whether the number lies in permissible range
        4. store the value in slot
        """

        """List to extract digits"""

        value = value.lower()

        price_in_number = re.findall(r'\d+', value)

        """
        If there are no number in the price given by the customer, then most probably the customer has chosen,
        words like 'mid', 'high', 'cheap' etc. which can directly be handled, and filled to the slot
        Here have filled the values taken from nlu.md file for high, mid, low (incl. synonyms)
        """
        accepted_price_low = ['low', 'cheap']
        accepted_price_mid = ['moderate', 'medium', 'mid', 'moderate']
        accepted_price_high = ['expensive', 'costly', 'high']

        """
        Before we assign anything to 'value', let us check for cases, where user might ask to check search for a range above
        than a provided number/value. For this we maintain
        """

        more_than_keywords = ['more', 'above', 'upwards', 'upwards', '>']
        RestaurantForm.upward_flag = any(keyword in value for keyword in more_than_keywords)

        # to cover case such as '>900'
        if (re.match('>\d*', value)):
            RestaurantForm.upward_flag = True

        """We shall keep the value in a number form to make more smooth handling of budget in logic"""
        if len(price_in_number) == 0:

            if value in accepted_price_low:
                value = '299'
                return {"budget": value}
            elif value in accepted_price_mid:
                value = '699'
                return {"budget": value}
            elif value in accepted_price_high:
                value = '2500'
                return {"budget": value}
            else:
                dispatcher.utter_message("Sorry, could not understand your budget.")
                return {"budget": None}

        """lets define a high price limit"""
        random_high_price = 10000

        """Below var. contains the numbers input by user. User might input vague range, e.g., "in range of 300-500-700",
           In such a case we'll use the last number in the string to determine budget range"""
        num_of_numbers = len(price_in_number)

        """
        We shall check if the price number lies in permissible range
        We'll make use of the last number in our list to determine the budget range(low, mid, high)
        """
        if int(price_in_number[num_of_numbers - 1]) in range(random_high_price):
            price_range = int(price_in_number[num_of_numbers - 1])

            if price_range <= 300:
                value = str(price_range)
                return {"budget": value}

            elif ((price_range > 300) & (price_range <= 700)):
                value = str(price_range)
                return {"budget": value}

            else:
                value = str(price_range)
                return {"budget": value}

        else:
            dispatcher.utter_message("Ask is too expensive, we can offer much cheaper food :). Please select from below.")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"budget": None}

    def submit(value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
         dispatcher.utter_message("Searching for "+tracker.get_slot('cuisine')+" restaurants in "+tracker.get_slot('location') + " in :")

         config = {"user_key": "318d7bb771fa4906aa7e41e9e96299c8"} #updated with a new zomato key
         zomato = zomatopy.initialize_app(config)
         loc = tracker.get_slot('location')
         cuisine = tracker.get_slot('cuisine')
         budget = tracker.get_slot('budget')
         location_detail = zomato.get_location(loc, 100)
         d1 = json.loads(location_detail)

         lat = d1["location_suggestions"][0]["latitude"]
         lon = d1["location_suggestions"][0]["longitude"]

         cuisines_dict = {'chinese': 25, 'italian': 55, 'mexican': 73, 'american': 1, 'north indian': 50,'south indian': 85}

         """incr. limit to incorporate cases such as exotic food in small cities"""
         results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 2000)

         d = json.loads(results)
         response = ""
         if d['results_found'] == 0:
             response = "Sorry, No Results Found :("
         else:
             res_det = []
             for restaurant in d['restaurants']:
                 rating = str(restaurant['restaurant']['user_rating']['aggregate_rating'])
                 name = restaurant['restaurant']['name']
                 location = restaurant['restaurant']['location']['address']
                 avg_price_for_two = str(restaurant['restaurant']['average_cost_for_two'])
                 details = (rating, name, location, avg_price_for_two)
                 res_det.append(details)

             """Sort according to the ratings of the restaurants in decreasing order"""
             res_det.sort(key=lambda x: x[0], reverse=True)
             res_det_rating_sorted = res_det

             """We would also need to refer to the upward_price_flag status, and acc. decide"""
             upward_flag_status = RestaurantForm.upward_flag

             """Extracting the restaurants offering in customer's budget, showing top 5 results"""

             No_of_results_shown = 5
             No_of_results_mailed = 10

             def restaurants(budget):
                 if int(budget) < 300:

                     if upward_flag_status:
                         res_det_rating_budg_sorted = [res for res in res_det_rating_sorted if
                                                       int(res[3]) > int(budget)]
                     else:
                         res_det_rating_budg_sorted = [res for res in res_det_rating_sorted if
                                                       int(res[3]) < int(budget)]

                     RestaurantForm.res_det_rating_budg_sorted_mail = res_det_rating_budg_sorted[:No_of_results_mailed]
                     res_det_rating_budg_sorted = res_det_rating_budg_sorted[:No_of_results_shown]
                     budget_label = 'Low'

                 elif int(budget) in range(300, 700):

                     if upward_flag_status:
                         res_det_rating_budg_sorted = [res for res in res_det_rating_sorted if
                                                       int(res[3]) > int(budget)]
                     else:
                         res_det_rating_budg_sorted = [res for res in res_det_rating_sorted if
                                                       int(res[3]) in range(300,int(budget))]

                     RestaurantForm.res_det_rating_budg_sorted_mail = res_det_rating_budg_sorted[:No_of_results_mailed]
                     res_det_rating_budg_sorted = res_det_rating_budg_sorted[:No_of_results_shown]
                     budget_label = 'Mid'

                 elif int(budget) >= 700:

                     if upward_flag_status:
                         res_det_rating_budg_sorted = [res for res in res_det_rating_sorted if
                                                       int(res[3]) > int(budget)]
                     else:
                         res_det_rating_budg_sorted = [res for res in res_det_rating_sorted if
                                                       int(res[3]) in range(700,int(budget))]

                     RestaurantForm.res_det_rating_budg_sorted_mail = res_det_rating_budg_sorted[:No_of_results_mailed]
                     res_det_rating_budg_sorted = res_det_rating_budg_sorted[:No_of_results_shown]
                     budget_label = 'High'
                     #print(RestaurantForm.res_det_rating_budg_sorted_mail)

                 return res_det_rating_budg_sorted, budget_label

             results, budget_label = restaurants(budget)
             dispatcher.utter_message(str(budget_label) + " price range")

             """If there are not enough results for the requested budget, increase the budget and show results"""
             increased_budget = 2000
             if len(results) == 0:
                 if upward_flag_status:
                     upward_flag_status = False   # important to reset this else,
                                                  # we would increase budget, and only look upwards of it - this will
                                                  # again give zero num. of results.

                 dispatcher.utter_message("*********************************************************************************************************************")
                 dispatcher.utter_message("  \nOops! Zero results found for " + str(budget_label) + " range budget, showing results for a broader budget range  \n")
                 dispatcher.utter_message("*********************************************************************************************************************")
                 results, budget_label = restaurants(str(increased_budget))

             elif len(results) < 5:
                 # more_res_to_be_added = No_of_results_shown - len(results)
                 # more_res_to_be_added_to_mail = No_of_results_mailed - len(results)
                 dispatcher.utter_message("**********************************************************************************************************")
                 dispatcher.utter_message("  \nOops! Not enough results found for requested " + str(budget_label) + " range budget, adding results from broader budget range \n")
                 dispatcher.utter_message("**********************************************************************************************************")
                 if upward_flag_status:
                     upward_flag_status = False   # important to reset this else,
                                                  # we would increase budget, and only look upwards of it - this will have
                                                  # high chances of giving even lesser num. of results than earlier.
                 increased_budget = int(budget) + 2000
                 results, budget_label = restaurants(str(increased_budget))

             response = "Here are my top recommendations  \n"

             for i,entry in enumerate(results):
                     response = response + str(i+1) + ". Found " + "(" + entry[0] + " rating) " + \
                                entry[1] + " in " + \
                                entry[2] + " with average price for two at Rs : " + \
                                entry[3] + "\n"

         dispatcher.utter_message("  \n-----------------------------------------------------  \n" + response + "-----------------------------------------------------")
         return [SlotSet('location', loc)]

"""inheriting RestaurantForm class"""
class ActionEntityChecker(RestaurantForm):
    def name(self):
        return "action_email_sender"

    def run(self, dispatcher, tracker, domain):
        def find_pattern(text):
            if re.search("^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$", text):
                return True
            else:
                return False
        mail = next(tracker.get_latest_entity_values('email'), None)
        if(find_pattern(mail)==True):
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            # start TLS for security
            s.starttls()
            # Authentication
            s.login("customercare.rasa.restaurant@gmail.com", "Password1$")

            content_unprocessed = RestaurantForm.res_det_rating_budg_sorted_mail   # this is coming in listed tuple form
            content_processed = []

            counter = 1
            for i in content_unprocessed:
                content_processed.append(str(counter) + ". " + i[1] + ", a " + str(i[0]) + " rated restaurant, with average price for two Rs." + str(i[3]) + " is located in " + i[2])
                counter = counter + 1

            # message to be sent
            num_res = len(content_processed)

            message = "Subject: List of TOP "+(tracker.get_slot('cuisine')).capitalize()+" Restaurants delivered!\nHello, \nPlease find below the list of Top " + str(num_res) + " restaurants: \n"

            content = ''
            for i in range(len(content_processed)):
                content = content + '\n  \n' + content_processed[i]

            message += content

            message += "\n\nBon Appetit!\nDo visit us soon!!" #é is not a supported ascii character

            # sending the mail
            s.sendmail("customercare.rasa.restaurant@gmail.com", mail, message)
            # terminating the session
            s.quit()
            dispatcher.utter_message("Mail shared to "+ mail)
        else:
            dispatcher.utter_message("That does not look like a valid email id, sorry I won't be able to share the details :(")
        return []