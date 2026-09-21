===== OVERVIEW =====
The 'arpspoof.py' is a python program that allows users to perform an ARP spoofing attack using a single command.
It utilises the 'scapy' module to perform a Man-In-The-Middle (MITM) attack by sending forged ARP responses.
The script tricks the victim into associating the attacker's MAC address with the gateway's IP.
While that happens, it simultaneously tricks the gateway into associating the attacker's MAC address with the victim's IP address.
The victim is Metasploitable2, and the attacker is Kali.
Before the attack, the entry for the gateway's IP address will show the real gateway's MAC address.
During the attack, the entry for the gateway's IP address will be overwritten and show the Attacker's MAC address.

Files:
1. arpspoof.py

===== REQUIREMENTS =====
ENVIRONMENT:
1. Kali Linux VM
2. Metasploitable2 VM

LANGUAGE: PYTHON
LANGUAGE VERSION: 3.14.6

===== INSTALLATION OF LIBRARY =====
Before running this script, ensure that you have Python3 installed and configured. If not, use the code below to install Python3 and/or Scapy.
(*Remember to use 'sudo' to install with root privileges.)

To install Python3 : 'sudo pip3 install Python3'
To install Scapy: 'sudo pip3 install scapy'

===== HOW TO RUN THE PROGRAM =====
1. Ensure that both Kali (attacker) and Metasploitable2 (victim) VMs are running, and navigate to the file location.
2. On Kali, open the terminal and run the command 'sudo python3 arpspoof.py <Victim_IP> <Gateway(Router)_IP>'. Next, open Metasploitable2 and run the command 'arp -a' to be able to access the ARP table.
3. To stop the attack, press 'Ctrl + C' in the terminal.

Example, (*Refer to the attached images for the screenshots of the successful runs.)
- Victim_IP: 10.0.2.3
- Gateway(Router)_IP: 10.0.2.2 
- Command: 'sudo python3 arpspoof.py 10.0.2.3 10.0.2.2'.

===== EXPECTED RESULTS =====
In Metasploitable2, use the command 'arp -a' to see the changes in the ARP table. The table should reflect the same hardware address for both the gateway and attacker.
