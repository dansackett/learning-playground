man COMMAND - show a help page for a command
man -k COMMAND - show man pages for similiar commands
pwd - print working directory
top - shows uptime of system, number of users, load, and running processes
ps aux - Show all processes
df -h - Show filesystem components with size, usage, and mount
du - Show current directory folders and sizes
locate PATTERN - can find files quickly
stat FILE - show file metadata
ln -s - symlinks
ln - hardlinks
wc -l FILE - Get number of lines in a file
head -n 1 - Number of lines
uniq -c - count unique records and group them
sort - sort the output
sort -h - sort by human readable numbers
sort -r - reverse sort
awk '{print 1}' - select first column of log file
lsof - list open files
lsof -p PID - list open files using process
history - loads .bash_history file
CTRL-R - Loads reverse history search
!! - Run last command
!2 - Run history command id 2
python -m SimpleHTTPServer 1234 - Serve contents of directory
iptables - Firewall
FILE | column -t - Create table based on spaces
FILE | column -t -s "DELIMETER" - Create table based on delimeter
FILE | tr ' ', ',' - Replace spaces with commas
COMMAND | tee file1 file2 file3 - Writes the command output to all files specified
md5sum FILE - Returns the MD5 checksum of a file to match against changes
uname -a - Show details about OS and Kernel
find -name PATTERN - Find files in given directory based on pattern

ifconfig - Check active network interfaces
ifconfig -a - Check ALL network interfaces
ifconfig eth0 down/up - Bring an interface up or down
ifconfig eth0 192.168.1.12 - Assign IP to interface

netstat - List all network ports

nslookup DOMAIN - Gets DNS information on a domain
nslookup -query=mx DOMAIN - Get MX record
nslookup -type=ns DOMAIN - Get name server records
nslookup -type=any DOMAIN - Query DNS
nslookup -type=soa DOMAIN - Query start of authority
nslookup -port 56 DOMAIN - Query port

dig DOMAIN - QUery DNS nameservers for info about host addresses, ns, etc
dig DOMAIN +nocomments - No comments

uptime - Get uptime of server

w - Return uptime and who commands

mysqldump -u root -p DBNAME > file.sql
