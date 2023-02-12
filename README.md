# Agent-Hunt
Zerodown Hackathon

Agent Hunt deployed on render is a web application which includes injecting data from postgreSQL to python, cleaning the data, removing duplicates, performing analysis, visualizing the data, gaining insights and so on.

# Website Link:
https://agenthunt.onrender.com

# Tools and Technologies:
- Flask, HTML, CSS, Bootstrap, Jinja
- PostgreSQL, psycopg2
- Tableau
- Python

# Web Application Deployment:
This application has been deployed using render with all the tables in the databases available in the network postgres server which helps in processing the data without the local server.

## Milestone 1 : ER Diagram
ER Diagram has been visualized with the help of ER builder tool mentioning primary keys, relationships, cardinality and so on.

![ER-Diagram](https://user-images.githubusercontent.com/102233917/218289119-c5fc81f7-a9f1-4ae4-a55e-c28ae7f73ecc.png)

## Milestone 2 : Removing Duplicates 
Removing similar data has been done in 2 ways:
   1. By writing direct sql queries which does self joining on the same table. If any similar values is found for any of the mentioned attribute, it is been removes from the postgres table.
   2. By writing python code, which involves loading the postgres tables to python with the help of psycopg2 and rows of the mentioned attributes are compared with each other with for loops.
   
Removing near similar words data has been done in 2 ways:
   1. By calculating cosine similrity between 2 words by converting them to vectors and calculating the cosine distance between them.
   2. By calculating the edit distance which is the minimum that should be done to convert a word similar to the other.
   
## Milestone 3 : Reltionship Graph between the related agents
Construction of relationship graph has been done in 2 ways:
   1. Using the NetworkX library available in python by passing the edge set.
   2. Using the line graph plot available in Tableau
   
Edge set is found by joining agent_listing table with the home_info table twice, from which agent_list and agent_sell is found by joining based on home_id and inserted into  new table agents_relations for further processing.

## Milestone 4 : Top n agents and brokerages
Using the forms available in HTML the necessary details has been taken from the user and the top n agents and brokerages hs been found by grouping the data and counting which gives which agent and brokerage completed more no. of deals

## Milestone 5 : Reltionship Graph between the related agents with market id
Same as in ms3 the data is visualized along with an added constraint the they should belong to the same market which can be found by comparing the city_market_id, state_market_id, country_market_id and the zip_market_id by joining the home_info, agent_listing and the agent_info tables.

## Data Visualization using Tableau
Using various useful charts generated using tableau, top brokers, agents who sold valuable property, deal side, listed and sold price comparision, status of agents, countries with valuable properties and so on are visualized.

# Website Output

## Home Page:
![image](https://user-images.githubusercontent.com/102233917/218290181-7c043d35-d0bc-4f24-a4e0-28bee7ab8e83.png)

## ER Diagram Page:
![image](https://user-images.githubusercontent.com/102233917/218290182-6ab5ae6b-b086-411d-8f76-f3a5ea954cb7.png)

## Agent relation visulization:
![image](https://user-images.githubusercontent.com/102233917/218290191-77ff1724-31a7-43e0-81eb-76168dcc6b67.png)
![image](https://user-images.githubusercontent.com/102233917/218290202-3a22200e-612c-40a9-b2ef-3b1f946f3951.png)

## Top N Agents and Brokerages:
![image](https://user-images.githubusercontent.com/102233917/218290241-5308b781-9a8a-4ace-bd3d-39ab6463efa4.png)
![image](https://user-images.githubusercontent.com/102233917/218290240-2ea321fd-6dd1-48d6-80f3-14ee17ca1fe3.png)

## Agents relationship based on market id:
![image](https://user-images.githubusercontent.com/102233917/218290263-8fff5e5a-79a2-4775-918d-acede8abd0bf.png)
![image](https://user-images.githubusercontent.com/102233917/218290287-23ee3ed2-72d8-46d6-a180-f65041474405.png)

## Insights page:
![image](https://user-images.githubusercontent.com/102233917/218290315-235bba57-3cb5-4bd2-9dcc-08951d14e52c.png)
![image](https://user-images.githubusercontent.com/102233917/218290320-00af8a94-153a-4916-acd6-df3269d58dde.png)


##### Due to heavy computation and very high time complexity for running, in some cases, less no. of data records has been used for processing.








   


