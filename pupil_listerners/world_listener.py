import msgpack as serializer
import numpy as np
import zmq

from logger import logger


class WorldListener:

    def __init__(self, glass_id, port_glass_1, ip='localhost'):
        self.glass_id = glass_id
        self.port = port_glass_1
        self.ip = ip

    def world_receiver(self, world_proxy):
        logger.info("Starting Pupil World Frames Listener...")
        ctx = zmq.Context()

        requester = ctx.socket(zmq.REQ)
        ip = self.ip
        requester.connect('tcp://%s:%s' % (ip, self.port))
        requester.send_string('SUB_PORT')
        sub_port = requester.recv_string()
        logger.info("Connecting to port {}".format(sub_port))

        subscriber = ctx.socket(zmq.SUB)
        subscriber.connect('tcp://%s:%s' % (ip, sub_port))
        subscriber.setsockopt_string(zmq.SUBSCRIBE, 'frame.world')

        try:
            while True:
                topic = subscriber.recv_string()
                info = serializer.unpackb(subscriber.recv(), encoding='utf-8')
                # logger.info("Received Topic - {} Frame - {}, Timestamp - {}".format(topic, info['index'], info['timestamp']))
                frame = []
                while subscriber.get(zmq.RCVMORE):
                    frame.append(subscriber.recv())
                frame_data = np.frombuffer(frame[0], dtype=np.uint8).reshape(info['height'], info['width'], 3)
                world_proxy.update(info['timestamp'], info['index'], frame_data)
        except:
            requester.close()
            subscriber.close()
            ctx.term()
            logger.warn('Listener shut down successfully')
            raise
