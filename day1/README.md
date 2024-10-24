### Understanding mindset of Metrics Generation and collection 

<img src="gen1.png">

### custom metrics required in many cases to start monitoring apps 

<img src="custom.png">

### Welcome to DogstatsD in datadog 

<img src="dogs.png">

### checking datadog agent status

```
 systemctl status datadog-agent
● datadog-agent.service - Datadog Agent
     Loaded: loaded (/usr/lib/systemd/system/datadog-agent.service; enabled; preset: disabled)
     Active: active (running) since Thu 2024-10-24 07:57:38 UTC; 56s ago
   Main PID: 2084 (agent)
      Tasks: 8 (limit: 4658)
```
### dogstatsD is running on 8125 in UDP mode 

```
netstat -nulp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
udp        0      0 127.0.0.1:8125          0.0.0.0:*                           2084/agent          
udp        0      0 172.31.92.124:68        0.0.0.0:*                           2053/systemd-networ 
udp        0      0 127.0.0.1:323           0.0.0.0:*                           2273/chronyd        
udp6       0      0 ::1:323                 :::*                                2273/chronyd        
udp6       0      0 fe80::10fc:6eff:fed:546 :::*                                2053/systemd-networ 
[root@ip-172-31-92-124 ~]# 

```

### creating a python webapp 

```
mkdir /opt/pyappnew
[root@ip-172-31-92-124 ~]# 
[root@ip-172-31-92-124 ~]# cd /opt/pyappnew/
[root@ip-172-31-92-124 pyappnew]# 

===> creating app
nano ashu.py 
