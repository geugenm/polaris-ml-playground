"""Module for PolarisConfig class
"""

import json

from mergedeep import merge


# Disabling check for public methods; the python_json_config class has
# all the methods we need, and we're explicitly deferring to it.
class PolarisConfig():
    """Class for Polaris configuration
    """

    _DEFAULT_CONFIGFILE = 'polaris_config.json'
    _DEFAULT_CACHEDIR = 'cache'
    _DEFAULT_NORMALIZED_FILE = 'normalized_frames.json'
    _DEFAULT_GRAPHDIR = 'graph'
    _DEFAULT_OUTPUT_GRAPH_FILE = 'graph.json'
    _DEFAULT_LOGDIR = 'log'

    _DEFAULT_SETTINGS = {
        'file_layout': {
            'root_dir': '/tmp/polaris',
        },
        'satellite': {
            'batch': {
                'learn': True,
                'fetch': True,
                'viz': False,
            }
        }
    }

    def __init__(self, file=_DEFAULT_CONFIGFILE, defaults=None):
        """Initialize Polaris configuration
        """
        defaults = defaults or self._DEFAULT_SETTINGS
        with open(file) as f_handle:
            # data from file overrides the defaults
            self._data = merge({}, defaults, json.load(f_handle))

    @property
    def root_dir(self):
        """Root directory for configuration
        """
        return self._data['file_layout']['root_dir']

    @root_dir.setter
    def root_dir(self, value):
        """Set root directory
        """
        self._data['file_layout']['root_dir'] = value

    @property
    def name(self):
        """Return name of satellite configuration
        """
        return self._data['satellite']['name']

    @name.setter
    def name(self, value):
        """Set name of satellite configuration
        """
        self._data['satellite']['name'] = value

    @property
    def cache_dir(self):
        """Return cache directory
        """
        return f'{self.root_dir}/{self.name}/{self._DEFAULT_CACHEDIR}'

    @property
    def normalized_file_path(self):
        """Return path to satellite-specific normalized frames file

        """
        # 'cache_dir': 'cache'
        return f'{self.cache_dir}/{self._DEFAULT_NORMALIZED_FILE}'

    @property
    def graph_dir(self):
        """Return graph directory
        """
        return f'{self.root_dir}/{self.name}/{self._DEFAULT_GRAPHDIR}'

    @property
    def output_graph_file(self):
        """Return path to graph file
        """
        return f'{self.graph_dir}/{self._DEFAULT_OUTPUT_GRAPH_FILE}'

    @property
    def log_dir(self):
        """Return log directory
        """
        return f'{self.root_dir}/{self._DEFAULT_LOGDIR}'

    @property
    def log_file(self):
        """Return path to log file
        """
        return f'{self.log_dir}/{self.name}.log'

    @property
    def batch_settings(self):
        """Batch settings
        """
        return self._data['satellite']['batch']
