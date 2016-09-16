# code-katas
## kata 1: Proper-parenthetics

###Python function takes a unicode string (text) as input and returns one of three possible values:

* 1 if the string is “open” (there are open parens that are not closed)
* 0 if the string is “balanced” (there are an equal number of open and closed parentheses in the string)
* -1 if the string is “broken” (a closing parens has not been proceeded by one that opens)

### To run:
```
$python parenthetics.py
$parenthetics(string)
```
## kata 2: Sort deck of cards
### Python function sorts shuffled list of cards, sorted by rank.
### To run:
```
$python sort_cards.py
$sort_cards(list('39A5T824Q7J6K'))  --> list('A23456789TJQK')

### 2 Solutions:
* sort_cards.py - using priority queue
* sort_cards_no_pq - without  priority queue

## kata 3: Sort deck of cards
### Given a starting city and an ending city, wilpython function returns:
* the shortest path between the two cities (including the two cities)
    - the shortest path is based on Dijkstra's algorithm
* the distance traveled between them
* appropriately handles the situation where no path exists

### To run:
```
$python src/flight_paths.py
$path('Moscow', 'London') # => ['Moscow', 'London'] traveled distanse is 1560.2 mi
```