from abc import ABC, abstractmethod

class AsperathosPluginBase(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

def pluginfy(plugin):

    def wrapper(*args, **kwargs):
        return plugin(*args, **kwargs)

    return wrapper
