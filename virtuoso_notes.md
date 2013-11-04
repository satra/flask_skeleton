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
