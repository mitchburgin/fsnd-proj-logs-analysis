Project objectives:

Output data from a newspaper database to answer the following questions:
q1 - What are the most popular three articles of all time?
q2 - Who are the most popular article authors of all time?
q3 - On which days did more than 1% of requests lead to errors?

Setup:

To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

- Install VirtualBox 5.1, available here: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
- Install Vagrant, available here: https://www.vagrantup.com/downloads.html
- Download the VM configuration, available here: https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip

Start the virtual machine:
- cd vagrant to open the vagrant subdirectory
- vagrant up to download and install the Linux operating system
- vagrant ssh to log in to the virtual machine

Logs Analysis analyses the data from a database that can be downloaded and initialized as follows:

- Download the data at: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
- Unzip the archive and move newsdata.sql to the vagrant subdirectory
- Within the vagrant subdirectory: psql -d news -f newsdata.sql to initalize the database
- Move views.sql to the vagrant subdirectory
- Create views in the database: psql -d news -f views.sql


Running the reports:

Once setup is done, run: python proj-logs-analysis.py fsnd-proj-logs-analysis
