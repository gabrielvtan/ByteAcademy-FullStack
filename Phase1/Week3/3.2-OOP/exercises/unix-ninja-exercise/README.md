Unix Ninja Part 1
=================

Are you ready to become a Unix ninja?

Today you're going to start on the path to mastering your Terminal. If you want to be a master young grasshopper, you must not be afraid of the sandbox.

#### cat

The first command you need to know is [cat](http://en.wikipedia.org/wiki/Cat_(Unix)). cat will output a file, or "catenate" multiple files.

Try to cat both csv files in the directory, seperately and together.

You can even join them and save them combined to a new file. Do it!

#### Combine two files into one
```
cat emails.csv names.csv > combined.csv
```

#### grep

The next command we need is [grep](http://en.wikipedia.org/wiki/Grep).

Grep searches any file or output for a [regular expression](http://en.wikipedia.org/wiki/Regular_expression) you provide.

grep each csv file just for occurences of the string 'tie'.

#### Solution
```
grep tie names.csv
```

Now output both files using cat and grep them both for the string 'tie'. You'll need to use a [pipe](http://en.wikipedia.org/wiki/Pipeline_(Unix)) to pass the output of cat to grep.

#### Solution
```
cat emails.csv names.csv | grep tie > tie.csv
```

Sandbox! grep more stuff and get results from both files.

Now pipe commands you use all the time to grep - like ls, git status and anything else you can think of.

### ls -l Sample
This will return files with the REGEX name in the file name
```
ls -l | grep name 
```

#### sort

Add [sort](http://en.wikipedia.org/wiki/Sort_(Unix)) into the mix. Sort each file, and sort them combined with cat.

#### Solution
```
sort emails.csv
```

Join them with cat, pipe to grep and look for all lines that contain the string "zo" and pipe them to sort to sort them.

#### Solution
```
cat emails.csv names.csv | grep tie > tie.csv
```

#### wc

[wc](http://en.wikipedia.org/wiki/Wc_(Unix)) is word count. It will give you the number of words, lines, and characters from an output. What is the total number of full names in the name file? What is the total number of words for occurences of the string 'tie' in both files? Pipe them all together!

#### Basic wc commands
```
wc -l <filename> # prints the line count (note that if the last line does not have \n, it will not be counted)
wc -c <filename> # prints the byte count
wc -m <filename> # prints the character count
wc -L <filename> # prints the length of longest line (GNU extension)
wc -w <filename> # prints the word count

```

#### Solution
```
cat names.csv emails.csv | grep tie | wc -m
```

How about some more? How many words are in the man page for grep? How many lines contain the word "repo" in git --help?

#Help?? Don't know... how to access man page or git page 

#### Bonus - curl

curl will output a web data in your terminal. curl http://www.seamless.com and grep for all occurrences of the word "sandwich". How about we get all the links on the page? grep for occurrences of "href". How many lines are returned?

#### Links
```
curl https://www.seamless.com | grep link
```

curl [reddit](http://www.reddit.com/) and save the page to an html file.

#### HTML file save
```
curl https://www.reddit.com > reddit.html
```
