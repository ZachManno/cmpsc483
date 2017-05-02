
![We Are Penn State!](http://www.underconsideration.com/brandnew/archives/penn_state_logo_detail.png "We Are Penn State!")

## *PSU CMPSC 483 - CSE Department - Generating Natural Language Specifications from Computer Code*


The ultimate goal of this project is to develop natural language expressions (word problems) from mathematic equations.  

Example: 
<code>a + b</code>     =>     <code>There are a apples and b bananas. How much fruit is there?</code>

* [Project Report](https://drive.google.com/open?id=1dMMDF4w7kvLdJ-hLHWn3Bbbab42CPzhQ5-hcz-6UK3A) 

*** 

### Installation

1. Pull the code from github. 
2. Install [Inflect](https://pypi.python.org/pypi/inflect "Inflect Documentation"). 
   - Mac: <code>sudo -H pip install -e git+https://github.com/pwdyson/inflect.py#egg=inflect</code>
   - Windows: <code>pip install -e git+https://github.com/pwdyson/inflect.py#egg=inflect</code>



*** 

### Sample Program 
A sample execution program is available in <code>program_sample.py</code> '

Run the program. The system will prompt you to input variables and what they equate to. Be sure to include one line to be the answer. 
 
Sample Input: 
- <code>a = 1 + 2</code>
- <code>b = x + 5</code>
- <code>ANS = a * b</code>

We also support a few **macros**, including: 
- AVG[] (Average of all values pased in) 
   - <code>AVG[X, Y, Z] </code>
- SQR[] (Square of the one value passed in) 
   - <code>SQR[x]</code>
- RAND[] (Pick a random number between 0 and the value passed in. 
   - <code>RAND[100]</code>

Follow the prompts to finsh your equation input. The system will then prompt you for the number of equations you would like to see generated. Proceed to see your output!  

*** 


### Use of Program
*Coming Soon! 

*** 

### Ideas for Future  
*Coming Soon!
This project is still in it's infant stages, however there are many exciting possible improvements/additions to the system including:
- Including support for conditional if/else statements
- A full application with an intuitive GUI to allow students to have infinite practice
- Machine learning to improve the quality of problems


*** 
### Credits 

The project wouldn't have been possible without the following contributors: 
- Rodney Wells - https://www.linkedin.com/in/rodneywells/
- Zach Manno - https://www.linkedin.com/in/zachmanno/
- Stephen Lasky - https://www.linkedin.com/in/stephen-lasky-878b51a3/
- Josh Marini 
- Dr. Stephen Shaffer (Advising) - https://www.linkedin.com/in/scs12/
