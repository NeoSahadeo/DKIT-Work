

1. Network Protocol, is a set of rules that define how
data is transfered on a network.


2. a) Makes it atomic (a change in 1 layer doesnt affect the other layers)
b) Allows the standardisations of different protocols
c) Since its smaller parts, its easier to develop / maintain
d) Makes it easier to learn.

3.
OSI MODEL (Pyramid)
7) Application Layer - HTTPS / TELNET
This is how users interact with a network

6) Presentation Layer - SSL, TLS
Translates the information to be understandable
by the layer above it.

5) Sessions - NetBios
Used to connect users together

4) Transmission - TCP and UDP
Allows data to be transfered between users.

3) Network - IP, ARP, ICMP
Packet forwarding

2) Data-link - Ethernet
Used to encapsulate data and allows data
transfer.

1) Physical - LAN Cable
Used for electrical and operational performance of
a network


4.
    OSI      |   TCP/IP
-------------------------------
Application  |
Presentation |     Application
Sessions     |
-------------------------------
Transmission |     Transmission
-------------------------------
Network      |     Internet
-------------------------------
Data-link    |     Network Access
Physical     |
-------------------------------


PDU (protocol data unit) of each layer:
Application -> message
Transmission -> segment
Internet -> Packet
Network Access -> Frame
"Physical Layer"  -> Bits


5.
Application -> HTTP
Transmission -> TCP, UDP
Internet -> IP, ICMP
Network Access -> Ethernet 802.3

6.
Encapsulation is the process of wrapping data around
another piece of data.

For example, to encapsulate a TCP packet with an Ethernet
header on the front of it and a ethernet trailer (FCS) on the
back of it

7.
+--------------------+
| Application Layer  |
| Protocol: HTTP     |
+--------------------+
| Transport Layer    |
| Protocol: TCP      |
+--------------------+
| Internet Layer     |
| Protocol: IP       |
+--------------------+
| Network Access     |
| Protocol: Ethernet |
+--------------------+

8.
a) NIC - Data-Link, Physical
b) Router - Network
c) IP - Transmission
d) RJ-45 - Physical
e) Patch panel - Physical
f) IEEE 802.3 (Ethernet) - Data-link, Physical
g) UDP - Transmission
h) DNS - Application
