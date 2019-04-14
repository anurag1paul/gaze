import zmq
import msgpack as serializer
import numpy as np

from logger import logger
from algo.kalman import OnlineKalman


class EyeListener:

    def __init__(self, glass_id, eye_id, port_glass_1):
        self.glass_id = glass_id
        self.eye_id = eye_id
        self.port = port_glass_1
        self.kalman = None

    def eye_receiver(self, eye_proxy):
        logger.info("Starting Eye_{} Frames Listener...".format(self.eye_id))

        ctx = zmq.Context()

        requester = ctx.socket(zmq.REQ)
        ip = 'localhost'
        requester.connect('tcp://%s:%s' % (ip, self.port))
        requester.send_string('SUB_PORT')
        sub_port = requester.recv_string()
        logger.info("Connecting to port {}".format(sub_port))

        subscriber = ctx.socket(zmq.SUB)
        subscriber.connect('tcp://%s:%s' % (ip, sub_port))
        subscriber.setsockopt_string(zmq.SUBSCRIBE, 'gaze.3d.{}'.format(self.eye_id))

        try:
            while True:
                topic = subscriber.recv_string()
                info = serializer.unpackb(subscriber.recv(), encoding='utf-8')
                # logger.info("Received Topic - {}, Timestamp - {}, Norm_Pos - {}, Confidence - {}".format(topic, info['timestamp'], info['norm_pos'], info['confidence']))

                pupil_x, pupil_y = self.denormalize(info['norm_pos'], (1280, 720), flip_y=True)

                if self.kalman is None:
                    self.kalman = OnlineKalman((pupil_x, pupil_y, info['timestamp']))

                pupil_filtered = self.kalman.predict((pupil_x, pupil_y, info['timestamp']))

                eye_proxy.update(info['timestamp'], np.array(pupil_filtered), info['confidence'])

        except KeyboardInterrupt:
            requester.close()
            subscriber.close()
            ctx.term()
            logger.warn('Listener shut down successfully')
            raise

    @staticmethod
    def denormalize(pos, size, flip_y=False):
        width, height = size
        x = pos[0]
        y = pos[1]
        x *= width
        if flip_y:
            y = 1 - y
        y *= height
        return x, y
