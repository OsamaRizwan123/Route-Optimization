# Route-Optimization
A comparative study between Heuristic Algorithm and Brute Force Algorithm to solve Traveling Salesman Problem (TSP).

### Abstract
The Traveling Salesman Problem (TSP) is a crucial problem that got associated with NP-hard problem by Karp in 1972 at the early stages of development of NP-completeness theory (Michael Jünger, 1995). The TSP is a wellknown algorithmic problem that resides in the domain of operations research & computer science studies. It primarily focuses upon finding the shortest yet most optimum route for a salesman to take given a set of locations (Ma, 2020). This paper presents a comparative study between two core algorithms for instance Brute Force Algorithm & Heuristic Approach (Genetic Algorithm) on the real-life data points made available by Retailo Technologies and highlight the implementation of the most efficient algorithm to find the shortest yet most efficient route to travel within a city.

### Problem Identification
This research paper focuses to solve one of the problems at Retailo which is highly related to Traveling Salesman Problem. Retailo has around 200 sales agents that are on field and they are primarily required to book orders from the shops that are assigned to them. On average a sales agent is typically required to visit 15 shops in a given day with an over of 90 unique shops in a whole month (the number varies depending upon the segment the agent works).

Once the shops are assigned the agent will commence his route to visit those 30 shops that would be visible on his mobile application. Once a customer has been visited, the customer would be marked as visited and the agent would continue his route by looking at the next possible close customer to his current location. This method is similar to what we call ‘Greedy Approach’. The Greedy Approach Algorithm looks for the local optima whilst optimizing the local best solution to reach the global optima (Raju, 2020). To better understand, the Greedy Approach illustrated on the right seeks to find the route with shortest distance. It does this by selecting the shortest available number at each step. The greedy approach fails to find the shortest route, because it makes it decision on each step without taking into consideration the whole overall problem (Karleigh Moore, 2022). 

![Route Optimization 2](https://github.com/user-attachments/assets/7f003231-2435-469e-85a7-b75eca248f5c)

![Route Optimization](https://github.com/user-attachments/assets/3a8f2b70-2a23-4d0b-a263-c6a7a42e30e6)
