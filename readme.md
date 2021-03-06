# ImagesAPI | Django REST Framework

## General info

REST API created in Django Rest Framework as HexOcean recruitment task.

# Setup:

Clone this repository.

Docker:
- `docker-compose up`

or demo: `https://images-api-hex.herokuapp.com/`

Login on admin site

## Endpoints

1. GET `/images`
 - List all user's images
2. POST `/images`
 - uploads image and returns links with image sizes depending on user's tier

## Features

 - upload .jpg and .png images, format validation
 - listing user's images
 - upload on HTTP request
 - builtin tiers (docker-compose command populates db based on fixture)
 - tiers have all requried features (thumbnails, original image, link duration)
 - making custom tiers in admin panel
 - pagination
 - docker-compose

 Unfortunately, due to end of time, project contains few tests.
 I know that heroku raises 500 when uploading with multiple image upload tier but it's working locally, just did not have enough time to investigate that.

## Stack

 - Python
 - Djanog
 - Django Rest Framework
 - Docker
 - PostgreSQL
 - Pytest
 - Pillow
 - AWS S3
 - Heroku
 - Factory boy

 ### Screen

 ![Alt text](static/screens/screen.png "Screen")