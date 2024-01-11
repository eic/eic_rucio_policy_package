
from .path_gen import construct_surl_eic
from .lfn2pfn import lfn2pfn_eic
from .extract_scope import extract_scope_eic

SUPPORTED_VERSION = [ "1.30", "1.31", "32" ]

def get_algorithms():
    return {'lfn2pfn': {'eic': lfn2pfn_eic},
            'surl': {'eic': construct_surl_eic},
            'scope': {'eic': extract_scope_eic}
           }

