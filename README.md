# Oomck-Bot

## Getting Started

### Dependencies

- [Docker](https://www.docker.com/get-started)
- [Python 3](https://www.python.org/downloads/)

### Setup Project

1. Ensure that [Docker](https://www.docker.com/get-started) is currently running on your machine with an up-to-date version.
2. Install python dependencies with: `pip install -r requirements.txt`
3. Run `docker-compose up` to start elastic search.
4. In a new terminal, run `python main.py`.
5. Enjoy!

### Test
1. run `python -m unittest` to run all the tests

### Run sockets with other bot
1. Install python dependencies with: `pip install -r requirements.txt`.
2. Run `docker-compose up` to start elastic search.
3. Set the host address and port at the top of `python sockets/main.py`.
4. In a new terminal, run `python sockets/main.py` when the other bot is running as host.

### Assignment 3 - Features
1. GUI:
    - We implemented a GUI to improve the overall experience for our users.
2. POS Tagging:
    - We implemented POS tagging to assign labels to tokens in the user's input. This helps improve the quality of the bot's responses.
3. Synonym Recognition:
    - We implemented this in our bot to recognize synonyms within the user's input. This improves the bot's understanding of message sent by the user.
4. Interaction with Another Bot via Sockets 
   - We connected our bot with another group's chatbot through sockets in order to allow communication between the two bots.
5. Automated Unit Testing: 
   - Unit tests were implemented to ensure that the quality of our code is maintained throughout the development process. This ensures that our bot behaves as expected at all times.
6. Handle Spelling Errors: 
   - This was implemented to ensure that there are no spelling mistakes in the user's input that could affect the quality of the response returned by the bot.
7. Extra Default Responses:
    - To keep conversation going, there are now more, and on topic, default responses. This keeps the conversation going even when the user is confusing the bot.

### Features of OOMCK-Bot for an API
The following features of our bot could be put in an API for others to use.
1. Easy connection with another bot through sockets.
2. Tokenizing user input with NLTK.
3. Processing and loading of data from a JSON file into an Elastic Search instance.
4. Answer questions regarding the Fast and Furious franchise.
5. The basic structure of our chat-bot allows it to be used with a variety of datasets according to a developer's specific needs.

### API Features Implemented in Individual Project
**Google Cloud Translate API**
- This is used for automatic translation in the chatbot.

- __Why:__ Data in our ElasticSearch Database is stored in english, so it widely expands the scope of our bot to convert user input into english before querying for a response.

- __Feature:__ The bot will now also automatically convert any response (whether from the database, or one of the many default response options) into the language that was used to query it. This additional point has obvious user experience benefits for foreign language users.

**Wikipedia API**
- This is used as a sort of global noun definition tool.

- __Why:__ I found that the bot would grind conversations to a halt when asked about topics outside of its conversational scope. In A3, we added more default responses to solve this, but I thought more was needed.

- __Feature:__ In order to give the illusion that the bot truly is conversing with the user, it will actually query wikipedia for the page corresponding to the first noun encountered in a hard-to-understand input string. After doing this, the bot will respond with the first sentence of the page summary (a short description of the noun itself) along with an appended follow-up sentence to redirect the conversation. This allows the bot to more naturally "respond" to user input that deviates from the topic at hand (i.e. the Fast and the Furious move franchise).