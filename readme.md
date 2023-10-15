<div align="center">
    <img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
    <img alt="Django" src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/>
    <img alt="JavaScript" src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>
</div>

# RedditBot - Video Generator
If you're like me and are addicted to short videos, have you ever wondered how on earth are there so many of them?
Well, I tried to answer this question and, in short, you can automate the process. (it's very easy!)

RedditBot - is a service that allows the user to generate a video
that reads out reddit post, relevant comments over a background video from
the provided catalog. The data is inputed through a form and is then converted into a video project that can
track the progress of creation and produces a *Voiced Over* video that is ready to be uploaded.

The idea is very simple:
1. Get data (urls, base clip) from the user
2. Get content (post text, screenshot and sound [text-to-speech])
3. Put everything together over a base clip (minecraft parkour)
4. Export, upload to Instagram/Tiktok
5. Wait for it to go viral and make $$$ on ads


[Demo Result](https://drive.google.com/file/d/1P3B2Jan5bwJUkvgY5Jjt-r0EWfMPSLAt/view?usp=sharing)

## Stack
* Python Django 3.1
* Docker
* Bootstrap

## Set up instructions:
* Install dependencies:
    * Docker 
        * https://docs.docker.com/engine/install/
    * Docker-Compose
        * https://docs.docker.com/compose/install/

* Clone the repo on your machine

* cd to the folder and fire it up
    * ```sudo docker-compose up --build```

* Apply migrations and start
    * ```sudo docker-compose exec web python manage.py migrate```

* The service will be available at:
    ```http://localhost:8000```
