# Abhiyaan_application_LeonDavis
Submission for Team Abhiyaan
=====================================

Name:
Leon Davis M S 

Roll no:
ED21B038

Previous Experience:
Participated in the IITM techsoc for the analytics and electrical competitons(my team got 4th place in analytics.).
I've worked with unity with C# for game development.
I've made a chess game using C language.
I've made simple 2-D games using python like the chrome dinosaur game.

Current PORs:
None

Why I want to work in the team:
I love coding and solving real-world problems using my code. Electronics also interests me, but i'm more inclined towards the software part. I think self-driving cars will play a big part in the near future, and it excites me to have a chance to work in field thats somewhat new and unexplored. I also used to love drawing and designing cars(before JEE). I like the thought of spending days, and even weeks on a problem and getting the satisfaction of finally solving it. Building something as a team and showcasing it to the world also excites me alot. So, Abhiyaan seems like the obvious choice considering my interests and all the the things i'm passionate about. I would love to work with you guys.

Relevant Courses:
In Institute:
ED1021 - 0 (It's a course on C language and OpenGL).

0 - Passed.
W - Attendance Shortage.
1 - Doing.

Online:
Harvard's CS50 - 0.
Andrew NG Deeplearning.ai - 1.

Other Relevant Things:
Section_A task_2 ROS filenames -> publisher is named pubnode, subscriber is named subnode,the message reversing node is called reverser. They are in a package called task2.The launchfile "task2launch.launch" is located in a folder named task2launch.

Section_A task_3 ROS filenames -> orbitor is node for turtle1 and orbitor2 is node for turtle2.

Section B_2 -> The idea is to find the number of corners in the threshholded image. If number of corners were above a certain number, they were ellipses and hence they were potholes.

BONUS Question 1 -> The idea is to go through each pixel on a line making a certain angle with x-axis until its pixel value is black(0 or less than 255).We use the formula x_new = x + rcos(theta) and y_new = y + rsin(theta) where x and y are the coordinates of centre of the image.We do this for all 360 degrees and plot the value of r/(length of beam) each time.


Reguarding section A task 3:There seems to be a problem in publishing to spawned turtles. My code only works for turtle1. Turtle1 is able to orbit around turtle2 but not the uther way around. My plan was to generate force on turtle one by finding distance between turtles 1 and 2 and generate the same opposite force on turtle 2. However, the same code (orbitor2) doesnt work for turtle2(which was spawned).Basically i wanted to run orbitor and orbitor2 at once using a launch file hence it would simulate both bodies attracting eachother. However, there seems to be a problem with publishing to spawned turtles.

Reguarding 

Did you attempt bonus questions:
1. Yes.
2. Yes.
3. No.
