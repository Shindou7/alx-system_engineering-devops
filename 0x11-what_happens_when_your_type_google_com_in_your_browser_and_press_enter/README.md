# 0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter

# Demystifying the Web Stack: A Journey from URL to Webpage

## Introduction

This repository accompanies an enlightening blog post that unravels the intricate journey triggered when you type `https://www.google.com` into your browser and press Enter. The narrative explores the crucial components of the web stack, offering a deep dive into the technologies that seamlessly deliver web content.

## Blog Post Overview

### DNS Request:

The journey begins with a Domain Name System (DNS) request. When you type the URL, your browser sends a request to a DNS server to translate the human-readable domain name (www.google.com) into an IP address. This IP address is crucial for establishing a connection to the web server hosting the Google website.

### TCP/IP:

Once the DNS server responds with the IP address, your browser initiates a Transmission Control Protocol (TCP) connection to the server. TCP ensures a reliable, ordered, and error-checked connection, dividing the data into packets for efficient transmission over the Internet Protocol (IP).

### Firewall:

As the data packets traverse the internet, they may encounter firewalls. Firewalls act as a security barrier, filtering incoming and outgoing network traffic. They play a crucial role in protecting against unauthorized access and potential threats.

### HTTPS/SSL:

To secure the communication between your browser and the web server, the Hypertext Transfer Protocol Secure (HTTPS) is employed, which utilizes the Secure Sockets Layer (SSL) or Transport Layer
Security (TLS) protocols. This encryption ensures that the data exchanged between your browser and the server remains confidential and secure.

### Load-Balancer:
Upon reaching Google's infrastructure, a load balancer distributes incoming requests across multiple servers. This ensures optimal resource utilization, prevents server overload, and enhances the website's overall performance and reliability.

### Web Server:
The load balancer forwards the request to one of Google's web servers. The web server is responsible for handling HTTP requests, processing them, and sending back the requested web page data. In Google's case, these servers might be distributed globally to minimize latency.

### Application Server:
Behind the scenes, an application server may be responsible for processing dynamic content or executing server-side code. This server interacts with databases, performs complex computations, and generates content that the web server then sends to your browser.

### Database:
For services like Google, databases store vast amounts of information, ranging from search results to user preferences. The application server communicates with the database to retrieve and update data dynamically.
