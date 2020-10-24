import pika 

credentials = pika.PlainCredentials('yunato', 'EashAnicOc3Op')
parameters = pika.ConnectionParameters('10.10.10.190',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel.basic_publish(exchange='', routing_key='plugin_data',
                      body='http://127.0.0.1:8080/root.lua')
connection.close()
