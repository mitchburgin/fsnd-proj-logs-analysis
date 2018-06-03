#**Proj-Log-Analysis**#

##**Project objectives:**##

Print out data from a database of news articles that answers the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

##**Setup:**##

To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

Install [VirtualBox 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
Install [Vagrant](https://www.vagrantup.com/downloads.html)
Download the [VM configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

Start the virtual machine:
1. `cd vagrant` to open the vagrant subdirectory
2. `vagrant up` to download and install the Linux operating system
3. `vagrant ssh` to log in to the virtual machine

This project analyses the data from a database of news articles that can be downloaded and initialized as follows:

1. [Download the data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
2. Unzip the archive and move newsdata.sql to the vagrant subdirectory
3. Within the vagrant subdirectory: `psql -d news -f newsdata.sql` to initalize the database
4. Move views.sql to the vagrant subdirectory
5. Create views in the database: `psql -d news -f views.sql`


##**Running the reports:**##

Once setup is done, run: `python proj-logs-analysis.py`
