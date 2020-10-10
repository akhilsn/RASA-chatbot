## interactive_story_24
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "bombay"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "bombay"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget": "high"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"location": "Mumbai"}
    - slot{"budget": "2500"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "shuklaakhil2014@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen
    
## interactive_story_25
* greet
    - utter_greet
* restaurant_search{"location": "Patna", "cuisine": "chinese"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget": ">400"}
    - form: restaurant_form
    - slot{"budget": "400"}
    - slot{"location": "Patna"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "shuklaakhil2014@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_26
* greet
    - utter_greet
* restaurant_search{"budget": "1000"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"budget": "1000"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "chennai"}
    - form: restaurant_form
    - slot{"location": "chennai"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "north indian"}
    - form: restaurant_form
    - slot{"cuisine": "north indian"}
    - slot{"location": "chennai"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "shuklaakhil2014@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_27
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "madurai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "madurai"}
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget": "more than 700"}
    - form: restaurant_form
    - slot{"budget": "700"}
    - slot{"location": "madurai"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* fetch_email{"email": "shuklaakhil2014@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_01
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Jhansi", "budget":"mid"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Jhansi"}
    - slot{"cuisine": "italian"}
    - slot{"budget": "mid"}
    - form{"name": null}
    - slot{"requested_slot": null}    
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_28
* greet
    - utter_greet
* restaurant_search{"location": "koch"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "ahmedabad"}
    - form: restaurant_form
    - slot{"location": "ahmedabad"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "italian"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget": "2000"}
    - form: restaurant_form
    - slot{"budget": "2000"}
    - slot{"location": "ahmedabad"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "akhilnshukla@yahoo.in"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## happy_case_1_location_2_cuisine
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Delhi"}
    - form: restaurant_form
    - slot{"location": "Delhi"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "Mexican"}
    - form: restaurant_form
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Delhi"}
    - form: restaurant_form
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget":"mid"}
    - form: restaurant_form
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Delhi"}
    - slot{"budget": "mid"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm+fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## sad_case_1_Loc_2_wrongCuis_3_wrongCuis_4_rightCuis
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Shimla"}
    - form: restaurant_form
    - slot{"location": "Shimla"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "Vietnamese"}
    - form: restaurant_form
    - slot{"cuisine": null}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "Japanese"}
    - form: restaurant_form
    - slot{"cuisine": null}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "American"}
    - form: restaurant_form
    - slot{"cuisine": "American"}
    - slot{"location": "Shimla"}
    - form: restaurant_form
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget":"low"}
    - form: restaurant_form
    - slot{"cuisine": "American"}
    - slot{"location": "Shimla"}
    - slot{"budget": "low"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen
    
## sad_case_1_wrongLoc_2_wrongLoc_3_wrongLoc_4_rightLoc_5_rightCuisine
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Lagos"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Urja"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Udaipur"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Nashik"}
    - form: restaurant_form
    - slot{"location": "Nashik"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "Italian"}
    - form: restaurant_form
    - slot{"cuisine": "Italian"}
    - slot{"location": "Nashik"}
    - form: restaurant_form
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget":"900-1000"}
    - form: restaurant_form
    - slot{"cuisine": "Italian"}
    - slot{"location": "Nashik"}
    - slot{"budget": "900-1000"}
    - form{"name": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "kolkata"}
    - form: restaurant_form
    - slot{"location": "kolkata"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "italian"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - slot{"location": "kolkata"}
    - form: restaurant_form
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget":">1000"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - slot{"location": "kolkata"}
    - slot{"budget": ">1000"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm+fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Kolkata"}
    - form: restaurant_form
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget":"low"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkata"}
    - slot{"budget": "low"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* deny
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_3
* restaurant_search{"location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkata"}
    - form: restaurant_form
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget":"low"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkata"}
    - slot{"budget": "low"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* deny
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_4
* restaurant_search{"cuisine": "chinese"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Mumbai"}
    - form: restaurant_form
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget":"low"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"budget": "low"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* deny
    - utter_goodbye
    - action_restart
    - action_listen
    
## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Kolkata"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "italian"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - slot{"location": "Kolkata"}
    - form: restaurant_form
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget":"low"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - slot{"location": "kolkata"}
    - slot{"budget": "low"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* deny
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_06
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "kolkata"}
    - form: restaurant_form
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget":"low"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"location": "kolkata"}
    - slot{"budget": "low"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* deny
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_6
* restaurant_search{"cuisine": "mexican", "location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget":"low"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"location": "kolkata"}
    - slot{"budget": "low"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm+fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_7
* restaurant_search{"budget": "mid", "location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"budget": "mid"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"location": "191, Park Street, Near 7 Point Crossing, Park Circus Area, Kolkata"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm+fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_8
* restaurant_search{"budget": "within 900", "location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"budget": "within 900"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"location": "191, Park Street, Near 7 Point Crossing, Park Circus Area, Kolkata"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_9
* restaurant_search{"cuisine": "mexican", "budget": "900-1200"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "mexican"}
    - slot{"budget": "900-1200"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "kolkata"}
    - form: restaurant_form
    - slot{"location": "kolkata"}
    - slot{"location": "191, Park Street, Near 7 Point Crossing, Park Circus Area, Kolkata"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"budget": "mid"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"budget": "mid"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "bhopal"}
    - form: restaurant_form
    - slot{"location": "bhopal"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "vietnamese"}
    - form: restaurant_form
    - slot{"cuisine": null}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"location": "Plot 5 And 6, First Floor, City Cement, Zone - 01, Maharana Pratap Nagar, Bhopal"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen


## interactive_story_11
* restaurant_search{"cuisine": "mexican", "location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget": "high"}
    - form: restaurant_form
    - slot{"budget": "1000"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "mexican"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_12
* restaurant_search{"cuisine": "italian", "location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget": "high"}
    - form: restaurant_form
    - slot{"budget": "1000"}
    - slot{"location": "74/8/12, Jadavpur Central Road, Ram Thakur Sarani, Golf Green, Kolkata"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* deny
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_13
* restaurant_search{"cuisine": "Mexican", "location": "kolkata", "budget": "1000"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "Mexican"}
    - slot{"budget": "1000"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_14
* restaurant_search{"cuisine": "Mexican", "location": "kolkata", "budget": "1000"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "surat"}
    - slot{"cuisine": "Mexican"}
    - slot{"budget": "1000"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* deny
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_15
* restaurant_search{"cuisine": "Mexican", "location": "indore", "budget": "1000"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "indore"}
    - slot{"cuisine": "Mexican"}
    - slot{"budget": "1000"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_16
* restaurant_search{"cuisine": "Mexican", "location": "Jammu", "budget": "1000"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Jammu"}
    - slot{"cuisine": "Mexican"}
    - slot{"budget": "1000"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm+fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_17
* restaurant_search{"location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "vietnamese"}
    - form: restaurant_form
    - slot{"cuisine": null}
    - slot{"requested_slot": "cuisine"}
* deny
    - utter_sorry
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_18
* restaurant_search{"location": "tokyo"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* deny
    - utter_sorry
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_19
* restaurant_search{"cuisine": "vietnamese", "location": "tokyo"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"requested_slot": "location"}
* deny
    - utter_sorry
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"location": "tokyo"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* deny
    - utter_sorry
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget": "high"}
    - form: restaurant_form
    - slot{"budget": "1000"}
    - slot{"location": "kolkata"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

## interactive_story_23
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "budget"}
* form: restaurant_search{"budget": "low"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"location": "kolkata"}
    - slot{"budget": "300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_need_email
* affirm
    - utter_ask_email_id
* fetch_email{"email": "dip@gmail.com"}
    - action_email_sender
* affirm
    - utter_goodbye
    - action_restart
    - action_listen

