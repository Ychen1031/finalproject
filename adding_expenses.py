import datetime
import os

postback_data = {"方式": "meal", "price": 100, "詳情": "蛋炒飯"}

if "方式" in postback_data:
    if postback_data["方式"] == "meal":
        print("餐費為" + str(postback_data["price"]) + "元" + "\n" + "細項: " + postback_data["詳情"])
    elif postback_data["方式"] == "transportation":
        print("交通費為" + str(postback_data["price"]) + "元" + "\n" + "細項: " + postback_data["詳情"])
    elif postback_data["方式"] == "entertainment":
        print("娛樂費為" + str(postback_data["price"]) + "元" + "\n" + "細項: " + postback_data["詳情"])
