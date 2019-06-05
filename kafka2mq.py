#!/usr/bin/python

import json
import websocket
from kafka import KafkaConsumer
import tornado.options

tornado.options.define("mqserver", default='', type=str, help="address of message queue server.")
tornado.options.define("kserver",  default='', type=str, help="address of kafka server .")
tornado.options.define("group",    default='', type=str, help="kafka group.")
tornado.options.define("topic",    default='', type=str, help="kafka topic.")

if __name__ == '__main__':
    tornado.options.parse_command_line()

    ws = websocket.create_connection(tornado.options.options.mqserver)

    consumer = KafkaConsumer(tornado.options.options.topic , group_id=tornado.options.options.group , bootstrap_servers=tornado.options.options.kserver)

    print 'starting forwording!'

    for msg in consumer:
        ws.send(msg.value)

