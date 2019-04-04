from plugin_base import AsperathosPluginBase, pluginfy

class PluginA(AsperathosPluginBase):
    name = "Plugin A"

plugin = pluginfy(PluginA)
