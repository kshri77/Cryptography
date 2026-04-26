

---

# Exercise 5: Snort Intrusion Detection System (IDS) 

This repository demonstrates basic usage of Snort for monitoring network traffic, analyzing packets, and creating custom detection rules.

---

1. Monitor Live Network Traffic

Capture real-time packets from a network interface and apply rules.

```bash
snort -i 4 -c C:\Snort\etc\snort.conf -A console
```

---

2. Analyze Packets from a PCAP File

Read and inspect previously captured traffic.

```bash
snort -r capture.pcap -c C:\Snort\etc\snort.conf -A console
```

---

3. Validate Snort Configuration

Check whether configuration files are correct.

```bash
snort -T -c C:\Snort\etc\snort.conf
```

---

4. Capture and Store Packets

Log packets into a PCAP file for later analysis.

```bash
snort -i 4 -b -l C:\Snort\log -L TrafficCapture
```

---

5. Create a Basic Detection Rule

Add this inside `local.rules`:

```bash
alert icmp any any -> any any (msg:"ICMP Ping Detected"; sid:1001001; rev:1;)
```

Run Snort again to activate the rule.

---

6. Display Detailed Packet Information

Show payload and header details along with alerts.

```bash
snort -i 4 -c C:\Snort\etc\snort.conf -A console -d -e
```

---

7. Capture Limited Packets

Stop after capturing a fixed number of packets.

```bash
snort -i 4 -c C:\Snort\etc\snort.conf -A console -n 15
```

---

8. Perform Network Discovery Scan

Use Nmap to identify active hosts.

```bash
"C:\Program Files (x86)\Nmap\nmap.exe" -sn 192.168.1.0/24
```

---

9. Configure Rule Files

Ensure these lines exist in `snort.conf`:

```bash
include classification.config
include reference.config
include $RULE_PATH/local.rules
```

---

10. Sample Detection Rules (local.rules)

```bash
# SYN Scan Detection
alert tcp any any -> any any (flags:S; msg:"Possible SYN Scan"; sid:1001002; rev:1;)

# FIN Scan Detection
alert tcp any any -> any any (flags:F; msg:"Possible FIN Scan"; sid:1001003; rev:1;)

# NULL Scan Detection
alert tcp any any -> any any (flags:0; msg:"NULL Scan Activity"; sid:1001004; rev:1;)

# XMAS Scan Detection
alert tcp any any -> any any (flags:FPU; msg:"XMAS Scan Activity"; sid:1001005; rev:1;)

# UDP Scan Detection
alert udp any any -> any any (msg:"UDP Scan Activity"; sid:1001006; rev:1;)
```

---

11. Run Scan Tests

Execute scans using Nmap to trigger alerts.

```bash
nmap -sS 192.168.1.2
nmap -sN 192.168.1.2
nmap -sX 192.168.1.2
```

---

12. Detect ICMP Traffic to Specific Host

```bash
alert icmp any any -> 8.8.8.8 any (msg:"ICMP Request to External DNS"; itype:8; sid:1001009; rev:1;)
```

---

13. Detect HTTP GET Requests

```bash
alert tcp any any -> any 80 (msg:"HTTP GET Request Found"; content:"GET"; http_method; sid:1001010; rev:1;)
```

Test using:

```bash
curl -I http://example.com
```

---

14. Detect Suspicious User-Agent

```bash
alert tcp any any -> any 80 (msg:"Suspicious Tool Detected"; content:"sqlmap"; http_header; sid:1001011; rev:1;)
```

Test:

```bash
curl -A "sqlmap" http://192.168.1.1
```

---

Detect Directory Traversal Attempts

```bash
alert tcp any any -> any 80 (msg:"Directory Traversal Attempt"; content:"../"; sid:1001012; rev:1;)
```

Test:

```bash
curl http://192.168.1.1/../../etc/passwd
```

---

16. Detect Suspicious DNS Queries

```bash
alert udp any any -> any 53 (msg:"Malicious Domain Query"; content:"malicious-site.com"; sid:1001013; rev:1;)
```

Test:

```bash
nslookup malicious-site.com
```

---

---

Tools Used

* Snort
* Nmap
* cURL
* Windows Command Prompt
