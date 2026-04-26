#EX5- SNORT

This repository contains basic Snort IDS commands, configurations, and custom rules for monitoring and detecting network activities.
1. Monitor Live Network Traffic

Reads packets from a network interface and compares them with rules.

snort -i 4 -c C:\Snort\etc\snort.conf -A console

2. Read Packets from a PCAP File

snort -r my_capture.pcap -c C:\Snort\etc\snort.conf -A console

3. Test Snort Configuration

snort -T -c C:\Snort\etc\snort.conf

4. Capture Packets to a PCAP File

snort -i 4 -b -l C:\Snort\log -L MyCapture

5. Create a Simple Test Rule

Add this in local.rules:

alert icmp any any -> any any (msg:"ICMP Test Alert"; sid:1000001; rev:1;)

Run Snort:

snort -i 4 -c C:\Snort\etc\snort.conf -A console

6. Print Alerts with Packet Details

snort -i 4 -c C:\Snort\etc\snort.conf -A console -d -e

7. Limit Packet Capture

snort -i 4 -c C:\Snort\etc\snort.conf -A console -n 10

8. Perform Network Scan using Nmap

"C:\Program Files (x86)\Nmap\nmap.exe" -sn 192.168.1.0/24

9. Configure Rule Files

In snort.conf:

include classification.config
include reference.config
include $RULE_PATH/local.rules

Example Detection Rules (local.rules)

# SYN Scan
alert tcp any any -> any any (flags:S; msg:"SYN Scan Detected"; sid:1000002; rev:1;)

# FIN Scan
alert tcp any any -> any any (flags:F; msg:"FIN Scan Detected"; sid:1000003; rev:1;)

# NULL Scan
alert tcp any any -> any any (flags:0; msg:"NULL Scan Detected"; sid:1000004; rev:1;)

# XMAS Scan
alert tcp any any -> any any (flags:FPU; msg:"XMAS Scan Detected"; sid:1000005; rev:1;)

# UDP Scan
alert udp any any -> any any (msg:"UDP Scan Detected"; sid:1000006; rev:1;)

10. Execute Snort in IDS Mode (Scan Testing)

"C:\Program Files (x86)\Nmap\nmap.exe" -sX 192.168.1.2
"C:\Program Files (x86)\Nmap\nmap.exe" -sN 192.168.1.2
"C:\Program Files (x86)\Nmap\nmap.exe" -sS 192.168.1.2

11. Detect ICMP Traffic to Specific IP

alert icmp any any -> 8.8.8.8 any (msg:"ICMP Traffic to Google DNS"; itype:8; sid:1000009; rev:1;)

12. Detect HTTP GET Request to a Domain

alert tcp any any -> any 80 (msg:"HTTP GET Request Detected"; content:"GET"; http_method; sid:1000010; rev:1;)

Test:

curl -I http://example.com

13. Detect Suspicious User-Agent

alert tcp any any -> any 80 (msg:"Suspicious User-Agent Detected"; content:"sqlmap"; http_header; sid:1000011; rev:1;)

Test:

curl -A "sqlmap" http://192.168.1.1

14. Detect Directory Traversal Attack

alert tcp any any -> any 80 (msg:"Directory Traversal Attack"; content:"../"; sid:1000012; rev:1;)

Test:

curl http://192.168.1.1/../../etc/passwd

15. Detect Suspicious DNS Query

alert udp any any -> any 53 (msg:"Suspicious DNS Query"; content:"malicious-site.com"; sid:1000013; rev:1;)

Test:

nslookup malicious-site.com

🚀 Tools Used

    Snort IDS
    Nmap
    Curl
    Windows Command Prompt
