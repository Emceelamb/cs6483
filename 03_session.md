# Network app

## What is a network app?
A network app is a program that runs on different end systems and communicates over a network. No need to write network-core.

## Application architectures
- client-server
- peer-to-peer (p2p)

## P2P architecture
- no always on server
- arbitrary end systems directly endsystems directly communicate

## Proccesses communicating
- server must be running first
- 

## Sockets
**Addressing processing**
- to receive messages process must have identifier
- needs IP address and port number

## App-layer protocol defines
- open protocols
- proprietary protocols

## What transport service does an app need?
- data integrity
- timing
- throughput
- security

## Internet transport protocols services
- tcp
  - reliable
  - flow control
  - congestion control
  - doesnt provide timing, security, min. throughput guarantee
  - connection-oriented
- UDP
  - unreliable data transfer
  - does not provide 
    - reliability flow control, congestion
- securing TCP
  - ssl
## Web and HTTP
- HTTP
  - client-server connection
  - non persistent http
    - at most one object sent over tcp
  - persistent http
    - multiple objects can be sent over single tcp connection between client and server
    - RTT = round trip time
    - server leaves connection open after sending response
- Uploading form input
  - POST method
  - web page often include form input
  - input is uploaded to server in entity body
- URL method
  - uses get method
  - input is uploaded in URL
- vulnerabilities
  - LFI local file inclusion
  - cross scripting

Method types: 
- HTTP/1.0
- HTTP/1.1
- HTTP status code appears in 1st line in server to client response message 

Caching example: install local cache
- calculating access link utilization delay with cache
 
## EMAIL servers
- SMTP uses tcp port 25
- direct transfer from system perspective
- three phases of transfer
  - handhhshaking
  - transfer of message
  - closure
- command/response interaction like http
- http = pull
- smtp = push
  - POP= auth/download
    - stateless across messages
    - download and keep copies of messages on differenct clients
  - IMAP - more features including manipulation of stored messages on server
  - HTTP gmail, hotmail, etc. access email in browser
