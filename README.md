# Api for random cats info wit bot
### How to use
Just use `@randomm_cats_bot` and you will have info about some cats :)  
### How to deploy
1. Install [docker](https://docs.docker.com/engine/install/)
2. Copy project `git clone https://github.com/senyehor/api_with_bot.git` and enter the directory
3. Fill all *.env.template files with your data, removing .template extension
4. Just `sudo docker compose up -d`
5. To have some data pre-populated run `chmod +x db/insert_into_db.sh && ./db/insert_into_db.sh`