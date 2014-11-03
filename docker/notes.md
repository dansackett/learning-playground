# What Is Docker?

[Docker](https://www.docker.com/) is an open platform for distributed applications.
It allows you to build portable applications that can be run anywhere. It also
allows configurations to be the same in many locations since they are based on
an image.

# Docker Hub

The [Docker hub](https://hub.docker.com) is a central repository of Docker images and allows for user
auth, automated image builds, webhooks, and integration with Github and
Bitbucket.

You can log into Docker hub from the terminal with:

```
$ sudo docker login
```

# Running applications

## Simple one-off application

Running an application in Docker means running a command inside a container.
We do this with the `docker run` command. For example, we can do:

```
$ sudo docker run ubuntu:14.04 /bin/echo 'Hello world'
Hello world
```

This does the following:

* It launches a container.
* More specifically, it loads `ubuntu:14.04` as the image for the container.
Docker will look for the image and download it from Docker Hub if it is not in
your local repos.
* It ran the command `/bin/echo 'Hello world'`
* Docker stopped and closed the container after echo since the command ended.

This workflow allows us to load our containers and run commands simply.
Perhaps to check stats or get output.

## Interactive Containers

We can go into interactive mode with a bash prompt like so:

```
$ sudo docker run -t -i ubuntu:14.04 /bin/bash
```

The `-t` flag assigns a terminal inside the container. The `-i` flag hooks to
STDIN and allows us to interact with the container.

From here, we can play with the container as if it were any other Linux
terminal. To leave the container we use `exit`.

## Daemonized Containers

We can create containers that run as daemons through the docker run utility as
before.

```
$ sudo docker run -d ubuntu:14.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
99b0ce5daf6110601d85afcc3381f796ccf9ddbfd8802fd05c5cb590440c6df7
```

This will return a container id which identifies the new deamon container. To
make sure that it is running we can use:

```
$ docker ps
```

This tells all information about the container including the ID, image,
command, and status.

We can view the logs from the Docker container with:

```
$ sudo docker logs NAME
```

Where the name is the assigned name given in the `docker ps` results. We can
finally stop the daemon with:

```
$ sudo docker stop NAME
```

This will close the container and clean it up. We can run `docker ps` again
and see that the container has been stopped.

# Working with Containers

Docker provides an extensive API to interact with containers. Some other
commands we can do are:

```
attach    Attach to a running container
build     Build an image from a Dockerfile
commit    Create a new image from a container's changes
cp        Copy files/folders from a container's filesystem to the host path
create    Create a new container
diff      Inspect changes on a container's filesystem
events    Get real time events from the server
exec      Run a command in an existing container
export    Stream the contents of a container as a tar archive
history   Show the history of an image
images    List images
import    Create a new filesystem image from the contents of a tarball
info      Display system-wide information
inspect   Return low-level information on a container
kill      Kill a running container
load      Load an image from a tar archive
login     Register or log in to a Docker registry server
logout    Log out from a Docker registry server
logs      Fetch the logs of a container
port      Lookup the public-facing port that is NAT-ed to PRIVATE_PORT
pause     Pause all processes within a container
ps        List containers
pull      Pull an image or a repository from a Docker registry server
push      Push an image or a repository to a Docker registry server
restart   Restart a running container
rm        Remove one or more containers
rmi       Remove one or more images
run       Run a command in a new container
save      Save an image to a tar archive
search    Search for an image on the Docker Hub
start     Start a stopped container
stop      Stop a running container
tag       Tag an image into a repository
top       Lookup the running processes of a container
unpause   Unpause a paused container
version   Show the Docker version information
wait      Block until a container stops, then print its exit code
```

# Running a Web Application

We can run full applications in Docker of course.

```
$ sudo docker run -d -P training/webapp python app.py

We can also specify a port with:
$ sudo docker run -d -p 5000:5000 training/webapp python app.py
```

This will download a Flask application from Docker Hub and will run the
application for us as a daemon. The `-P` flag maps network ports inside our
container to our host. This way we can actually view the application. Now,
running `docker ps` will gives us information about ports. We can also run
`docker port NAME` to get the port information for our container easily.

We can tail the log files easily:

```
$ sudo docker logs -f NAME
```

We can see running processes with top:

```
$ sudo docker top NAME
```

We can of course stop the app, start it, or restart it with `docker
start/stop/restart`. Just choose one of the options. If we find that we don't
need the container any more, we must first stop the container. Then we can
run:

```
$ sudo docker rm NAME
```

Deleting is final and we won't have access to it anymore.

# Managing our own Docker Images

When working with images, we can create and see our current images. For
instance, to see all images that we have we can do `docker images`.

If we want to add a new image to our host, we can use the `docker pull IMAGE`
command. This will look on the Docker Hub and find the appropriate image and
download it for use later. While we can browse the Docker Hub [registry](https://registry.hub.docker.com/)
we can also use `docker search TERM` in the terminal to get a list of images
we can download.

We can make changes to an image a lot like using Git. For instance, we could
do the following:

```
$ sudo docker run -t -i redis /bin/bash
$ sudo apt-get install PACKAGE
$ exit

$ sudo docker commit -m="Test" -a="Dan Sackett" 17d5d8484040 mine/redis:v2
e39713b793d9052c805a48d24594ec433f8e271aa03304f87b316e8ead96896b
```

This workflow is awesome and allows us to take base images and customize them
to our liking. It also allows you to collaborate with others and share your
images. Here, we can install a package for instance and then commit the new
change. We specify the container ID to say that we want to reference that and
then we name the new container `mine/redis` with a tag of `v2`.

If we want to create a new Docker image, we create a recipe known as the
Dockerfile. A sample Dockerfile looks like:

```
# This is a comment
FROM ubuntu:14.04
MAINTAINER Dan Sackett <danesackett@gmail.com>
RUN apt-get update && apt-get install -y ruby ruby-dev
RUN gem install sinatra
```

With that, we can do:

```
$ sudo docker build -t="dansackett/sinatra:v2" .
```

This will name the image and build it out. We use the `.` to specify that
the Dockerfile is in the current directory. After this is done, we can use
this image. We can also create new tags on the image if we wish:

```
$ sudo docker tag IMAGE_ID IMAGE_NAME:NEW_TAG
```

If we want, we can then push the image to Docker hub with:

```
$ sudo docker push dansackett/IMAGE_NAME
```

If we then want to remove an image from the hub, we can do:

```
$ sudo docker rmi dansackett/IMAGE_NAME
```

# Linking Containers

One thing that can become really useful is building containers for different
functions. For instance, having a database container and an application
container. One thing that will help do this is specifically naming containers.
We can name containers with:

```
$ sudo docker run -d -P --name NAME IMAGE python app.py
```

Container names must be unique. You have to `docker rm` the container if you
want to use the same name. Getting back to links, we like these because when
containers are linked, they can transfer information securely and work with
one another.

As an example, we can do this:

```
$ sudo docker run -d --name db training/postgres
$ sudo docker run -d -P --name web --link db:db training/webapp python app.py
```

Creating container links consists of `--link name:alias` where we create a new
alias that can be used in the linked container. One thing to take note of is
that we didn't need to expose a port for the sub containers. The only one that
needed it was the application itself to access it. This process sets a number
of environment variables for us to work with as seen here:

```
$ sudo docker run --rm --name web2 --link db:db training/webapp env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=3e9b90933420
DB_PORT=tcp://172.17.0.4:5432
DB_PORT_5432_TCP=tcp://172.17.0.4:5432
DB_PORT_5432_TCP_ADDR=172.17.0.4
DB_PORT_5432_TCP_PORT=5432
DB_PORT_5432_TCP_PROTO=tcp
DB_NAME=/web2/db
DB_ENV_PG_VERSION=9.3
HOME=/
```

The variables are prefaced with the alias we set in the link. With this, only
the linked container will be able to access and talk to this instance. Another
cool thing is linking will automatically create a reference in /etc/hosts on
the linked container.
