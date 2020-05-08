# -*- coding: utf-8 -*-
from kafka import KafkaProducer
import time


# 每隔一秒发送一条消息到kafka
def send(kafka_server, topic):
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    i = 0
    while i < 100:
        biz_no = "00000" + str(i)
        phone = str(13000000000 + i)
        event_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


        message = bytes((r'{"businessCode":"VAR_100001","paramsInfo":{"userId":"21771940167",'
                         r'"bizNo":"' + biz_no + r'","phone":"' + phone + r'","userName":"王胜勇"},'
                         r'"phone_data":{"emergency_phone": ["1111","2222"]}, "event_time" : "' + event_time + '"} ')
                        .encode("utf-8"))
        future = producer.send(topic, message)
        result = future.get(timeout=60)
        print("biz_no:" + biz_no + ", " + "phone:" + phone + ", " + "event_time:" + event_time)
        print(result)
        print("\n")
        i = i + 1
        time.sleep(1)  # 暂停5s


if __name__ == "__main__":
    print(r"start-------------------" + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    send(r"10.201.5.57:9092", r"fin.data.variable.params.yuxin_yyy")
    print(r"end-------------------" + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
