### Problem Statement

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. You have been hired as the lead data scientist for creating this product. 
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.The bot takes the following inputs from the user:
- **City**: Take the input from the customer as a text field. For example:
    - Bot: In which city are you looking for restaurants?
    - User: anywhere in Delhi
- **Cuisine Preference**: Take the cuisine preference from the customer. The bot should list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that. Following is an example for the same:
    - Bot: What kind of cuisine would you prefer?
    
            Chinese
            Mexican
            Italian
            American
            South Indian
            North Indian
    - User: I’ll prefer Italian!
- **Average budget for two people**: Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. The bot should ask the user to select one of the three price categories. For example:
    - Bot: What price range are you looking at?

            Lesser than Rs. 300
            Rs. 300 to 700
            More than 700
    - User: in range of 300 to 700
    
- **Email:** The bot should ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot should ask for user’s email id and then send it over email. Else, just reply with a 'goodbye' message. The mail should have the following details for each restaurant:

            Restaurant Name
            Restaurant locality address
            Average budget for two people
            Zomato user rating
            
### Important Notes

- Assume that Foodie works only in Tier-1 and Tier-2 cities
- The bot should be able to identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc.
- Your chatbot should provide results for tier-1 and tier-2 cities only, while for tier-3 cities, it should reply back with something like _"We do not operate in that area yet"_.
- While showing the results to the user, the bot should display the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.


### Versions
    rasa==1.10.3
    rasa-sdk==1.10.2
    rasa-x==0.29.3
Full list given in _read me.txt_

