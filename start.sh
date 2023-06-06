#!/bin/bash
cd /root/ChatServer/
/usr/local/bin/uvicorn main:app1 --reload --host 185.119.58.234 --port 3031