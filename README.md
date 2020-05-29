# Pushbullet Notify Server
This is a docker container which runs a [FastAPI](https://fastapi.tiangolo.com/) server to send some
simple notifications, over [Pushbullet](https://www.pushbullet.com/), when a command is completed.

## Installation
Run the following to build the image:

```console
$ docker build -t pushbullet_server .
```

## Configuration and running
Create a new user network for the containers:

```console
$ docker network create notify-net
```

You need to get two pieces of information from Pushbullet.
1. Access Token (from the settings)
1. Device Identification
    - Get with the following command:

```console
$ curl --header 'Access-Token: <your_access_token>' \
https://api.pushbullet.com/v2/devices
```

Start the container with your settings:

```console
$ docker run -d --rm \
-e ACCESS_TOKEN=<your_access_token> \
-e DEV_ID=<your_device_iden>
--network notify-net \
--name pbs \
-p 8700:80 \
pushbullet_server:latest
```

## Usage

### From your host
Send a success:

```console
$ curl "localhost:8700/cmd?err=0"
```

Send a success or failure based on a command:

```console
$ echo hello; curl "localhost:8700/cmd?err=$?"
```

### From another container
Startup a container on the same network:

```console
$ docker run -d --rm --it \
--network notify-net \
ubuntu
```

Send a success:

```console
$ curl "pbs/cmd?err=0"
```

Send a success or failure based on a command:

```console
$ echo hello; curl "pbs/cmd?err=$?"
```
