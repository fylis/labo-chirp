# Lab 2 - Chirp
## Requirements
The requirements for this project are : 
- Python
- Redis server
- Streamlit (optionally)
## How to compile/run the code
### Clone the repo
Clone the repo using the following command in a folder on the same machine where the Redis server is on.
```bash
git clone https://github.com/fylis/labo-chirp
```
### Launch the Redis server
Launch the Redis server service using the following command :
```bash
sudo systemctl start redis-server
```
Check the status using this command : 
```bash
sudo systemctl status redis-server
```
It should look like follow :
```bash
● redis-server.service - Advanced key-value store
     Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2025-03-24 13:57:10 CET; 1h 15min ago
       Docs: http://redis.io/documentation,
             man:redis-server(1)
   Main PID: 238 (redis-server)
     Status: "Ready to accept connections"
      Tasks: 5 (limit: 18974)
     Memory: 14.8M
     CGroup: /system.slice/redis-server.service
             └─238 "/usr/bin/redis-server 127.0.0.1:6379" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
```
### Run the Python file
Run the Python `.py` using the IDE or the following command using the terminal.
```bash
python .py
```
## Authors
- [Filip S.](https://github.com/fylis)
- [Ünal K.](https://github.com/UnalKulekci)
