
from calendar import c
import tunning.config_s as config_s
import tunning.config_st as config_st

class Integrate:
    def __init__(self, config=None, yaml=None):
        assert (config is not None) and \
            (yaml is not None)
        
        if config == "config_s":
            self.config = config_s.cfg 
            config_s.update_config_from_file(yaml)
        else:
            self.config = config_st.cfg 
            config_st.update_config_from_file(yaml)

        self.tunning = self.config
        
    def update_setting(setting,tunning):

