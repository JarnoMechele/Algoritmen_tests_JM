# Cheatsheet

## Programming concepts from C# to Python

This cheatsheet is copied: https://gist.github.com/DanielKoehler/606b022ec522a67a0cf3

### Variables

Python:
´´´
foo = 1
bar = "hi"
something_that_varies = 2 # Though strict immutability in Python isn't common.
something_that_varies += 1
´´´

C#:
´´´
var foo = 1; // Equivalent to: int foo
var bar = "hi"; // Equivalent to: String bar
var somethingThatVaries = 2; // Equivalent to: int somethingThatVaries
somethingThatVaries++;
´´´

### Functions

Python:
´´´
# Function definition: takes an argument
def do_domething(some_argument):
  return some_argument + 1µ

# Function use
results = do_something(3)
´´´

C#:
´´´
// Function definition: takes an integer argument, returns an integer
static int DoSomething(int some_argument)
{
  return some_argument + 1;
}

// Function use
var results = DoSomething(3);
´´´

### Conditionals

Python:
´´´
if x == 3:
    # ...
elif x == 0:
    # ...
else:
    # ...
´´´

C#:
´´´
if (x == 3)
{
  // ...
}
else if (x == 0)
{
  // ...
}
else
{
  // ...
}
// Or using a switch:
switch(x) {
  case 3:
    // ...
    break;
  case 0:
    // ...
    break;
  default:
    // ...
    break;
}
´´´

### Output to the screen

Python:
´´´
x = 5
print("x has the value %s" % x);
´´´

C#:
´´´
var x = 5;
Debug.Log("x has the value {0}", x);
´´´

### Lists of variable size

Python:
´´´
i = ["a", "b", "c"];
i.append("d");
print(i[1]); # outputs b
´´´

C#:
´´´
var i = new List<String>() { "a", "b", "c" };
i.Add("d");
Debug.Log(i[1]); // outputs b
´´´
