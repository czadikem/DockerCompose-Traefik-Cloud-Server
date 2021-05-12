from flask import current_app
import os


class Config:
    def __init__(self, **kwargs):
        def read_config_bool(var: str) -> bool:
            val = os.getenv(var, '0')
            if val.isdigit():
                return bool(int(val))
            return False

        app_config = current_app.config
        self.url = os.getenv('WHOOGLE_CONFIG_URL', '')
        self.lang_search = os.getenv('WHOOGLE_CONFIG_SEARCH_LANGUAGE', '')
        self.lang_interface = os.getenv('WHOOGLE_CONFIG_LANGUAGE', '')
        self.style = os.getenv(
            'WHOOGLE_CONFIG_STYLE',
            open(os.path.join(app_config['STATIC_FOLDER'],
                              'css/variables.css')).read())
        self.block = os.getenv('WHOOGLE_CONFIG_BLOCK', '')
        self.ctry = os.getenv('WHOOGLE_CONFIG_COUNTRY', '')
        self.safe = read_config_bool('WHOOGLE_CONFIG_SAFE')
        self.dark = read_config_bool('WHOOGLE_CONFIG_DARK')
        self.alts = read_config_bool('WHOOGLE_CONFIG_ALTS')
        self.nojs = read_config_bool('WHOOGLE_CONFIG_NOJS')
        self.tor = read_config_bool('WHOOGLE_CONFIG_TOR')
        self.near = os.getenv('WHOOGLE_CONFIG_NEAR', '')
        self.new_tab = read_config_bool('WHOOGLE_CONFIG_NEW_TAB')
        self.get_only = read_config_bool('WHOOGLE_CONFIG_GET_ONLY')
        self.safe_keys = [
            'lang_search',
            'lang_interface',
            'ctry',
            'dark'
        ]

        # Skip setting custom config if there isn't one
        if kwargs:
            mutable_attrs = self.get_mutable_attrs()
            for attr in mutable_attrs:
                if attr in kwargs.keys():
                    setattr(self, attr, kwargs[attr])
                elif attr not in kwargs.keys() and mutable_attrs[attr] == bool:
                    setattr(self, attr, False)

    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        return setattr(self, name, value)

    def __delitem__(self, name):
        return delattr(self, name)

    def __contains__(self, name):
        return hasattr(self, name)

    def get_mutable_attrs(self):
        return {name: type(attr) for name, attr in self.__dict__.items()
                if not name.startswith("__")
                and (type(attr) is bool or type(attr) is str)}

    def is_safe_key(self, key) -> bool:
        """Establishes a group of config options that are safe to set
        in the url.

        Args:
            key (str) -- the key to check against

        Returns:
            bool -- True/False depending on if the key is in the "safe"
            array
        """

        return key in self.safe_keys

    def from_params(self, params) -> 'Config':
        """Modify user config with search parameters. This is primarily
        used for specifying configuration on a search-by-search basis on
        public instances.

        Args:
            params -- the url arguments (can be any deemed safe by is_safe())

        Returns:
            Config -- a modified config object
        """
        for param_key in params.keys():
            if not self.is_safe_key(param_key):
                continue
            self[param_key] = params.get(param_key)
        return self
