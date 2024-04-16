# Discord_Test_-Chatbot
A  basic chatbot in Discord contains API of snapshot. 

first converts the user input to lowercase for case-insensitive comparison.

If the user input is empty, it returns a default message.
If the user input contains "hello", it returns a greeting message.
If the user input contains "how are you", it returns a response indicating the bot's mood.
If the user input contains "bye", it returns a farewell message.
If the user input contains "roll dice", it generates a random number between 1 and 6 as a simulated dice roll result.
If the user input contains "proposals", it sends a GraphQL query to the Snapshot API to fetch closed proposals from specific spaces (balancer.eth and yam.eth). It then parses the response and returns the title of the first proposal if successful, otherwise, it returns a "bad request" message.
