# CollatzConjectureVisualization
This program is meant to visualize the Collatz Conjecture with a twist. Instead of running the conjecture once, it runs x amount of times based on user argument.  

How I Learned About The Collatz Conjecture: [Veritasium Video](https://www.youtube.com/watch?v=094y1Z2wpJg)

How It Works:

1. The `collatz(times)` runs a collatz conjecture `times` amount of times and adds each resulting number to a list called `sequence`.
2. When the resulting number is 1, the conjecture stops. It adds the ```sequence``` with an attached `sequence_key`to an dictionary object. The `collatz(times)` function then returns a dictionary object. 
3. The `graph(times)` function makes the entire program run. The `graph(times)` function makes the `collatz(times)` function run `times` amount of times (`times` is the argument for the `collatz(times)`) function. The `graph(times)` function then gets the returned dictionary with all the conjecture sequences. 
4. Then each sequence is graphed with an attached x,y coordinate. 

---

*Note that for fitting on a 1920x1080 screen, I found the log of the numbers, `math.log(math.log(dict[key][sequence_index]))`. Furthermore, to make each distinct point visible, I multilpe that resulting number by `margin_size_y/x`.*


