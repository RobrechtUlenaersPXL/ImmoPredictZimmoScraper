#!/bin/bash


docker run --privileged -it --rm \
	--name scraper_container \
	--hostname scraper_container \
	--volume=/tmp/.X11-unix:/tmp/.X11-unix \
	-v `pwd`/../Scraper:/home/user/scraper \
	--device=/dev/dri:/dev/dri \
	--env="DISPLAY=$DISPLAY" \
	-e "TERM=xterm-256color" \
	--cap-add SYS_ADMIN --device /dev/fuse \
	-p 4444:4444 \
	itprojectscraper:latest \
bash

