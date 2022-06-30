import json
import kafka
from config import constant

consumer = kafka.KafkaConsumer(group_id='payee-group',
                               bootstrap_servers=constant.BOOTSTRAP_SERVER,
                               security_protocol=constant.SECURITY_PROTOCOL,
                               ssl_cafile=constant.SSL_CAFILE,
                               ssl_certfile=constant.SSL_CERTFILE,
                               ssl_keyfile=constant.SSL_KEYFILE,
                               auto_offset_reset="latest")

producer = kafka.KafkaProducer(bootstrap_servers=constant.BOOTSTRAP_SERVER,
                               security_protocol=constant.SECURITY_PROTOCOL,
                               ssl_cafile=constant.SSL_CAFILE,
                               ssl_certfile=constant.SSL_CERTFILE,
                               ssl_keyfile=constant.SSL_KEYFILE,
                               value_serializer=lambda v: json.dumps(v).encode('ascii'),
                               )