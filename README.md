# mac_changer
 This tool can be used to change any mac address temporarily provided that the system has python installed

This tool is very useful and easy to use. Using this tool, we can change the mac address of any of the interfaces in our computer to a mac address of our choice. I have created this tool using python 3.7 version. This tool can be downloaded from my git-hub repository. This tool is only created for Linux environment and will not work on Windows or OSX.

Note: Changing mac-address is a temporary process. As soon as you restart your computer your mac-address will change back to the original mac-address provided by the device manufacturer.

What is MAC ADDRESS?
->	MAC stands for Media Access Control
->	It is a permanent address which is assigned by the device manufacturer
->	It’s a physical address which you can see on your device
->	It’s unique to every device

Why change the MAC ADDRESS?
1.	Increase anonymity
By changing out mac address we can become anonymous in a network because our mac address will be different from the mac address provided by the manufacturer and therefore no one will be able to link us to the spoof mac later.
2.	Impersonate other devices
When we have the privilege to change our mac address, we can impersonate the mac address of any other device connected in the network and therefore and gain that device’s privileges.
3.	Bypass Filters
By changing our mac address, we can bypass filters in a network that doesn’t allow our devices to connect to the network. I will elaborately explain this in my future articles.


Using mac_changer to change mac address
---------------------------------------
Make sure you have git installed in your system before moving to the next steps.

1>	To use this tool first you have to open your terminal and type the following command: 
git clone https://github.com/cs-sohan/mac_changer

2>	Now move to the directory where you stored it.

3>	Now type the following command to view the options of the tool:
python mac_changer.py -h

4>	Now I will change it using the following command:
python mac_changer.py -i <interface-name> -m <spoof mac address>

That’s it. I have successfully changed my mac address to my custom mac address and now I can do so many cool things.

I will show all the cool and useful things I can do by changing my mac address & I will also talk about many more hacking tools in my future articles to further your knowledge and protecting your privacy online.
Stay Tuned!

About myself
------------
My name is Sohan Chakraborty and I am an Ethical Hacker & a Cyber-Security Enthusiast. I specialize in penetration testing and tools creation.

Connect with me:
-----------------
 linkedin: sohan-chakraborty-cs
 
 email: cs.sohanchakraborty@gmail.com

