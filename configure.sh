#!/bin/bash
cp ./webserv.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable webserv.service