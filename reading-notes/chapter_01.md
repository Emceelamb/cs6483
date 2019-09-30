# Computer Networks & the Internet

## What is the internet
### Nuts and Bolts
- Hosts & end systems - devices that are connected to the internet
- End system connected by communiccation links and packet switches
- transmission rate is measured in bits/second
- packets arer packages of information each segment of data adds header
- routers are used for network core
- link layer switches are used in access networks
- each isp is in itself a network of packet swictches and comm. links
- internet standards are developed by the internet engineering task force (ietf)
- standards docs arre called resquests for comments (rfcsc)

### Services
- socket interfaces specify how a program deliveers data to end system

### What is protool?
- protococl defines format and order of messages exchnaged between two or more cocmmunicated entities as well as the actions taken on the transmission and recipt of a message or otherr event

## Network edge
- end systems are referred to as hosts because they host applications
- hosts are divided into two categories clients and servers

### Access Networks
- Digital Subscriber Network (DSL) - telco uses telehphone line
- cable internet access uses cable televisions exstisting cable tele. infrastructure
  - uses coaxial cable
- fiber to the home (FTTH)
  - direct line from telco local central office (CO)j
  - each home has Opticacl Network Terminiator (ONT)
  - Optical line terminator (OLT)
  - Internet > Centraol Office > OLT > Optical splitter > ONT
- sattelite
- dial up access uses phone line
    - very slow at 56 kbps

### Etherrnet and Wifi
- ethernet diagram
  - ISP > Institutional Router > Ethernet Switch > hosts
- WLAN = wireless LAN
- wigle.net logs 802.11 base stations

### Wide Area Acces (WAN)
- 3G and beyond
- cellular telephony

### Physical media
- guided media = cables
- unguided = wireless
- Twisted-pair cocpper wire
  - least expensive and most common for telephones
- coaxial cable
  - common for cable television
  - can be used for shared medium
- fiber optics
  - conducts pulses of light
  - can achieve high bit rates
  - preferred for logn distance 
  - high cost hinderred short hau transport
- terrestial radio channels
  - do  not equire physical wire 
  - prone to environmental interference
  - three groups:
    - personal (bluetooth, zigbee)
    - LAN (ten to few hundred meters)
    - WAN (cellular)
- sattellite
  - geostationary
    - permanently remain above the same spot on earth
    - 280 ms delay
  - low earth orbiting
    - not currently used for intenet
## Network core
### packet switching
- packets - chunks of data
- send packets of L bits over a link with transmission rate R bits/sec
- time to ransmit the packet is *L/R* seconds
- **store-and-forward**
  - packet switches uses store andd forward
  - routers must buffer packets bits
  - only whe router has received all of packets bit can it bgin to transmission
  - output buffer
  - queuing delays - delay whilte store and forwad
### circuit switching
- hosts are directly connected to each other (end to end connection)
- they have a guaranteed constant rate
### Multiplexing
- Frequency division multip plexing (FDM)
  - separates connecctions on differrent frequenccy bands
- Time division multiplexing (TDM)
  - time is divided into frames
  - each frame is divided into slots
- Factors to consider
  - silent periods (idle time) of circuit is considered wasteful
  - end to end circuit design is complicated
  - critics say packcet switchcing is not ideal forr real time due to unpredectibale end to end delays
  - propents say it is more efficient
  - probability packet switchc users will simultaneously use connecctions is low
## Networks of networks
- tier 1 isp = global (imaginary) isp
- regional isp = network n a region connected to isp
- PoP - points of precence - group of routers in one location
- IxP - internet exchange point
- multi-home - connect to two or moe provider isp

## Delay lost and throughput in packet switch networks
-  processing delay
  - time it takes to examine header 
  - bit errors etc
- queuing delay
  - delay as packet waits to be sent
  - due to previously sent packcets
- transmission delay
  - time it takes all packets to transmit through the line
- propagation delay
  - time it takes on the line
- total nodal delay

### Packet loss
- if queue is full on router a packet will be lost

