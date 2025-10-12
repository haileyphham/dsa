from collections import deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        route_sets = []         #convert list to sets so when we look up if stop in route its O(1) time; also gets rid of duplicates
        route_dict = defaultdict(list)    #create a dictionary = given a stop, which bus routes have that stop can can transfer to
                                          #key: given stop number, value: set of route indecies that include that stop
        for route_id, stops in enumerate(routes): #enumerate adds a counter to an iterable; route_id starts count (index), stops gives us the (value)
            route_set = set(stops)        #each interation of stops is a route list and we convert it into a set 
            route_sets.append(route_set)  #store each route_set into a list of route_sets

            for stop in route_set:        #now for each individual stop in a route_set
                route_dict[stop].append(route_id)      #for that individual stop is a key, and we add route_id 

        #BFS is a queue --> setup
        start_routes = route_dict.get(source, [])    #collecting all the route_ids that's key is 'source'
        if not start_routes:
            return -1

        q = deque(start_routes)         #each item in the queue is a route_id that has source
        visited_routes = set(start_routes)  #so we dont go back to old routes we've visited (infinite loops)
        visited_stops = set([source])       #keep track of stops we've visited
        bus_count = 1

        while q:                            #actual BFS algorithm
            level_size = len(q) 

            for _ in range(level_size):
                route_id = q.popleft()     # pop the next route (bus) to explore

                if target in route_sets[route_id]: #route_sets is the list of lists and route_id is the index
                #it the target is in the set of that given route_id then we've reached the end
                    return bus_count               #if not now we look at the neighbors
                for stop in route_sets[route_id]:  #for every stop in a given route (route_id index)
                    if stop in visited_stops:
                        continue
                    visited_stops.add(stop)

                    for next_route in route_dict[stop]: #for each route that also has this stop; for each of the values in the dictionary for that key (stop)
                        if next_route not in visited_routes: #if we haven't seem this route yet, we add it to seen
                            visited_routes.add(next_route)
                            q.append(next_route)             #then put it in the queue so we can look at it in the next level
            bus_count += 1


        return -1

        
#start from all routes that contain source
#traverse through when contains a common stop
#if == target; return num_layers