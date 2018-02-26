# Python Quick Start Guide

This guide will walk you through deploying a Python application on [UVCloud](uvcloud.ir).

## Usage

```console
$ git clone https://github.com/uvcloud/example-python.git
$ cd example-python
$ uv create
Creating Application... done, created haptic-waggoner
Git remote uv added
remote available at ssh://git@uv-builder.uvcloud.ir:2222/haptic-waggoner.git
$ git push uv master
Counting objects: 11, done.
Delta compression using up to 24 threads.
Compressing objects: 100% (8/8), done.
Writing objects: 100% (11/11), 3.08 KiB | 0 bytes/s, done.
Total 11 (delta 1), reused 0 (delta 0)
Starting build... but first, coffee!
...
-----> Restoring cache...
       No cache file found. If this is the first deploy, it will be created now.
-----> Python app detected
-----> Installing python-3.6.1
-----> Installing pip
-----> Installing requirements with pip
       Collecting python-telegram-bot (from -r /tmp/build/requirements.txt (line 1))
       Downloading python_telegram_bot-9.0.0-py2.py3-none-any.whl (292kB)
       Collecting certifi (from python-telegram-bot->-r /tmp/build/requirements.txt (line 1))
       Downloading certifi-2018.1.18-py2.py3-none-any.whl (151kB)
       Collecting future>=0.16.0 (from python-telegram-bot->-r /tmp/build/requirements.txt (line 1))
       Downloading future-0.16.0.tar.gz (824kB)
       Installing collected packages: certifi, future, python-telegram-bot
       Running setup.py install for future: started
       Running setup.py install for future: finished with status 'done'
       Successfully installed certifi-2018.1.18 future-0.16.0 python-telegram-bot-9.0.0

-----> Discovering process types
       Procfile declares types -> web
-----> Checking for changes inside the cache directory...
       Files inside cache folder changed, uploading new cache...
       Done: Uploaded cache (57M)
-----> Compiled slug size is 54M
Build complete.
Launching App...
...
...
...
...
Done, haptic-waggoner:v2 deployed to Workflow

Use 'deis open' to view this application in your browser

To learn more, use 'deis help' or visit https://deis.com/

To ssh://git@deis-builder.uvapps.io:2222/haptic-waggoner.git
 * [new branch]      master -> master
$ curl http://haptic-waggoner.uvapps.io
Powered by UV
Release v2 on haptic-waggoner-web-3084677544-b9q78
```

## Additional Resources
* [Documentation](https://uvcloud.ir/docs/)
* [Blog](https://uvcloud.ir/blog/)


