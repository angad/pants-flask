# This dockerfile is only for demo purposes for setting up a build environment for building pex files
# For production use cases, generate a pex file beforehand as part of CI/CD and then build the docker image with that PEX file.:w

FROM ubuntu
RUN apt-get update && apt-get -y install curl python build-essential python-dev openjdk-8-jdk
ADD . /opt/helloworld/
RUN cd /opt/helloworld && \
    ./pants binary src/python/helloworld:helloworld
CMD ["/opt/helloworld/dist/helloworld.pex"]
