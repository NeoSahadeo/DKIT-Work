1. Ethernet II
[PREAMBE][SFD][DESTIONATION ADDRESS][SOURCE ADDRESS][LENGTH][DATA][FCS]

Preamble:
Used to let the destination computer know that data
is coming and was used to sync the clocks of the
host and destination.

SDF (Start frame delimeter):
Tells the system that the preamble has ended

Addresses:
destination and source MAC / Phyiscal adress

Type:
Values above 1500 are the length of the data
in the data section.

Data:
Actual Bits transmitted

FCS (Frame-Check-Sequence):
Used for error checking

2. IEEE 802.3
[PREAMBE][SFD][DESTIONATION ADDRESS][SOURCE ADDRESS][TYPE][DATA][FCS]

Preamble:
Used to let the destination computer know that data
is coming and was used to sync the clocks of the
host and destination.

SDF (Start frame delimeter):
Tells the system that the preamble has ended

Addresses:
destination and source MAC / Phyiscal adress

Length:
Value determines what type of data is in the
data sections

Data:
Actual Bits transmitted

FCS (Frame-Check-Sequence):
Used for error checking

3. 48bits = 6bytes
a) 01 80 c2 00 00 00

b) 01 -> multicast

c) 40 8f 9d 0d d6 bc

d) IEEE 802.3 (type)

4.
a) ff ff ff ff ff ff

b) Broadcast

c) c0 25 a5 86 4d c8 (source mac)

d) 0x0806 > 1500 so its length (Ethernet II)

5.
a) 00 0c 29 70 47 6d

b) unicast

c) 08 bf b8 28 7f 3d

d) 0x0800 > 1500 so its length (Ethernet II)

6.
...

7.
(1/10^9) * 64 * 8 = 5.12*10^-7 seconds
time taken = 512ns (in nano seconds)

8.
(1/10^9) * 1518 * 8 = 1.214410^-5 seconds
time takne = 12.1µs (in mico seconds)
