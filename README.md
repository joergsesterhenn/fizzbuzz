# FizzBuzz Kata
Michael Feathers and EmilyBache performed this kata at agile2008 when competing in “Programming with the stars” in python, in 4 minutes.

*Difficulty*: Easy Good for teaching: TDD , BabySteps

## Problem Description

### Stage 1
Imagine the scene. You are eleven years old, and in the five minutes before the end of the lesson, your Maths teacher decides he should make his class more “fun” by introducing a “game”. He explains that he is going to point at each pupil in turn and ask them to say the next number in sequence, starting from one. The “fun” part is that if the number is divisible by three, you instead say “Fizz” and if it is divisible by five you say “Buzz”. So now your maths teacher is pointing at all of your classmates in turn, and they happily shout “one!”, “two!”, “Fizz!”, “four!”, “Buzz!”… until he very deliberately points at you, fixing you with a steely gaze… time stands still, your mouth dries up, your palms become sweatier and sweatier until you finally manage to croak “Fizz!”. Doom is avoided, and the pointing finger moves on.

So of course in order to avoid embarrassment in front of your whole class, you have to get the full list printed out, so you know what to say. Your class has about 33 pupils, and he might go round three times before the bell rings for break time. Next maths lesson is on Thursday. Get coding!

Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print "FizzBuzz".

**Sample output:**

1  
2  
Fizz  
4  
Buzz  
Fizz  
7  
8  
Fizz  
Buzz  
11  
Fizz  
13  
14  
FizzBuzz  
16  
17  
Fizz  
19  
Buzz   
... etc up to 100  

### Stage 2 new requirements
A number is fizz if it is divisible by 3 or if it has a 3 in it
A number is buzz if it is divisible by 5 or if it has a 5 in it
For example :

53 should return FizzBuzz (contains 5 and 3)
35 should return FizzBuzzBuzz (contains 3 and 5 and is divided by 5)


### Stage 3 late change in requirements
Forget what we wanted in Stage 2 this is no longer useful to us.
Instead, go with these requirements that Emilie made up in https://sammancoaching.org/kata_descriptions/fizzbuzz.html

Multiples of 7 are “Whizz”  
Multiples of 11 are “Bang”  

That means for example that multiples of 3 & 7 are “FizzWhizz”, multiples of 5 & 11 are “BuzzBang” etc.

Extend your printout, so it continues beyond 100 and stops the first time you get “FizzBuzzWhizzBang”.

### Stage 4 reintroduce the stage 2 feature
One of our customers demanded that we immediately reintroduce the feature from stage 2 in addition to the new features.
Looks like they need to be more flexible about which numbers to mark and which logic applies.

Make sure the printout stops at "FizzBuzzWhizzBangFizzBuzz"!