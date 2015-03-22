# eagle-script-generator
A python script for generating EAGLE .scr script files. The irony of generating a script with a script.

It's pretty easy to use: pick a pad size, number of pads in each direction (you can have as many as you want), run it with python, and it will generate an eagle .scr script file which you can use inside eagle to make pads quickly and accurately. It works much better than placing each pad, at least when it's an object like a DIP, SOIC, etc. It's super useful for creating BGA or other buried pad arrays where manually clicking or entering 128 commands on the eagle command editor would be suicidal.

It's free to use for whatever you want. If you build something awesome with it, buy me a coffee or something. 