import json
import netengine
import os

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict  # python < 2.7


__all__ = ['BaseBackend']


class BaseBackend(object):
    """
    Base NetEngine Backend
    """

    __netengine__ = True
    _dict = OrderedDict

    def __str__(self):
        raise NotImplementedError("Not implemented, must be extended")

    def __repr__(self):
        """ returns unicode string represantation """
        return self.__str__()

    def __unicode__(self):
        """ unicode __str__() for python2.7 """
        return unicode(self.__str__())

    def validate(self):
        raise NotImplementedError('Not implemented')

    def to_dict(self):
        raise NotImplementedError('Not implemented')

    def to_json(self, **kwargs):
        dictionary = self.to_dict()
        return json.dumps(dictionary, **kwargs)

    @property
    def os(self):
        """
        Not Implemented

        should return a tuple in which
        the first element is the OS name and
        the second element is the OS version
        """
        raise NotImplementedError('Not implemented')

    @property
    def name(self):
        """
        Not Implemented

        should return a string containing the device name
        """
        raise NotImplementedError('Not implemented')

    @property
    def model(self):
        """
        Not Implemented

        should return a string containing the device model
        """
        raise NotImplementedError('Not implemented')

    @property
    def RAM_total(self):
        """
        Not Implemented

        should return a string containing the device RAM in bytes
        """
        raise NotImplementedError('Not implemented')

    @property
    def uptime(self):
        """
        Not Implemented

        should return an integer representing the number of seconds of uptime
        """
        raise NotImplementedError('Not implemented')

    @property
    def uptime_tuple(self):
        """
        Not Implemented

        should return tuple (days, hours, minutes)
        """
        raise NotImplementedError('Not implemented')

    @property
    def ethernet_standard(self):
        raise NotImplementedError('Not implemented')

    @property
    def ethernet_duplex(self):
        raise NotImplementedError('Not implemented')

    @property
    def wireless_channel_width(self):
        raise NotImplementedError('Not implemented')

    @property
    def wireless_mode(self):
        raise NotImplementedError('Not implemented')

    @property
    def wireless_channel(self):
        raise NotImplementedError('Not implemented')

    @property
    def wireless_output_power(self):
        raise NotImplementedError('Not implemented')

    @property
    def wireless_dbm(self):
        raise NotImplementedError('Not implemented')

    @property
    def wireless_noise(self):
        raise NotImplementedError('Not implemented')

    # TODO: this sucks
    @property
    def olsr(self):
        raise NotImplementedError('Not implemented')

    def get_interfaces(self):
        raise NotImplementedError('Not implemented')

    def get_manufacturer(self):
        """ returns the manufacturer of the network interface """
        base = netengine.__file__
        file_path = os.path.dirname(os.path.dirname(base))
        manufacturer_file = open(os.path.join(file_path,"netengine/resources/manufacturer.txt"))
        res = ""
        mac_addr = self.get_interfaces()[1]['hardware_address']
        mac_address1 = mac_addr[0:8].replace(":","")

        for line in manufacturer_file.readlines():
            if mac_address1.encode() in line:
                res = line.split(mac_address1)[1].replace("(base 16)","").split()
                return ",".join(res).replace(","," ")
