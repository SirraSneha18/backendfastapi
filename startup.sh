#!/bin/bash
cd /home/site/wwwroot/app
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
