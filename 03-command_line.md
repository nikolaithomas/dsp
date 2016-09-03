# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

'unzip-' lists tests and extracts compressed files in a ZIP archive, 
'cp-' copies a file, mv- lets you move files without the mouse, 'find-' will let you search through your directories from the command line, 'rm-' lets you remove a file from the directories, 'grep <str><files>-' will find files which contain a certain word, 'who-' will output who is logged on, 'history-' will list commands you've used recently, 'top-' prints system usage and the top resource users, 'mail-' sends and recieve email from command line

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls` 
`ls -a` 
`ls -l` 
`ls -lh` 
`ls -lah`
`ls -t` 
`ls -Glp` 

`ls`  lists the contents of the current directory
`ls -a`  lists all entries even those with a .
`ls -l`  uses a long listing format with information about the contents
`ls -lh`  uses a long listing format and prints sizes in human readable format
`ls -lah`  all of the above (l,a,h)
`ls -t`  sorts the contents by modification time with the newest first
`ls -Glp`  G inhibits display of group information, l uses a long listing format with information about the contents, p appends a '/' to the directories

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -R seems really useful to trace through file paths, ls -1 makes it easier to track through the content listing visually, ls -m is also useful for getting a quick list of files w/commas, ls -u interesting as opposed to modified time, and ls -r quick way to reverse.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs allows you to execute the same command from standard input over a series of things, in order

find /tmp -name "*.tmp" | xargs rm

This will find every file name that is temporary and delete it in the /tmp directory or any directories below

 

