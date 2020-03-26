#!/bin/sh
tar -xvzf /home/ubuntu/movie-analyst-api-1.0.0.tgz
cd /home/ubuntu/package
npm i
pm2 start /home/ubuntu/package/server.js --name API