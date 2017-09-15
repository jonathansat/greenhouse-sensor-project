#!/usr/bin/env python

import random
import time


class Sensor(object):
    """
    I represent the abstract parent class that dictates what a sensor should do. I'm not much use unless
    you implement me and override my METRIC_SYMBOL and value().

    And I also take care of representing how I look - which is basically the value
    of my sensor and the metric that dictates the type of value I represent.
    Example:
        23C     <-- 23 degrees celsius
        2L      <-- 2 litres
    """
    METRIC_SYMBOL = None

    def value(self):
        raise NotImplementedError('You must override this method')

    def __str__(self):
        return '%s: %s' % (self.METRIC_SYMBOL, self.value())


class SensorStubMixin(object):
    """
    I represent a mixin class, a class which can provide additional functionality
    to another class without necessarily being meaningful to the inheritance hierarchy.

    As a sensor stub, I override Sensor's value() method and just return a random value
    which could be interpreted as a real-world value from an actual physical sensor.
    """

    def __init__(self, min_value=20, max_value=25):
        self.min = min_value
        self.max = max_value

    def value(self):
        return random.randint(self.min, self.max)


class TemperatureSensor(SensorStubMixin, Sensor):
    METRIC_SYMBOL = 'C'


class WaterLevelSensor(SensorStubMixin, Sensor):
     METRIC_SYMBOL = 'L'


if __name__ == "__main__":
    print('Initialising sensors..')
    sensors = (
        TemperatureSensor(),
        TemperatureSensor(),
        WaterLevelSensor(min_value=0, max_value=5),
    )

    print('Starting sensor reading event loop..')
    while True:
        for sensor in sensors:
            print('{sensor_name}: {level}{level_metric}'.format(
                sensor_name=sensor.__class__,
                level=sensor.value(),
                level_metric=sensor.METRIC_SYMBOL
            ))
        print('\n')
        time.sleep(2)

