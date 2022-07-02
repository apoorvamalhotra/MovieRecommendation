# Python Assignment
## _How to run_

Run the `assignment.py` file to execute the program. You can use the command :
```
python -m pythonAssignment.assignment
```

You can input the any numeric value from **1 to 5** as required to execute any one of the 5 tasks mentioned below in the Problem Statement.

## _Problem Statement_

These days, no matter we look, we are bombarded with automated recommendations - whether a movie to watch on Netflix, or a things to buy on Amazon. Let's learn and showcase our Python skills by implementing our own mini-recommendation engine. Don't worry if you have never done this before, we'll walk you though this step-by-step!

To make it easy on ourselves, let's stick with movies and movie ratings. (But the principles involved in this project can be adapted to books, restaurants, and more.) You will write a program to recommend movies to a person based on the ratings of several movies by other people of similar age. (Yes, in our case, we'll consider only their age. However, a real recommendation system may use hundreds of variables - also known as "features"!)

- **Input File 1**: `RatingsInput.csv` This file contains the ratings given by a person to each movie. You program will use this data "learn" how people of different ages rate each movie.
- **Input File 2**: `NewUsers.csv` This lists some new users, their age, and the number of movies they want to be recommended to them. The file also has a question mark (?) which you will replace with movie recommendations.
- **Output File**: `task5Output.csv` Your final output file after replacing the question mark with the names of movies you are recommending to them.

To accomplish this assignment, you will go through a series of five tasks. If you accomplish the five tasks successfully, you will arrive at the final output file as above.
> Task 1 - **Separate Movie IDs and Movie names.**
In the provided input file, you will notice that the MovieID column is empty.  Unfortunately, Movie IDs and Movie Names are combined into a single column MovieName. In this task, you will separate these two parts into corresponding columns -> MovieID and MovieName. You will create a new CSV file with the MovieID column filled out and with the MovieName column containing only the name of the movie. This task will test your file and string manipulation skills.

> Task 2 - **String Capitalization - Capitalizing the first letter of every word in the movie names.**
Capitalize the first letter of every word in the MovieName column.
e.g. :   dinosaur planet -> Dinosaur Planet
You will create a new CSV file in this format.

> Task 3 - **Read in from your new CSV file from Task 2 and parse data into lists and dictionaries.**
You can choose any type of dictionary and/or list that you like. Below is an example of how you can create one but you are welcome to choose your own as long as you can accomplish the objectives of remaining tasks (4 and 5). You may want to read those two tasks before you make a decision.
As an illustration, you can create a dictionary with the key as the age and the value as another dictionary based on ratings. The inner dictionary will use the rating as the key and the list of movies as the value. For example
34 => { 1 => [“Dinosaur Planet”, “Rocky”], 2 => [“Coco”], 3 -> [“Twins”,”Cars”]}
indicates that users of age 34 have given Dinosaur Planet and Rocky a rating of 1, Coco a rating of 2, and Twins and Cars a  rating of 3. You will have ratings from 1 to 5 in your inner dictionary. Your outer dictionary will have many entries - one for each age.
Once you have these dictionaries and lists, you should be able to easily look up and identify the best-rated movies for each age.

> Task 4 - **Find the recommended movies for a given age from best to worst ratings.**
You will write a function that takes an age and goes through the maps/lists you created in the previous task to return (and display) the best-recommended movies for that age. You should also take an additional parameter, which is the maximum number of movies to be recommended/displayed for that age. You should display no more than the requested number of movies.
In this task, use your creativity to determine how you will recommend movies. Consider the scenarios where you may not have an exact age match. Also, consider if you should recommend a movie that was rated 2 even if it's listed against a particular age.

> Task 5 - **Recommend movies to users in the second input file.**
Now process the second input file given to you by us which contains a list of new users with their ages as well as the number of recommendations they requested. Call the function above repeatedly for each line in the file to get the best recommendations for a user based on their age. Create a new output file - you don’t need to physically replace the question marks in the input file.

## _Solution Approach_
The **'UserAge'** given in Input File 1 : `RatingsInput.csv` is divided into age groups based on the interval it lies in.
For creating these intervals, ***qcut*** function of the ***pandas*** library is used. Basically qcut tries to divide up the underlying data into equal sized bins. For this problem we are dividing the data into **10** bins.

The above mentioned 'Group' acts as a key to a dictionary whose value is another dictionary. The inner dictionary contains ratings from 1 to 5 as keys and the list of movies with that particular rating as the value.
*For example:*
```
{
    10 :
        {
            1: ["Class Of Nuke 'Em High 2"],
            2: ['Spitfire Grill'],
            4: ['Strange Relations'],
            5: ['Classic Albums: Meat Loaf: Bat Out Of Hell', 'The Bonesetter']
        }
}
```
Where ***10*** is the **Group** ,
the keys ***1, 2, 4*** and ***5*** in the inner dictionary are **ratings** and,
the values ***["Class Of Nuke 'Em High 2"], ['Spitfire Grill'], ['Strange Relations']*** and ***['Classic Albums: Meat Loaf: Bat Out Of Hell', 'The Bonesetter']*** are **movies** with the respective ratings (keys).

A movie is recommended based on the group in which the input user age lies only if the rating is **3 and above**. If the group has less recommendations than asked for, the next closest age group is considered to provide recommendations.
