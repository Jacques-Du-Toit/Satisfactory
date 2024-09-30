# Satisfactory


## What do I want as a user

What types of things would be useful?  
I'm thinking maybe a program where you give it a part you want to make i.e. reinforced iron plates.  
It then will tell you all the different trees you could use to make the part, showing what machines are used at each layer,  
and the stats of each tree.  
Ideally there would be some UI showing the trees in a nice easy way to follow, but we will sort out the backend first.

Let's break this into smaller problems:
1. Given a part, what are all the branching paths for it
   1. A list of all the different possible recipes we could follow
   2. The list should also show all the required outputs as it goes down the route
2. Calculate the stats per tree
   1. Maybe have something that automatically removes trees that have all objectively worse stats
3. Represent the tree in a nice way

## Stats

### +
  - output per minute (all products)
  - unique outputs  

### -
  - input per minute
  - unique outputs
  - power usage
  - machines used (square feet used if possible)