### Notes

Virtuoso still uses a commandline config tool to set the root password.

Once the instance is up, ssh in 

	vagrant ssh virtuoso
	
Reconfigure the package

	sudo dpkg-reconfigure -plow virtuoso-opensource-6.1
	
Update the service config: change 'run=no' to 'run=YES'

	sudo pico /etc/default/virtuoso-opensource-6.1
	
Start virtuoso

	sudo service virtuoso-opensource-6.1 start
	

Now you can visit the virtuoso page at [http://192.168.100.30:8890](http://192.168.100.30:8890)


### adding write permissions (via Nolan)

Enable SPARUL

Execute  the following from isql as the "dba" user:

	grant execute on SPARQL_INSERT_DICT_CONTENT to "SPARQL"
	
	grant execute on SPARQL_INSERT_DICT_CONTENT to SPARQL_UPDATE

this may or may not be needed if the SPARQL_UPDATE role is granted to the user

	grant execute on DB.DBA.SPARQL_MODIFY_BY_DICT_CONTENTS to "SPARQL";
	
	grant execute on DB.DBA.SPARUL_CLEAR to "SPARQL";

**note: SPARUL will only support up to 10000 lines of code at a time**