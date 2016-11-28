# -*- coding: utf-8 -*-

def sg_service_interfaces(a, service):
    '''Find what interfaces a given service is on'''
    # This only works because we know the schema of the dict in advance
    interfaces = []
    for iface in a:
        if 'services' in iface:
            if service in iface["services"]:
                interfaces.append(iface["name"])
    return " ".join(interfaces)

def sg_interfaces_with_attribute(a, attribute):
    '''Find what interfaces a given service is on'''
    # This only works because we know the schema of the dict in advance
    interfaces = []
    for iface in a:
        if attribute in iface:
            interfaces.append(iface)
    return interfaces

class FilterModule(object):
    def filters(self):
        return {
            "sg_service_interfaces": sg_service_interfaces,
            "sg_interfaces_with_attribute": sg_interfaces_with_attribute,
        }
