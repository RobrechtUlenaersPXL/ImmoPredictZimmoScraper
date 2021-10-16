
#Download base image ubuntu 20.04
FROM ubuntu:20.04
ENV TZ=Europe/Brussels
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# LABEL about the custom image
LABEL maintainer="Robrecht.Ulenaers@student.pxl.be"
LABEL version="0.1"
LABEL description="This is custom Docker Image for \
the zimmo scraper used in our itproject."


RUN set -x \
	&& apt-get update \
	&& apt-get install unzip -y\
	&& apt-get install python3 -y\
	&& apt-get install python3-pip -y\
	&& pip3 install --upgrade pip \
	&& apt-get install sudo -y\
	&& apt-get install wget -y\
	&& apt-get install chromium-chromedriver -y\
	&& pip3 install pandas==1.3.3 \
	&& pip3 install selenium==3.14.0\
	&& pip3 install bs4 \
	&& pip3 install requests\
	&& pip3 install lxml==4.6.3\
	&& rm -rf /var/lib/apt/lists/* \
	&& useradd -ms /bin/bash user \
	&& echo "user:user" | chpasswd && adduser user sudo \
	&& echo "user ALL=(ALL) NOPASSWD: ALL " >> /etc/sudoers

	
	
ARG CHROME_VERSION="google-chrome-stable"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    ${CHROME_VERSION:-google-chrome-stable} \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*
  
USER user
WORKDIR /home/user
RUN mkdir scraper
    
CMD sudo service ssh start && /bin/bash
    
   
