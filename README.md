# bot_telegram
# Telegram Bot Automatically Updates News with requests

![Telegram Bot]

## Introduce
This project is a Telegram bot built in Python and uses request to automatically update news from websites that contain information of your interest. This bot will send the latest news to your group or users on Telegram.

## Setting

1.**Clone Repository**
git clone https://github.com/ChienNguyenIT/bot_telegram

2. Download and create a runtime environment on pycharm

3. **Install necessary libraries**
    ![384535269_228981720170144_1524988844995250100_n](https://github.com/ChienNguyenIT/bot_telegram/assets/127098641/4937bea2-a0a7-4baa-9d57-e7fa83fb4460)


4. **Telegram Bot Configuration**

- Create a bot on Telegram by talking to BotFather.
 ![384535290_254095700958788_3272367844237847136_n](https://github.com/ChienNguyenIT/bot_telegram/assets/127098641/6efd2654-7d1d-4564-98bc-15d353169096)

- Get the bot token and add it to the `config.py` file.
 ![384535269_228981720170144_1524988844995250100_n](https://github.com/ChienNguyenIT/bot_telegram/assets/127098641/03ba4c1d-58b7-4fe5-89af-01f41d9fa9fe)


5. **Configure requests to get news from websites**
![image](https://github.com/ChienNguyenIT/bot_telegram/assets/127098641/fbc30621-8db5-4664-8df6-4325888c414d)

- Add request spiders to retrieve data from specific websites.
- Configure rules and items to extract information from these websites.

## Use

1.	Run requests to get information:
 

2. Run a bot to send news to Telegram:
 ![384532658_640544614890264_6583204596589130348_n](https://github.com/ChienNguyenIT/bot_telegram/assets/127098641/2a108758-fada-4c2b-a054-553df55115ec)

- chat : "/hello" bot will send greetings
![image](https://github.com/ChienNguyenIT/bot_telegram/assets/127098641/338b967c-cb95-4cc3-a656-de642849802a)


- chat: “/news1,/news2,/new3” bot will automatically update news from 3 sources


## Custom

You can customize Scrapy's bot and spiders to fit your needs. Change rules and items to extract different information from different web pages.

## Contribute

If you want to contribute to this project, open a pull request or bug report on GitHub.

## License

This project is distributed under the license [LICENSE_NAME]([(https://www.crummy.com/software/BeautifulSoup/bs4/doc/)https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
