1.	Gather IP Address from our pi. : //run ifconfig
2. Get the gateway address : //run netstat -nr 
![image](https://user-images.githubusercontent.com/14791021/69016974-46557880-0958-11ea-8e91-7fc4ba0dea18.png)

3.	We now need to plug this information into the Pi’s DHCP configuration file using a text editor.     //run sudo nano /etc/dhcpcd.conf
4.	On the very top of the file type in the following lines:
interface eth0 static ip_address=10.0.0.XX/24 static routers=10.0.0.1 static domain_name_servers=10.0.0.1

![image](https://user-images.githubusercontent.com/14791021/69017000-83ba0600-0958-11ea-9d4a-70b0a3b8c727.png)

5.	Reboot the pi: sudo reboot
