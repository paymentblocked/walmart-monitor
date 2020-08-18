# walmart-monitor
Monitors the Walmart website for the item of your choice. If a restock is detected, it will send it to your Discord channel. Specifically designed to assist with purchasing essential items during COVID-19 (Medicine, masks, gloves, etc).

## Getting Started

Download the required packages from [requirements.txt](requirements.txt)

```
pip install requirements.txt
```

Go to https://discord.com/developers/applications and get your bot token ```(New Application > Bot)```.

Paste your bot token on [line 5](https://github.com/ra-zo/walmart-monitor/blob/master/walmart.py#L5).

### Start Monitor

To start the monitor, type ```!monitor``` in the channel of your choice.

Once you are prompted for a Walmart product link, please send it exactly like this example. EX: https://www.walmart.com/ip/Oculus-Quest-64GB-VR-Headset/472031416

#### Out Of Stock Products

If the product is out of stock, the **only** message that will be sent is ```Monitoring starting. Checking for stock...```. No other message will be sent in the Discord channel until stock is detected.

Out of stock products will be checked for stock at a default delay of 60 seconds (every minute a request will be made). If you would like to change the delay, you may do so at [line 44](https://github.com/ra-zo/walmart-monitor/blob/master/walmart.py#L44). As an example, if you would like to monitor every 30 seconds, change it to 
```
await asyncio.sleep(30)
```

To run, use ```python walmart.py``` or ```python /Users/YourNameHere/Downloads/walmart.py``` in terminal.

![Image](https://i.imgur.com/dc2WCLt.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
