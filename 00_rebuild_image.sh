#!/bin/bash

(cd ./01_scraper_docker; ./00_remove_image.sh)
(cd ./01_scraper_docker; ./01_build_image.sh)

