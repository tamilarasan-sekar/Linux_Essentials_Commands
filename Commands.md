Commandos | Description
 --- | --- 	
ls |	Lists all the files and directories in current directory
ls /etc/ppp /etc/ssh |	The ls command also accepts multiple arguments. To list the contents of both the /etc/ppp and /etc/ssh directories, pass them both as arguments
ls /etc/ppp |	List the files and directories from /etc/ppp
ls -l |	Lists the files with size, date and permissions
ls -lr |	Lists the files with size, date and permissions and in reverse alphabetical order
ls -l /usr/bin/perl |	By default the -l option of the ls command displays files sizes in bytes
ls -lh |	Lists the files with size, date and permissions and size of the file in human readable form i.e KB, MB and GB
ls -l --human-readable /usr/bin/perl|	Equivalent option for h. Supported mostly in modern Linux System
ls |	Lists all the files and directories in current directory
cal 2030 |	Displays the calendar for 2030
history |	Displays the history of the commands executed
!3 |	Executes the third from history
history 3 |	Displays last three history of commands
!-3 |	Executes the third command on the history list from the last
!ls |	Executes the most recent ls command
!! |	Executes the last recent command from the history list
variable1='Something' |	Assigns Something to variable1
echo $variable1 |	Displays the value of variable1
HISTSIZE=500 |	Changes the value to 500
env \| grep variable1 |	Searches and displays the variable1 if found
export variable2='Else' |	Assigns Else to variable2 and exports it as global variable
env \| grep variable2 |	Searches and displays the variable2 if found
variable1=$variable1' '$variable2|	Updates variable1 as variable1+variable2
echo $variable1|	Displays the value of variable1
unset variable2 |	Removes variable2
PATH=/usr/bin/custom:$PATH |	When updating the PATH variable, always include the current path, so as not to lose access to commands located in those directories. This can be accomplished by appending $PATH to the value in the assignment expression. Recall that a variable name preceded by a dollar sign represents the value of the variable.
which cal |	Searches for the location of cal command by searching the PATH variable
type cal |	Determines the type of command. If its external it will display the path of binary
type echo |	Determines the type of command. If its internal it will display as built-in
which echo |	Searches for the location of echo command by searching the PATH variable
type -a echo|	Determines the type of command. -a option of the type command displays all locations that contain the command
alias mycal="cal 2019" |	Sets mycal as alias to cal 2019
&nbsp;|	Aliases created this way only persist while the shell is open. Once the shell is closed, the new aliases are lost. Additionally, each shell has its own aliases, so aliases created in one shell won’t be available in a new shell that’s opened.
mycal |	Displays Calendar for 2019
type ll |	The type command can identify aliases to other commands
type -a ls |	The type command can identify aliases to other commands. Displays the alias created for ls if any. -a option of the type command displays all locations that contain the command
my_report |	Invokes or executes the function
echo "The path is $PATH" |	Displays The path is /usr/bin/custom:/home/sysadmin/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games. Variable Substitution works with in double quotes.
echo The car costs $100 |	Displays The car costs 00
echo 'The car costs $100'|	Displays The car costs $100. With in single quotes variable substitution will not work
echo "The service costs $1 and the path is $PATH"|	Displays The service costs  and the path is /usr/bin/custom:/home/sysadmin/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
echo 'The service costs $1 and the path is $PATH'|	Displays The service costs $1 and the path is $PATH
echo The service costs \$1 and the path is $PATH|	Displays The service costs $1 and the path is /usr/bin/custom:/home/sysadmin/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
date |	Displays todays date and time
echo Today is date |	Displays Today is date
echo Today is \`date\`|	Displays Today is Sat May 13 16:34:29 UTC 2023
&nbsp; |	Within `` executes that command
cal 1 2030; cal 2 2030; cal 3 2030|	Displays Jan, Feb, March months Calendars of 2030
ls /etc/ppp && echo success |	Lists the directory and prints success if the directory exists
ls /etc/junk && echo success |	Lists the directory and prints success if the directory exists. If not error will be thrown
ls /etc/ppp \|\| echo failed |	Lists the directory or prints failed
ls /etc/junk \|\| echo failed |	Lists the directory or prints failed. If the directory does not exist then failed will be printed
ls|	Lists the files and directories
ls -l |	Lists the files with size, date and permissions
ls -l /tmp|	Lists the attributes of files and directories of /tmp
whoami |	Displays the user name of the current user
uname |	Displays the kernel you are using
uname -n |	Displays the network node hostname
uname --nodename |	Displays the network node hostname
pwd |	Prints working directory
echo Hi |	Displays Hi
history|	Displays the history of the commands executed
clear|	Clears the screen
history 5 |	Displays last Five history of commands
!9 |	Executes the ninth command from history
&nbsp;|	Up arrow key will provide the history of commands one by one
echo Hello Student|	Displays Hello Student on the screen
echo $HISTSIZE |	Displays History Size. The HISTSIZE variable defines how many previous commands to store in the history list.
echo $PATH |	Displays the value of the PATH variable
which date |	which command to determine if there is an executable file. The output of the which command tells you that when you execute the date command, the system will run the command /bin/date. The which command makes use of the PATH variable to determine the location of the date command
type cd |	type command can be used to determine information about command type. Determines the type of command. If its external it will display the path of binary. If its internal it will display as built-in
which ls |	Displays the path of the command from the PATH variable
type cp |	For external commands, the type command displays the location of the command
which cp |	Displays the path of the command from the PATH variable
type -a ls |	a option of the type command displays all locations that contain the command as well as aliases
alias |	To determine what aliases are set on the current shell use the alias command
type vi |	Type command can be used to determine information about command type. Determines the type of command. If its external it will display the path of binary. If its internal it will display as built-in
cd /bin |	Changes from the current directory to /bin
type vlc |	Displays the path of vlc from PATH variable if its installed
cd |	Changes from the current directory to users home directory
echo Today is \`date\` |	Displays Today is Sat May 13 16:34:29 UTC 2023
echo Today is $(date) |	Another way of substitution
echo This is the command '\`date\`'|	Displays This is the command \`date\`
echo This is the command \\\`date\\\`|	Displays This is the command \`date\`
echo This is the command "\`date\`"|	Displays This is the command Sat May 13 18:17:10 UTC 2023
echo D*|	Displays directories that starts with D
echo "D*"|	Displays D*
echo Hello; echo Linux; echo Student|	Displays Hello Linux Student (on each line)
false; echo Not; echo Conditional|	While you can't see from the output of the false command, it did execute. However, when commands are separated by the ; character, they are completely independent of each other
echo Start && echo Going && echo Gone|	Displays Start Going Gone on each line. Because each echo statement executes correctly, a return value of success is provided, allowing the next statement to also be executed
echo Success && false && echo Bye|	Displays Success.The first echo command succeeds and we see its output. The false command executes with a failure result, so the last echo statement is not executed
false \|\| echo Fail Or|	Displays Fail Or
true \|\| echo Nothing to see here|	Displays(nothing)
&nbsp; | &nbsp;
man ls |	Displays the manual page for ls command
man man |	Displays man page about man
man passwd |	Displays under which section the command was found
man -f passwd |	-f allows to search with command or the term
&nbsp;|	whatis displays the same output as above
man 5 passwd |	Searches the 5th section for passwd
man -k copy |	-k option to the man command searches both the names and descriptions of the man pages for a keyword
&nbsp;|	apropos command also does the same thing as man-k
whereis ls |	This command searches for commands, source files and man pages in specific locations where these files are typically stored
locate gshadow |	Searches for file or directory with the name gshadow. This command searches a database of all files and directories that were on the system when the database was created. Typically, the command to generate this database is run nightly. Any files created today will not be searchable with the locate command. If root access is available, it’s possible to update the locate database manually by running the updatedb command. Regular users cannot update the database file
locate -c passwd |	Displays the number of files matched the text passwd
locate -c -b passwd |	Displays only the number of files that has the search text in the base name of the filename
locate -b "\passwd" |	Limits the output to filenames that exactly matches the term passwd
info ls |	Displays info page for the ls command. Navigate the document using the arrow keys. The items under the menu are hyperlinks that link to nodes that describe more about the ls command. For example, placing the cursor on the line * Sorting the output:: and pressing the Enter key, leads to a node that describes sorting the output of the ls command. Note that going into the node about sorting leads into a sub-node of the original. To go back to the previous node, use the U key. While U leads to the start of the node one level up, the L key returns to the same location as before entering the sorting node
info |	Execute the info command without any arguments to be taken to the top level of the documentation. This is a good starting point to explore many of the features offered
cat --help |	This option is useful to learn the basic usage of a command quickly without leaving the command line
date|	Displays the current date and time
man date |	Displays the manual page for date command. Documents that are displayed with the man command are called "Man Pages"
man -k password |	-k option to the man command searches in both the names and descriptions of the man pages for a keyword
apropos password |	There is no difference between man -k and the apropos command
man -f passwd |	Displays the pages that matches the name passwd
&nbsp;|	whatis displays the same output as above
man 5 passwd |	To display a man page for a different section, provide the section number as the first argument to the man. q to return to the system prompt
whatis passwd |	Displays all man page sections for a name
info date |	Almost all system features (commands, system files, etc.) have man pages. Some of these features also have a more advanced feature called info pages. While viewing the info page from the previous step, type Shift and the letter h to see a list of movement commands. Note that they are different from the movement commands used in man pages. After reading the movement commands, type the letter l (lowercase L) to return to viewing the document
date --help |	Another way of getting help is by using the --help option to a command. Most commands allow you to pass an argument of --help to view basic command usage
ls /usr/share/doc |	Some system features also have more detailed help documents located in the /usr/share/doc directory structure Execute the following command to view the contents of this document
locate crontab |	Searches for files that have crontab as part of their name. An easy way to search for a file is to use the locate command
locate -b "\crontab" |	Finds files that are just named crontab
whereis passwd |	Finds where a command (or its man pages) is located
&nbsp; | &nbsp;
ls / |	lists the contents of the root directory
pwd |	To determine where the user is currently located within the filesystem. print working directory command can be used
cd Documents |	Changes the current directory to Documents
cd |	Changes to home directory i.e /home/<user>
cd Junk |	Changes the directory to Junk if exists. If not error will be thrown
cd /home/sysadmin |	Changes the current directory to /home/sysadmin
pwd |	Prints Working Directory
cd /home/sysadmin/Documents/School/Art|	Changes the current directory to Art (Absolute Path)
cd Art|	Changes the current directory to Art (Relative Path)
cd School/Art|	Changes the current directory to Art (Relative Path)
pwd|	Prints Working Directory
cd ../../Downloads |	From the current Directory It Navigates two levels up and goes to Downloads(Relative Path)
ls /var |	Lists the files of the directory /var
type ls |	Lists the alias assigned to ls
ls |	Lists the files of the current directory
\ls |	To avoid using the alias, place a backslash character \ in front of your command
ls -a |	ls command omits hidden files by default. -a option displays all the hidden files as well. A hidden file is any file (or directory) that begins with a dot . character
ls -l /var/log/ |	Each file has details associated with it called metadata. This can include information such as the size, ownership, or timestamps. To view this information, use the -l option to the ls command
ls -l /var/log/lastlog|	Displays the file information such as the size, ownership, or timestamps.The -l option to the ls command displays file sizes in bytes. For text files, a byte is 1 character. For smaller files, byte sizes are fine. However, for larger files, it is hard to comprehend how large the file is
ls -lh /var/log/lastlog|	Displays the file size in a more human-readable size, like megabytes or gigabytes. The -h option must be used with the -l option
ls -d |	When the -d option is used, it refers to the current directory, and not the contents within it. Without any other options, it is rather meaningless. Recall that the current directory is always referred to with a single period . character. To use the -d option in a meaningful way requires the addition of the -l option
ls -ld |	This indicates that the current directory is being listed, and not the contents
ls -R /etc/ppp |	Performs a recursive listing i.e it will list all the files from the dub directories. Be careful with this option; for example, running the command on the root directory would list every file on the file system, including all files on any attached USB device and DVD in the system. Limit the use of recursive listings to smaller directory structures.
ls /etc/ssh |	Lists the files of the /etc/ssh. By default, the ls command sorts files alphabetically by file name
ls -S /etc/ssh |	Sorts the files by size i.e largest to smallest
ls -lS /etc/ssh |	Lists files from largest to smallest and displays the actual size of the file.
ls -lSh /etc/ssh |	Lists files from largest to smallest and displays the actual size of the file. -h option to display human-readable file sizes
ls -tl /etc/ssh |	-t option sorts files based on the time they were modified. It will list the most recently modified files first. It is important to remember that the modified date on directories represents the last time a file was added to or removed from the directory.
ls -t --full-time /etc/ssh |	If the files in a directory were modified many days or months ago, it may be harder to tell exactly when they were modified, as only the date is provided for older files. For more detailed modification time information you can use the --full-time option to display the complete timestamp (including hours, minutes, seconds). It will assume the -l option automatically
ls -lrS /etc/ssh |	-r option reverse sort the file based on file size smallest to largest
ls -lrt /etc/ssh |	-t list files by modification date from newest to oldest, r option reveres it and displays from oldest to newest
pwd |	Prints working directory
echo $HOME |	Displays the HOME path i.e /home/sysadmin
cd / |	Changes the directory to /(root)
cd |	Changes the directory to home i.e /home/sysadmin
cd /home |	Changes the directory to /home
pwd |	Prints the working directory
cd ~ |	Changes the directory to home
pwd |	Prints the working directory i.e /home/sysadmin
cd ~sysadmin |	Changes the directory to home of sysadmin i.e /home/sysadmin
cd ~/|	Changes to home directory of the current user
echo ~ ~sysadmin ~root ~mail ~nobody|	Prints home directory of current user
&nbsp;|	Prints home directory of sysadmin
&nbsp;|	Prints root directory
&nbsp;|	Prints mail path
&nbsp;|	Prints nonexistent path
cd ~root |	Changes to /home directory, but throws error since current user dont have access
cd /usr/bin |	Changes the directory to bin
cd /usr |	Changes the directory to usr
cd /usr/share/doc |	Changes the directory to /usr/share/doc
cd bash |	Changes the directory to bash i.e /bash
cd .. |	Changes the directory above the current directory
pwd |	Prints the working directory i.e /usr/share/doc
cd ../dict |	Changes up one level from the current directory and then down into the dict directory
cd |	Changes the current directory to Home Directory
ls |	Lists the files in Home Directory
ls -a |	Displays all the files from the current directory including the hidden ones
ls -l /etc/hosts |	Lists all the file attributes such as the size, ownership, or timestamps
ls -R /etc/udev |	Recursively lists the files from all the subdirectories
ls -d /etc/s* |	Lists all the directories that starts with s under /etc. * character can match "zero or more of any characters" in a filename. Note that the -d option prevents files from subdirectories from being displayed. It should always be used with the ls command when you are using file globbing
ls -d /etc/???? |	Displays all of the files in the /etc directory that are exactly four characters long.The ? character can be used to match exactly 1 character in a file name
ls –d /etc/[abcd]* |	Displays all the directories that starts with letter a/b/c/d. By using square brackets [ ] you can specify a single character to match from a set of characters
&nbsp; | &nbsp;
echo /etc/t* |	Displays all the files that starts with t
echo /etc/*.d |	Displays all the files that ends with .d
echo /etc/r*.conf |	Displays all the files that starts with r and ends with .conf
echo /etc/t??????? |	Displays all of the files in the /etc directory that begin with the letter t and have exactly 7 characters after the t character
echo /etc/*???????????????????? |	Displays files in the /etc directory with twenty or more characters in the filename
echo /etc/*.??? |	Displays files with three-letter extensions
echo /etc/[gu]* |	Pattern matches any file that begins with either g or u character and contains zero or more additional characters
echo /etc/[a-d]* |	Pattern matches all files that begin with any letter between and including a and d
echo /etc/*[0-9]* |	Pattern displays any file that contains at least one number
echo /etc/*[9-0]* |	If an invalid order is provided, no matches will be made
echo /etc/[!a-t]* |	Matches any file that does not begin with a to t
ls /etc/a* |	Lists the contents of the directory that starts with a
ls /etc/adduser.conf |	Lists the filename ie adduser.conf
ls -l /etc/adduser.conf|	Lists the filename ie adduser.conf with size, permissions, type, date, time etc.
ls /etc/apparmor |	Lists the contents of the directory apparmor
ls /etc/ap* |	Lists the contents of the directory that starts with ap
ls /etc/x* |	Lists the contents of the directory that starts with x
ls -d /etc/x* |	Lists the name of the directories that starts with x
cp /etc/hosts ~ |	Copies hosts to home directory with the same name ie hosts
cp -v /etc/hosts ~ |	Copies hosts directory to home directory. The -v option causes the cp command to produce output if successful. The -v option stands for verbose
cp /etc/hosts ~/hosts.copy |	Copies hosts directory and pastes as hosts.copy in the destination
cp -v /etc/hosts ~/hosts.copy |	Same as above command verbose enabled
cp /etc/hostname example.txt |	Copies hostname to example.txt
ls -l example.txt |	Lists the file atrributes of example.txt
cat example.txt |	Displays the contents of example.txt
cp /etc/timezone example.txt |	Copies timezone to example.txt
cp -i /etc/hosts example.txt |	Copies the file from source to destination in interactive mode. For example if the same file exists in destination already -i option pprompts you to enter y or n. Based the yes or no option the file will be overwritten or not overwritten
cp -i /etc/skel/.* ~ |	Copies all the files from source to destination in interactive mode
cp -n /etc/skel/.* ~ |	Copies all the files from source to destination. If the same file exists in destination it will not be overwritten. -n option is used to overwrite
cp -r /etc/skel/.* ~ |	Copies all the folders and files from source to destination recursively
mv hosts Videos |	Moves the hosts file to Videos Directory
ls Videos |	Lists the files and folders in Videos directory
mv /etc/hosts . |	Moves the hosts file from /etc to current Directory
mv example.txt Videos/newexample.txt|	Moves the file example.txt from current directory to Videos and renames the file name as newexample.txt
ls Videos|	Lists the files and folders in Videos directory
cd Videos|	Navigates from the current Directory to Videos directory
mv newexample.txt myfile.txt|	Renames the file newexample.txt to myfile.txt
touch sample |	Creates a empty file without any data
ls -l sample |	Lists the file attributes of sample file
rm sample |	Removes the sample file permanently
rm hosts.copy |	Removes the hosts.copy file permanently
touch sample.txt example.txt test.txt|	Creates multiple empty files without any data
rm -i *.txt |	Removes all the .txt files in interactive mode. User will be prompted for each file
rm Videos |	Throws an error since Videos is a directory. By default rm without any option cant delete a directory
rm -r Videos |	Removes the directory and the contents of the Videos directory
rmdir Documents |	Removes the directory Documents if its empty
mkdir test |	Creates a new directory test in the current directory
echo * |	Displays all the files and directories in the current location
echo D* |	Displays all the files and directories that starts with D character and have zero or more of any other character after D
echo P* |	Displays all the files and directories that starts with P character and have zero or more of any other character after P
echo *s |	Displays all the files and directories that has zero or more characters and ends with s
echo D*n*s |	Displays all the files and directories that starts with D and ends with s with n in between and zero or more characters after D and n
echo ?????? |	Displays all the files and directories that has 6 characters. Each ? character must match exactly one character in a filename-no more and no less than one character
echo D???????? |	Displays all the files and directories that starts with D followed by 8 characters
echo ?????*s |	Matches filenames that begin with any five characters, then have zero or more of any characters and then end with a s character
echo [DP]* |	The first character of the file name can be either a D or a P
echo [!DP]* |	The first character can be any character except a D or P
echo [D-P]* |	The first character of the file name can be any character ranging from D till P
echo [!D-P]* |	Any single character will match as long as it is not between the letters D and P
cp /etc/hosts hosts|	Copy hosts file from /etc/hosts to the current directory with name as hosts
cp -v /etc/hosts hosts |	Copies hosts file from /etc/hosts to the current directory in verbose mode i.e source target will be shown
rm hosts|	Removes hosts file from the current directory
cp -v /etc/hosts . |	Copies hosts file from /etc/hosts to the current directory '.' in verbose mode i.e source target will be shown
rm hosts |	Removes hosts file from the current directory
cd /etc |	Changes the current directory to /etc
ls -l hosts |	Lists the file attributes of hosts file
cp –p hosts /home/sysadmin |	Copies the file to /home/sysadmin and preserves file attributes i.e the date and permission modes were preserved
cd |	Changes the directory to /home/sysadmin (user)
ls –l hosts |	Lists the file attributes of hosts file
rm hosts |	Removes hosts file from the current directory
cp -p /etc/hosts ~ |	Copies the file to home directory and preserves file attributes i.e the date and permission modes were preserved
cp hosts newname |	Copies the hosts file in the current directory and names it as new name
ls –l hosts newname |	Lists the file attributes of hosts file newname
rm hosts newname |	Removes the hosts and newname file
mkdir Myetc |	Creates a new directory named Myetc
cp –R /etc/udev Myetc |	Recursively copies all the files and directories from /etc/udev to Myetc
ls –l Myetc |	Lists the file attributes of Myetc
ls –lR Myetc |	Recursively lists all the files and directories attributes of Myetc
rm -r Myetc |	Removes directories and their contents recursively
touch premove |	Creates an empty file called premove
mv premove postmove |	This command “cuts” the premove file and “pastes” it to a file called postmove
rm postmove |	Removes postmove file
&nbsp;|	&nbsp;
cd Documents |	Changes the directory to Documents
ls -l longfile* |	Lists the file attributes of longfile followed by any charcter/characters
gzip longfile.txt |	Compresses longfile.txt using Lempel-Ziv data compression algorithm
gzip -l longfile.txt.gz |	Lists the info of the zip like size before & after compression, ratio and original file name
gunzip longfile.txt.gz |	Unzips the file
tar -cf alpha_files.tar alpha*|	Makes tarfile or tarball by combining all the files that starts with alpha
ls -l alpha_files.tar|	Lists the file attributes of alpha_files.tar
tar -czf alpha_files.tar.gz alpha*|	Creates tar ball and zips it using gzip
ls -l alpha_files.tar.gz|	Lists the file attributes of alpha_files.tar.gz
gzip -l alpha_files.tar.gz|	Lists the info of the zip like size before & after compression, ratio and original file name
tar -cjf folders.tbz School|	Creates tar ball and zips it using bzip2
tar -tjf folders.tbz|	Lists the contents of folders.tbz
bunzip2 -c folders.tbz | tar -t|	The left side of the pipeline is bunzip2 –c folders.tbz, which decompresses the file, but the -c option sends the output to the screen. The output is redirected to tar –t. If you don’t specify a file with –f then tar will read from the standard input, which in this case is the uncompressed file
cd ~|	Change to user home directory
cp Documents/folders.tbz Downloads/folders.tbz|	Copy folders.tbz from Documents to Downloads
cd Downloads|	Change to Downloads directory
tar -xjf folders.tbz|	Extract contents of folders using bzip algorithm
ls -l|	List the file attributes
cd School|	Change to School directory
tar -xjvf folders.tbz|	Extract contents of folders in Verbose Mode
tar -xjfv folders.tbz|	Error in Syntax f should come before file name
tar -xjvf folders.tbz School/Art/linux.txt|	Extract linux.txt Under School/Art from folders.tbz
zip alpha_files.zip alpha*|	The first argument zipfile is the name of the archive to be created, after that, a list of files to be added. The following example shows a compressed archive called alpha_files.zip being created
zip -r School.zip School|	The zip command will not recurse into subdirectories by default, which is different behavior than the tar command. That is, merely adding School will only add the empty directory and not the files under it. If you want tar like behavior, you must use the –r option to indicate recursion is to be used
unzip -l School.zip|	The –l list option of the unzip command lists files in .zip archives
unzip School.zip|	Extracts the files from School.zip. It gives several options if unzipping files will overwrite existing ones. This can be avoided by copying the zip to some other directory
mkdir tmp|	Creates a new directory tmp
cp School.zip tmp/School.zip|	Copies School.zip from the current directory to tmp
cd tmp|	Changes the current directory to tmp
unzip School.zip linux.txt|	Extracts linux.txt from School.zip. If not present error will be thrown
unzip School.zip School/Math/numbers.txt|	Extracts numbers.txt from School/Math directory
unzip School.zip School/Art/*t|	Extracts all files that ends with t from School/Art directory
cd|	Change to the users home directory
mkdir mybackups|	Creates a new directory mybackups
tar –cvf mybackups/udev.tar /etc/udev|	Create a tar of /etc/udev under mybackups
ls mybackups|	List the files and folders under mybackups
tar –tvf mybackups/udev.tar|	List the files and folders under udev.tar
tar –zcvf mybackups/udev.tar.gz /etc/udev|	Compresses the tar file using gzip
ls –lh mybackups|	Lists the file attributes and size in human readable format
cd mybackups|	Changes the directory to mybackups
ls|	Lists the files and folders in current directory
tar –xvf udev.tar.gz|	Extracts the files and folders from udev.tar.gz
ls etc|	Lists the files and folders in etc directory
ls etc/udev|	Lists the files and folders in /etc/udev directory
ls etc/udev/rules.d|	Lists the files and folders in /etc/udev/rules.d directory
tar -rvf udev.tar /etc/hosts|	To add a file to an existing archive, use the -r option to the tar command
tar –tvf udev.tar|	Lists the files and folders under udev.tar
cp /usr/share/dict/words .|	Copies the /usr/share/dict/words to the current directory
ls -l words|	Lists the file attributes of words directory
gzip words|	Compresses the words directory
ls -l words.gz|	Lists the file attributes of words.gz directory
ls -l words.gz |	Lists the file attributes for words.gz
gunzip words.gz |	Unzips words.gz in the current directory
ls -l words |	Lists the file attributes for words
bzip2 words |	Compresses the words directory using bzip2
ls -l words.bz2 |	Lists the file attributes for words.bz2
ls -l words.bz2 |	Lists the file attributes for words.bz2
bunzip2 words.bz2 |	Unzips the words.bz2 directory
ls -l words |	Lists the file attributes for words
xz words |	Compresses the words directory using xz
ls -l words.xz |	Lists the file attributes for words.xz
ls -l words.xz |	Lists the file attributes for words.xz
unxz words.xz |	Unzips the words.xz directory
zip words.zip words |	Compresses words directory using zip
ls -l words.zip |	Lists the file attributes for words.zip
zip -r udev.zip /etc/udev |	Recursively compresses the /etc/udev directory
ls -l udev.zip |	Lists the file attributes for udev.zip
unzip -l udev.zip |	Lists the files and directories of udev.zip
rm -r etc |	Removes etc and its subdirectories recursively
unzip udev.zip |	Unzips udev.zip directory. To extract the zip archive, use the unzip command without any options
&nbsp; | &nbsp;
cat food.txt |	Displays the contents of food.txt i.e Food is good
less words |	There are many movement commands for the less command, each with multiple possible keys or key combinations. While this may seem intimidating, it is not necessary to memorize all of these movement commands. When viewing a file with the less command, use the H key or Shift+H to display a help screen
head /etc/sysctl.conf|	Displays the first five lines of the file
tail -5 /etc/sysctl.conf|	Displays the last five lines of the file
head -n 3 /etc/sysctl.conf|	Displays the first three lines of the file
nl /etc/passwd|	Displays the line numbers
nl /etc/passwd | tail -n +25|	Displays from the 25th line till end
nl /etc/passwd | head -n +25|	Displays from the beginning till 25th line
nl /etc/passwd | head -n -25|	Displays all the lines except the last 25 lines For example if the file has 28 lines this will start displaying only first 3 lines
nl /etc/passwd | tail -n -25|	Displays the last 25 lines. For example if the file has 28 lines this will start displaying only from the 4th line
ls /etc|	Lists /etc
ls /etc | head|	Lists only the first 10 lines of /etc
ls /etc/ssh | nl|	Lists /etc/ssh with line numbers
ls /etc/ssh | nl | tail -5|	Lists /etc/ssh with line numbers and displays the last 5 lines
ls /etc/ssh | tail -5 | nl|	Lists only the last 5 lines of /etc/ssh and then the line numbers
echo "Line 1"|	Displays Line 1 on the terminal
echo "Line 1" > example.txt|	Writes Line1 to the example.txt file in the current directory
cat example.txt|	Displays the contents of example.txt
echo "New line 1" > example.txt|	Overwrites New line 1 to the example.txt file
echo "Another line" >> example.txt|	Appends Another line to example.txt
ls /fake|	Lists the file and directories if present
ls /fake > output.txt|	Lists the file and directories if present and output is redirected to output.txt
ls /fake 2> error.txt|	Redirects the error to error.txt file
cat error.txt|	Displays the contents of error.txt
ls /fake /etc/ppp|	Lists /fake and /etc/ppp if exists
ls /fake /etc/ppp > example.txt|	Lists /fake and /etc/ppp if exists and writes to example.txt
ls /fake /etc/ppp 2> error.txt|	Redirects the error to error.txt while listing
ls /fake /etc/ppp &> all.txt|	Redirects the output and error to all.txt
cat all.txt|	Displays the content of all.txt
ls /fake /etc/ppp /junk /etc/sound &> all.txt|	Redirects the output and error to all.txt
ls /fake /etc/ppp > example.txt 2> error.txt|	Redirects the output to example.txt and error to error.txt
cat|	Text followed by cat will be displayed on the screen after enter is pressed
cat > new.txt|	Text followed by cat will be written to new.txt
cat new.txt|	Displays the content of new.txt file
tr 'a-z' 'A-Z'|	Text followed by this command will be translated from lower case to uppercase and displayed on the terminal
tr 'a-z' 'A-Z' example.txt|	Syntax error
tr 'a-z' 'A-Z' < example.txt|	Contents of example.txt will be translated and displayed on terminal
tr 'a-z' 'A-Z' < example.txt > newexample.txt|	Contents of example.txt will be translated and written to newexample.txt
cat newexample.txt|	Displays the content of newexample.txt file
head -5 /etc/passwd > mypasswd|	The 1st 5 lines will be written to mypasswd file
cat mypasswd|	Displays the contents of mypasswd file
sort mypasswd|	Sorts the contents of mypasswd file based on alphabetic dictionary or  numeric order
sort -t: -n -k3 mypasswd|	Delimiter is : sort by field 3 in numeric order
sort -t: -n -r -k3 mypasswd|	Delimiter is : sort by field 3 in numeric reverse order
cd ~/Documents|	Change the directory Documents
cat os.csv|	Display the contents of os.csv
sort -t, -k2 -k1n -k3 os.csv|	Delimiter is , (comma) sort by field 2, 1 in numeric order and then by 3
wc /etc/passwd /etc/passwd-|	Displays the number of lines, words, bytes and file name
ls /etc/ | wc -l|	Displays the number of lines i.e files in /etc
cut -d: -f1,5-7 mypasswd|	Colon is the delimiter, Extract Field 1, 5 to 7 from mypasswd file
ls -l | cut -c1-11,50-|	Long list the files and Extract 1st till 11th character, and from the 50th Character till the end
grep bash /etc/passwd|	Searches for bash in /etc/passwd, if found displays it
grep --color bash /etc/passwd|	Searches for bash in /etc/passwd, if found highlights it
grep -c bash /etc/passwd|	Returns the count of bash found in /etc/passwd
grep -n bash /etc/passwd|	Searches for bash in /etc/passwd, if found displays it with line number
grep -v nologin /etc/passwd|	Inverts the match i.e displays all except nologin
cd Documents|	Changes the directory to Documents
grep -i the newhome.txt|	Ignores the case while finding a match
grep are newhome.txt|	Searches for are in newhome.txt
grep -w are newhome.txt|	Searches for the exact whole word
cat red.txt |	Displays the contents of red.txt
grep 'r..f' red.txt |	Displays all the words that matches r..f pattern i.e r followed by any two characters and ends with f
grep 'r..t' /etc/passwd |	Displays all the words that matches r..f pattern i.e r followed by any two characters and ends with t from the file /etc/passwd
grep '....' red.txt |	Displays all the words which has atleast 4 characters or more
cat profile.txt|	Displays the contents of profile.txt
grep '[0-9]' profile.txt|	Displays all that matches the numbers 0 to 9 in profile.txt
grep '[d-a]' profile.txt|	Invalid range it should be a-d
grep '[^0-9]' profile.txt|	Displays all that matches lines which contain non-numbers. i.e lines which only has numbers will not be displayed. Lines which has alphabets and numbers will be displayed. Example below
cat red.txt |	Displays the contents of red.txt
grep 're*d' red.txt |	Pattern matches re followed by zero or more occurrences of the previous letter e followed by d
grep 'r[oe]*d' red.txt |	Pattern matches r followed by zero or more occurrences of o or e followed by d
grep 'z*' red.txt |	Pattern matches zero or more occurrences of the previous character to * i.e z
grep 'e*' red.txt |	Pattern matches zero or more occurrences of the previous character to * i.e e
grep 'ee*' red.txt |	Pattern ee* effectively matching every line which contains at least one e.
grep 'root' /etc/passwd|	Pattern matches root in the files
grep '^root' /etc/passwd|	Pattern matches root only at the start of the line
cat alpha-first.txt|	Dislays the contents of alpha-first.txt
grep 'r$' alpha-first.txt|	Pattern matches only r at the end of the line
cat newhome.txt|	Displays the contents of newhome.txt
grep 're*' newhome.txt|	Pattern matches r followed by zero or more occurrences of e
grep 're\*' newhome.txt|	Pattern matches re followed by *
grep -E 'colou?r' spelling.txt|	Pattern matches Zero or one occurrence of previous character
grep -E 'e+' red.txt|	Pattern matches One or more occurrence of previous character
grep -E 'gray|grey' spelling.txt|	Pattern matches either grey or grey
echo "Hello World"|	Displays Hello World on the terminal
echo "Hello World" > mymessage|	Redirects Hello World to mymessage
cat mymessage|	Displays the contents of mymessage
echo "Greetings" > mymessage|	Overwrites Grretings to mymessage file
find ~ -name "*bash*"|	Searches for files beginning in your home directory containing the name bash
find /etc -name hosts|	Searches for hosts file in /etc directory. If no permission error will be displayed
find /etc -name hosts 2> err.txt|	Searches for hosts file in /etc directory. If not found writes the error to err.txt
cat err.txt|	Displays the contents of err.txt
find /etc -name hosts > std.out 2> std.err |	Searches for hosts file in /etc directory. If found the output will be redirected to std.out and error to std.err
cat std.err|	Displays the contents of std.err
cat std.out|	Displays the contents of std.out
find /etc -name hosts > find.out 2>&1|	Redirect both output and error to find.out. The 2>&1 part of the command means send the stderr channel 2 to the same place where stdout channel 1 is going
cat find.out|	Displays the contents of find.out
tr a-z A-Z|	Translates Small letters  to Capital letters. Note: Press Control+d, to signal the tr command to stop processing standard input
tr A-Z a-z > myfile|	Translates the capital letters to small letters received as input and writes it to myfile. Press the Enter key to make sure your cursor is on the line below "This works!", then use Control+d to stop input
cat myfile|	Displays the contents of myfile
tr a-z A-Z < myfile|	Translates the small letters to capital letters from myfile and displays on the screen
ls -l /etc | more|	Lists all the files and directories under /etc that can be viewable in display screen, pressing spacebar will scroll through and ctrl+c will quit
cut -d: -f1 /etc/passwd|	Delimiter is : and extracts the field 1 based on the delimiter from passwd
cut -d: -f1 /etc/passwd | sort |	Delimiter is : and extracts the field 1 based on the delimiter from passwd and sorts it alphabetically (default)
cut -d: -f1 /etc/passwd | sort | more|	Delimiter is : and extracts the field 1 based on the delimiter from passwd and sorts it alphabetically (default), to avoid scrolling more is used
cat /etc/passwd|	Displays the contents of the passwd file
more /etc/passwd|	Displays the contents of passwd file but only the viewable amount. SPACE bar to view the rest of the content and h to view the help screen
less /etc/passwd|	Displays the contents of passwd file viewable in display area
head /etc/passwd|	Displays only the first 10 lines of passwd file
tail /etc/passwd|	Displays the last ten lines of passwd file
head -2 /etc/passwd|	Displays the first 2 lines of passwd file
ls /etc | tail -5|	Lists the last 5 lines
head -n -20 /etc/passwd |	Excludes last 20 lines and displays the rest
cd /etc|	Changes the directory to etc
grep sshd passwd|	Higlights the string sshd that matches in the passwd file
grep root passwd|	Higlights the string root that matches in the passwd file
grep '^root' passwd|	Higlights the string root that matches at the beginning of the line in passwd file
grep 'sync' passwd|	Higlights the string sync that matches in the passwd file
grep 'sync$' passwd|	Higlights the string sync that matches at the end of the line in passwd file
grep '.y' passwd|	Higlights the strings that matches any character followed by a 'y'
grep 'sshd|root|operator' passwd|	Displays nothing
grep -E 'sshd|root|operator' passwd|	Higlights the strings sshd or root or operator if matches
egrep 'no(b|n)' passwd|	Matches and highlights nob or non
head passwd | grep '[0-9]'|	Higlights the matched numbers in the range given
grep -E '[0-9]{3}' passwd|	Higlights the matched numbers in the range given but only the 3 digit numbers
&nbsp; | &nbsp;
vi test.sh |	Opens a sh file in vi editor
sh test.sh |	Passes test.sh as an argument to Shell
./test.sh |	Executes test.sh file but throws error if execute permission is not present
chmod +x ./test.sh |	Adds execute permission to test.sh file
./test.sh |	Executes test.sh file
echo "Hello there! Here is the calendar for this month:" |	Displays "Hello there!  Here is the calendar for this month:"
cal|	Displays todays calendar
ls -l sample.sh|	Lists the file attributes of sample.sh
chmod a+x sample.sh |	Adds execute permissions to all i.e users, groups and others
ls -l sample.sh |	Lists the file attributes of sample.sh
./sample.sh |	Executes sample.sh
vi sample.sh |	Opens sample.sh in VI Editor
cat sample.sh |	Displays the contents of sample.sh
sample.sh |	Executes sample.sh but throws error
echo $PATH|	Displays the PATH variable
echo $PATH |	Displays the PATH variable
mkdir bin |	Creates a directory bin
mv sample.sh bin |	Moves sample.sh from current directory to bin
vi drive.sh|	Opens drive.sh in the vi editor
cat drive.sh|	Displays the contents of drive.sh
chmod a+x drive.sh|	Provides execute permission to all the users and groups
./drive.sh|	Executes drive.sh
vi check.sh |	Opens check.sh in the vi editor
cat check.sh|	Displays the contents of check.sh
chmod a+x check.sh|	Provides execute permission to all the users and groups
./check.sh|	Executes check.sh
vi num.sh |	Opens num.sh in the vi editor
cat num.sh|	Displays the contents of num.sh
chmod a+x num.sh|	Provides execute permission to all the users and groups
./num.sh|	Executes num.sh
&nbsp; | &nbsp;
arch|	Gives which family the CPU of the current system belongs to
lscpu|	Gives more details about the CPU
free -m|	Lists the memory and swap space details in MB -g for gigabyte
lspci|	Displays all of the devices connected by pci bus
lsusb|	Displays the devices connected to the system via USB
ls /dev/sd*|	Lists the hard disks and its partitions
fdisk -l /dev/sda|	Displays the details about partitions
head -n 20 /proc/cpuinfo|	Displays the first 20 lines of CPU information from proc file
free -g|	Displays how much memory and swap space is used in Gigabytes
lspci -k|	The-k option to show devices along with the kernel driver and modules used
lsmod|	Displays the currently loaded modules
fdisk|	Lists the disk partitions
fdisk -l|	Lists the partition tables for the specified devices and then exits
&nbsp; | &nbsp;
su -|	Swiches from current User to root
cat /proc/sys/net/ipv4/icmp_echo_ignore_all |	Lists the contents of the file
ping -c1 localhost|	Pings the local host
echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all |	Writes 1 to the file
pstree|	Displays the family tree of parent and child couplings of processes
ps|	The ps command only shows the current processes running in the current shell
ps --forest|	Similar to the pstree command, it shows lines indicating the parent and child relationship
ps aux|	Displays all running processes on the system
ps aux | head|	Displays only the first 10 running processes on the system
ps -ef|	Displays all running processes on the system
ps -ef | head|	Displays only the first 10 running processes on the system
ps -e | grep firefox|	Filters only the firefox process if found
ps -u sysadmin|	Displays the running processes of a specific user i.e sysadmin
ps -u root|	Displays the running processes of a specific user i.e root
top|	The top command has a dynamic, screen-based interface that regularly updates the output of running processes. By default, the output of the top command is sorted by the percentage % of CPU time that each process is currently using, with the higher values listed first, meaning more CPU-intensive processes are listed first. There is an extensive amount of interactive commands that can be executed from within the running top program. Use the H key to view a full list.
cat /proc/loadavg|	The load averages shown in the first line of output from the top command indicate how busy the system has been during the last one, five and fifteen minutes. This information can also be viewed by executing the uptime command or directly by displaying the contents of the /proc/loadavg file
free|	free command without any options provides a snapshot of the memory being used at that moment
free -s 10|	Displays the memory usage details and updates it for every 10 seconds
file /var/log/wtmp|	Displays whether the file is binary i.e data or text
lastb /var/log/btmp|	Displays contents of the binary file i.e data but requires root privilege
last /var/log/wtmp|	Displays contents of the binary file i.e data
dmesg | grep -i usb|	dmesg command can be used to view the kernel ring buffer, which holds a large number of messages that are generated by the kernel. grep searches for usb by ignoring the case
su|	Switch User
ls /proc |	Lists the /proc directory
cat /proc/1/cmdline; echo|	Displays the information from the cmdline file. echo keeps the prompt in a new line
ps -p 1 |	Displays information about the process1
cat /proc/cmdline|	Displays the arguments that were passed to the kernel at boot time. This output contains all of the information, such as command line parameters, special instructions, etc., that was passed to the kernel when it was first started.
ping localhost > /dev/null|	The system will continue to ping until the process is terminated or suspended by the user. Terminate the foreground process by pressing Ctrl-C.
ping localhost > /dev/null &|	Pings the local host, ampersand & to the end of the command, the process is started in the background, allowing the user to maintain control of the terminal
jobs |	Displays the jobs that are running in the current terminal
fg %1 |	Brings the first job to the foreground. To suspend (pause) the process and regain control of the terminal, type Ctrl-Z
bg %1 |	Move the first job to run in background
kill %3 |	Terminates the third job
killall ping|	Kills all the ping jobs
top|	Displays the processes, CPU, memory etc. The output of the top command changes every two seconds.
sleep 888888 &|	The sleep command is typically used to pause a program (shell script) for a specific period of time. In this case it is used just to provide a command that will take a long time to run.
ps |	Displays the processes that are running under current shell
kill 134 |	Terminates the 134th Process
pkill -15 sleep|	Terminates sleep process with signal code 15
ps|	Lists the processes running in the current shell
ps -e|	Displays all the processes
ps -o pid,tty,time,%cpu,cmd|	Displays the processes with the columns specified as options. The ps command with the -o option to specify which columns to output.
ps -o pid,tty,time,%mem,cmd --sort %mem |	Sorts the processes list in ascending order based on %memory
ps -o pid,tty,time,%mem,cmd --sort -pid |	Sorts the processes list in descending order based on pid
ps -o pid,tty,time,%mem,cmd --sort +pid |	Sorts the processes list in ascending order based on pid
free |	The ps command can show the percentage of memory that a process is using, the free command will show overall system memory usage
kill 138 |	Kills the process that has the id 138
ls /var/log |	List the files and directories from var/log. System logs are stored in the /var/log directory
ssh localhost|	ssh to localhost
tail -5 /var/log/auth.log|	Displays last 5 entries of /var/log/auth.log
&nbsp; | &nbsp;
su - |	Swiches from current User to root
cat /etc/sysconfig/network-scripts/ifcfg-eth0 |	Displays the contents of ifcfg-eth0 file
cat /etc/resolv.conf|	Displays the contents of resolv.conf file
host example.com|	The host command, which works with DNS to associate a hostname with an IP address
cat /etc/hosts|	Displays the contents of hosts File
cat /etc/nsswitch.conf|	Displays the contents of nsswitch.conf file
ifconfig |	The ifconfig command stands for interface configuration and is used to display network configuration information
ip addr show|	The ifconfig command is becoming obsolete in some Linux distributions (deprecated) and is being replaced with a form of the ip command, specifically ip addr show. The ip command differs from ifconfig in several important manners, chiefly that through its increased functionality and set of options, it can almost be a one-stop shop for configuration and control of a system’s networking. While ifconfig is limited primarily to modification of networking parameters, and displaying the configuration details of networking components, the ip command branches out to do some of the work of several other legacy commands such as route and arp.
route|	Displays a table that describes where network packages are sent
route -n |	Displays the table with numeric data only
ip route or ip route show|	Displays a table that describes where network packages are sent
ping 192.168.1.2|	The ping command can be used to determine if another machine is reachable.
ping -c 4 192.168.1.2|	The ping command can be used to determine if another machine is reachable. -c option followed by a number indicating how many iterations you desire.
netstat -i|	Displays statistics regarding network traffic
netstat -r|	Displays the routing information
netstat -tln|	Lists all the open ports. -t stands for TCP, -l stands for listening (which ports are listening) and -n stands for show numbers, not names.
netstat -tl|	Lists all the open ports.Sometimes showing the names can be more useful. This can be achieved by dropping the -n option
ss|	Displays what connections are currently established between their local machine and remote machines, statistics about those connections, etc. The ss command is designed to show socket statistics and supports all the major packet and socket types. Meant to be a replacement for and to be similar in function to the netstat command
ss -s|	The -s option, which displays mostly the types of sockets, statistics about their existence and numbers of actual packets sent and received via each socket type
dig example.com|	dig command, which performs queries on the DNS server to determine if the information needed is available on the server
host 192.168.1.2|	Returns the domain name, if IP address has been given
host -t CNAME example.com|	Returns the canonical name or alias
host -t SOA example.com|	Returns the primary server of the domain. Since many DNS servers store a copy of example.com, SOA Start of Authority records indicate the primary server for the domain
host -a example.com|	Returns a comprehensive list of DNS information regarding example.com
ssh bob@test|	allows you to connect to another machine across the network, log in and then perform tasks on the remote machine. If you only provide a machine name or IP address to log into, the ssh command assumes you want to log in using the same username that you are currently logged in as. To use a different username, use the syntax: username@hostname. To return back to the local machine, use the exit command
cat ~/.ssh/known_hosts|	Displays the contents of known hosts
rm ~/.ssh/known_hosts|	Removes the known hosts file
&nbsp;|	To view the table of routing information, use the route command:
grep 127.0.0.1 /etc/hosts|	Searches for 127.0.0.1 in /etc/hosts and displays it if found
ping -c4 localhost|	The ping command can be used to determine if another machine is reachable. -c option followed by a number indicating how many iterations you desire.
dig localhost.localdomain|	Returns the ip address, domain name etc buy querying the DNS server
sudo /etc/init.d/bind9 restart|	Restarts bind9 process
dig cserver.example.com|	Returns the IP address, resolve other fully-qualified domain names
dig -x 192.168.1.2|	dig command resolves the IP address 192.168.1.2 to a hostname
netstat --help|	Displays the help section for netstat
netstat -tl|	Displays the ports that are Listening to
netstat -ltn|	The -t option to the netstat command limits the listing to TCP ports; the -l option limits the output to ports with listening services; the -n shows the network addresses numerically
&nbsp; | &nbsp;
su -|	Switches from current User to root
su -l|	Switch from current user to root
su --login|	Switch from current user to root
su - root |	Switch from current user to root
id|	Displays the values for uid, gid etc
exit |	 Exits the current session
sudo head /etc/shadow |	Super do as root and displays the first 10 lines from /etc/shadow.The system will prompt for the current user's password, not the root password. If the current user is part of the sudo group, the command will be executed. By default on many Ubuntu systems, sudo commands entered after the first sudo command will be executed as root without being prompted for a password for the next 15 minutes. Other systems may have different timeouts.
tail -5 /etc/passwd |	Displays the last 5 entries of passwd file
tail -5 /etc/shadow |	Displays the last 5 entries of shadow file
getent passwd sysadmin |	Retrieves the information about the sysadmin. Another way to retrieve the account information for a user is by running the following command: getent passwd username. The getent command has the advantage over the grep command as it is also able to access user accounts that are not defined locally. In other words, the getent command is able to get user information for users who may be defined on network directory servers such as LDAP, NIS, Windows Domain, or Active Directory Domain servers.
grep mail /etc/group |	Searches for mail and highlights it. Displays the group information.
getent group mail |	Searches for the group mail and highlights it. Displays the group information.
id |	The id command is used to print user and group information for a specified user
id root |	The id command is used to print user and group information for a specified user
id -g |	Prints the primary group information for the current user
id -G |	Prints all the group information i.e Primary and Secondary of the current user
cat /etc/group | grep sysadmin |	Searches for sysadmin and highlights that line in /etc/group
who |	The who command displays a list of users who are currently logged into the system, where they are logged in from, and when they logged in
who -b -r |	 -b option shows the last time the system started [booted], and the -r option shows the time the system reached the current runlevel
w |	w command gives a more detailed view of the users who are currently on your system. Output from the w command displays a summary of how long the system has been running, how many users are logged in and the system load averages for the past 1, 5, and 15 minutes. Also displayed is an entry for each user with their login name, tty name (terminal name), host, login time, idle time, JCPU (CPU time used by background jobs), PCPU (CPU time used by the current process) and what is executing on the current command line.
last|	The last command reads the entire login history from the /var/log/wtmp file and displays all logins and reboot records by default.
&nbsp; | &nbsp;
su - |	Switch user as root (without any argument root is default)
head /etc/shadow |	Displays the first 10 lines from shadow file if the current user is a root user or displays permission denied
head /etc/passwd |	Displays the first ten lines from passwd file
grep sysadmin /etc/passwd |	Highligts sysadmin from the matched lines. The output only includes the account information for that one username
head -3 /etc/shadow |	Displays the first 10 lines from /etc/shadow if the current user is root or displays permission denied
ls -l /etc/shadow |	Lists the file attributes of /etc/shadow file
sudo head -3 /etc/shadow |	sudo command with head provides the access to view the first 3 lines of the /etc/shadow file (prompts for user password not the root password)
man 5 passwd |	Displays Manual page for passwd
grep root /etc/group |	After creating or modifying a group, you can verify the changes by viewing the group configuration information in the /etc/group file with the grep command.
getent group root |	If working with network-based authentication services, then the getent command can show you both local and network-based groups.
groupadd -g 1005 research |	The groupadd command can be executed by the root user to create a new group. The command requires only the name of the group to be created. The -g option can be used to specify a group id for the new group
grep research /etc/group |	Searches research and highlights it from /etc/group
groupadd development |	Creates a new group development
grep development /etc/group |	Searches development and highlights it from /etc/group
groupadd -r sales |	Reduces the group id of sales
getent group sales |	Gets the group info of sales
ls -l index.html |	Lists the file attributes of index.html
groupmod -n clerks sales |	Changes the group name from sales to clerks
groupmod -g 10003 clerks |	Changes the group id of clerks to 10003
find / -nogroup |	Searches for all files that are owned by just a GID (not associated with a group name)
groupdel clerks |	Deletes the group clerks
useradd -D |	The -D option to the useradd command allows you to view or change some of the default values used by the useradd command. The useradd command will now create a mail spool file.
useradd -D -f 30 |	Allows users to have expired passwords that they could still log in with for up to thirty days
grep -Ev '^|	|^$' /etc/login.defs 
useradd jane |	The only required argument for the useradd command is the name you want the account to have
useradd -u 1000 jane |	Adding the -u option to the useradd command allows you to specify the UID number. UIDs typically can range anywhere from zero to over four billion, but for greatest compatibility with older systems, the maximum recommended UID value is 60,000.
useradd -g users jane |	To specify a primary group with the useradd command, use the -g option with either the name or GID of the group. For example, to specify users as the primary group
useradd -G sales,research jane |	To make the user a member of one or more supplementary groups, the -G option can be used to specify a comma-separated list of group names or numbers. For example to specify sales and research as supplementary groups:
useradd jane |	By default, most distributions create the user's home directory with the same name as the user account underneath whichever base directory is specified in the HOME setting of the /etc/default/useradd file, which typically specifies the /home directory. For example, if creating a user account named jane, the user's new home directory would be /home/jane.
grep '/home/jane' /etc/passwd |	Searches for /home/jane on passwd file and displays that line
useradd -m jane |	m option is used to specify to the useradd command that it should not create the home directory, even if CREATE_HOME is set to yes. he -m option can be used to make the home directory.
ls -ld /home/jane |	Lists the directories with the attributes
useradd -mb /test jane |	The -b option allows you to specify a different base directory under which the user's home directory is created. For example, the following creates the user account jane with a /test/jane created as the user’s home directory
ls -ld /test/Jane |	Lists the directories with the attributes
useradd -md /test/jane jane |	The -d option allows you to specify either an existing directory or a new home directory to create for the user
useradd -mk /home/sysadmin jane |	By using the -k option with the useradd command, the contents of a different directory can be used to populate a new user's home directory. When specifying the skeleton directory with the -k option, the -m option must be used or else the useradd command will fail with an error.
ls /home/jane|	 
useradd -s /bin/bash jane |	While the default shell is specified in the /etc/default/useradd file, it can also be overridden with the useradd command using the -s option at the time of account creation
useradd -c 'Jane Doe' jane |	The -c option of the useradd command allows for the value of this field
grep jane /etc/passwd |	Searches for jane on passwd file and displays that line
grep jane /etc/shadow |	Searches for jane on shadow file and displays that line
grep jane /etc/group |	Searches for jane on group file and displays that line
grep jane /etc/gshadow |	Searches for jane on gshadow file and displays that line
ls /var/spool/mail |	In addition, if the CREATE_MAIL_SPOOL is set to yes then the mail spool file /var/spool/mail/jane is created
ls /home |	Finally, because the -m option is used, the /home/jane directory is created with permissions only permitting the jane user access, and the contents of the /etc/skel directory would be copied into the directory
passwd Jane |	Sets the initial password or changes the existing password
chage -M 60 jane|	Changes or Sets the maximum number of days before a password should be changed to 60
grep jane /etc/shadow | cut -d: -f1,5|	Extracts the fields 1 and 5 based on delimiter :
usermod -aG development jane |	Adds supplementary group development to Jane along with other groups
userdel jane |	userdel command is used to delete users
userdel -r jane |	To delete the user, home directory, and mail spool as well, use the -r option
su -|	Switch user as root (without any argument root is default), enter password when prompted
groupadd -r research |	Creates a new group research with group id in the reserved range i.e 1 to 999. With -r option, Group Identifiers (GIDs) are automatically assigned with a value of less than the lowest normal user UID. The groupadd command modifies the /etc/group file where group account information is stored.
groupadd -r sales|	Creates a new group sales with group id in the reserved range i.e 1 to 999. With -r option, Group Identifiers (GIDs) are automatically assigned with a value of less than the lowest normal user UID. The groupadd command modifies the /etc/group file where group account information is stored.
getent group research |	getent command will retrieve information about the new research group
grep sales /etc/group |	Matches the sales value from /etc/group and displays it. Another method to retrieve group information
groupmod -n clerks sales|	Changes the group name from sales to clerks
groupmod -g 10003 clerks|	Changes the group id to 10003 for clerks
grep clerks /etc/group|	Matches clerk in /etc/group and retrieves the group information. Note that any files that had been in the sales group will now have no group name and will now be orphaned files.
groupdel clerks |	Deletes the group clerks. If you decide to delete a group with the groupdel command, be aware that any files that are owned by that group will also become orphaned.
grep clerks /etc/group |	Matches clerk in /etc/group and retrieves the group information
useradd -D -f 30|	The -f 30 option specifies that users who have expired passwords can still log in for up to thirty days before their accounts are inactivated
nano /etc/default/useradd |	Opens the useradd file in nano editor. Once it is opened. Press the down arrow key to scroll to the bottom of the file. On the CREATE_MAIL_SPOOL=no line, backspace over the no and type yes. Press Ctl + X to exit and type Y. Press Enter to save your changes. This Modifies the CREATE_MAIL_SPOOL value in the /etc/default/useradd.
useradd -G research -c 'Linux Student' -m student |	Creates a new user named student who is a secondary member of the research group and a primary member of their own private group. Use a comment of Linux Student that will appear as the full name of the user when they do a graphical login. Make sure that their home directory will be created by specifying the -m option
grep student /etc/passwd |	Matches student in /etc/passwd and retrieves the user information
grep student /etc/group |	Matches student in /etc/group and retrieves the group information. The user's account information is stored in the /etc/passwd and /etc/shadow files. The user's group information can be found in the /etc/passwd and /etc/group files.
usermod -aG research sysadmin |	Adds the research group as a secondary group for the sysadmin user, 'a' should be included while adding a secondary group. Users who are actively logged into the system will not be able to use any new group memberships until the next time they log into the system.
getent group student |	Retrieves the group information for student
getent passwd student |	User information from passwd file is displayed
passwd student |	Changes the password for student. No characters will appear when typing the password.
getent shadow student |	Displays the password information for the user student
last |	Shows the current user login history
last student |	Shows the student user login history
userdel -r student |	Using the -r option with the userdel command removes the user's home directory and mail, in addition to deleting the user's account
id |	The id command can be useful for verifying which user account you are using and which groups you have are available to use
touch /tmp/filetest1 |	Creates a empty file filetest1 under /tmp
ls -l /tmp/filetest1 |	Lists the file permissions for filetest1
ls -la |	List all the files, directories and its attributes including the hidden ones
groups |	Lists the groups of the current user
newgrp research |	Changes the current primary group but temporarily
touch /tmp/filetest2 |	Creates a empty file filetest2 under /tmp
ls -l /tmp/filetest2 |	Lists the file permissions for filetest2
usermod -g groupname username |	Changes the primary group of the user permanently but requires root privileges
touch sample |	Creates a empty file sample in the current directory
ls -l sample |	Lists the file permissions for sample
chgrp research sample |	Changes the group owner of sample file to research. Note research should be one of groups for current user
chgrp development /etc/passwd |	Changes the group owner of passwd file to development. Note development should be one of groups for current user
chgrp -R development test_dir |	Recursively changes the group owner of test_dir and its subdirectories to development. Note research should be one of groups for current user
stat /tmp/filetest1 |	stat command provides more detailed information than the ls -l command. The stat command displays more detailed information about a file, including providing the group ownership both by group name and GID number. Because of this, you may consider using the stat command instead of the ls -l command when viewing permissions on a file. One big advantage of the stat command is that it shows permissions using both the symbolic and numeric methods
chown jane /tmp/filetest1 |	Changes the owner of the file to jane
chown jane:users /tmp/filetest2 |	Changes the owner of the file to jane and group to users
chown .users /tmp/filetest1 |	Changes the group of the file to users
ls -l /etc/passwd |	Lists the file permissions for passwd file
touch abc.txt |	Creates a empty file abc.txt
ls -l abc.txt |	Lists the file permissions of abc.txt
chmod g+w abc.txt |	Adds write permission to group owner
chmod ug+x,o-r abc.txt |	Adds execute permission to user and group owner and removes read permission from others
chmod u=rx abc.txt |	Gives the user owner only read and execute permissions, removing the write permission
chmod 754 abc.txt |	Changes the permission rwx to user, rx to group and r to others
umask |	The umask command is a feature that is used to determine default permissions that are set when a file or directory is created
umask 027 |	Sets the mask value, that will be subtracted from the maximum for files and directories. The new umask is only applied to file and directories created during that session. When a new shell is started, the default umask will again be in effect.Permanently changing a user's umask requires modifying the .bashrc file located in that user's home directory.
mkdir test-dir |	Creates a new test-dir directory
ls -ld test-dir |	Lists the folder permissions for test-dir
cd /tmp |	Changes the directory to /tmp
mkdir priv-dir pub-dir |	Creates two directories priv-dir and pub-dir
touch priv-dir/priv-file |	Creates a empty priv-file under priv-dir
touch pub-dir/pub-file |	Creates a empty pub-file under pub-dir
ls -l priv-dir |	Lists the files and its attributes for priv-dir
ls -l pub-dir |	Lists the files and its attributes for pub-dir
ls -ld priv-dir/ |	Lists the directory and its permissions for priv-dir
chmod o-rx priv-dir/ |	Removes the read and write permission for others
chmod a+x file |	Gives everyone execute permission
chmod g-w file |	Removes write permission for group owners
chmod go+r file |	Adds read permission for group owner and others
chmod o=rwx file |	Sets others permissions to read, write and execute
ls -ld pub-dir/ |	Lists the attributes of the directory
chmod o+w pub-dir/ |	Adds write permissions to other user
ls -l priv-dir/priv-file |	Lists the priv-file attributes
chmod g-rw,o-r priv-dir/priv-file |	Removes rw for group and r for others in priv-file
ls -l pub-dir/pub-file |	Lists the pub-file attributes
chmod a=rw pub-dir/pub-file |	Modifies the permission to have only rw for all users
ls -l pub-dir/pub-file|	Lists the pub-file attributes
echo "date" > test.sh |	Writes date to test.sh
./test.sh |	Executes the script if it has the execute permission
ls -l test.sh |	Lists the file permissions for test.sh
chmod u+x test.sh |	Adds the execute permission to test.sh
stat test.sh |	The stat command displays more detailed information about a file, including the group ownership both by group name and GID number. Use the stat command to verify the octal value for the permissions
chmod 775 test.sh |	Changes the permission to r,w,x to user, group and r,w for others
ls -ld pub-dir |	Lists the directory permissions
chown root:root pub-dir |	Changes the user and group owner to root
chown bin pub-dir/pub-file |	Changes the user owner to bin
ls -ld priv-dir |	Lists the directory permissions
ls -l priv-dir/priv-file|	Lists the file permissions
chgrp -R users priv-dir |	Changes the group permissions recursively for all files, directory and sub-directories
&nbsp; |
more /etc/shadow |	Lists the contents of shadow file
ls -l /etc/shadow|	Lists the permissions for the shadow file.
ls -l /usr/bin/passwd |	Lists the file permissions
id|	The id command can be useful for verifying which user account you are using and which groups you have are available to use
ls -l /usr/bin/wall |	Lists the file permissions
ls -l /dev/tty? |	Lists the file permissions
ls -ld /tmp/data |	Lists the directory permissions
touch /tmp/data/file.txt |	Creates an empty file
ls -ld /tmp/data/file.txt |	Lists the directory permissions
chmod g+s <file|directory> |	Sets the setgid in a symbolic method
chmod 2775 <file|directory> |	Sets the setgid in Octal method
chmod g-s <file|directory> |	Removes the setgid in a symbolic method
chmod 0775 <file|directory> |	Removes the setgid in Octal method
ls -ld /tmp |	Lists the permissions of directory
chmod o+t <directory> |	Sets Sticky bit to the directory in a symbolic method
chmod 1775 <file|directory> |	Sets Sticky bit to the directory in Octal method
chmod o-t <directory> |	Removes Sticky bit from the directory in a symbolic method
chmod 0775 <directory> |	Removes Sticky bit from the directory in Octal method
ls -i /tmp/file.txt |	Displays the inode value for file.txt
echo data > file.original |	Redirects/writes the contents of data to file.original1
ls -li file.* |	Lists all the files with their inode numbers that starts with file
ln file.original file.hard.1 |	Cretes a hard link for file.original
ls -l /etc/grub.conf |	Lists the permissions of conf file
ln -s /etc/passwd mypasswd |	Creates a soft link for /etc/passwd
ls -l mypasswd |	Lists the permissions of mypasswd file
ls -l mytest.txt |	Lists the permissions of mytest.txt file
more test.txt |	Displays the contents of test.txt
more mytest.txt |	Displays the contents of mytest.txt
rm test.txt |	Removes test.txt
ls -i file.original |	Lists the inode value for file.original
find / -inum 278772 2> /dev/null |	Finds the file that has that inode number
ls -l mypasswd |	Lists the permissions of mypasswd file
ln /boot/vmlinuz-2.6.32-358.6.1.el6.i686 Linux.Kernel |	Creates hardlink for /boot/vmlinuz-2.6.32-358.6.1.el6.i686 but throws error
ln -s /boot/vmlinuz-2.6.32-358.6.1.el6.i686 Linux.Kernel |	Creates soft link for /boot/vmlinuz-2.6.32-358.6.1.el6.i686
ls -l Linux.Kernel |	Lists the permissions of Linux.Kernel
ln /bin binary |	Creates hard link for /bin but throws error
ln -s /bin binary |	Creates hard link for /bin
ls -l binary |	Lists the permissions of binary
ls -ld /tmp |	Lists the permissions of the directory
ls -ld /var/tmp |	Lists the permissions of the directory
ls -l /usr/bin/passwd |	Lists the permissions for the passwd file.
ls -l /usr/bin/wall |	Lists the permissions of the wall file
cd |	Changes to the home directory
echo "data" > source |	Writes data to the source file
ls -li source |	Displays the inode value and the permissions of the file
ln source hardlink |	Creates a new hardlink for source
ls -li source hardlink |	Lists the permissions and inode number for both source and hardlink
ln hardlink hardlinktwo |	Creates hardlinktwo from hardlink
ls -li hardlink hardlinktwo source |	Lists the permission snd inode number of hardlink hardlinktwo and source
rm hardlinktwo |	Removes hardlinktwo
rm hardlink |	Removes hardlink
ls -li source |	Lists the inode number and permissions of the file.
ln -s source softlink |	Creates a soflink for file named source
ls -li source softlink |	Lists the inode number and the file permissions
ln -s /proc crossdir |	Creates a softlink for /proc directory
ls -l crossdir |	Lists the file permissions
