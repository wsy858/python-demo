# -*- coding: utf-8 -*-
from kafka import KafkaProducer
import csv
import time


def send(file_name, kafka_server, topic):
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    with open(file_name) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            phone = str(row[0])
            message = bytes(('{"user_name": "wsy", "update_time": "2020-04-14 10:34:38", "phone": "' + phone
                             + r'","user_id":"3620193713499","biz_no": "finTest000000000004"} ')
                            .encode("utf-8"))
            future = producer.send(topic, message)
            result = future.get(timeout=60)
            print(result)


if __name__ == "__main__":
    print(r"start-------------------" + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    send(r"E:\Users\Desktop\query-impala-258060.csv", r"10.201.5.57:9092", r"fin.data.variable.params.flinktest")
    print(r"end-------------------" + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
