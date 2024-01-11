def extract_scope_eic(did, scopes):
    split_did = did.split('/')
    if did.startswith('/eic/user/'):
        if len(split_did) > 4:
            if len(split_did[3]) == 1 and 'user.%s' % (split_did[4]) in scopes:
                return 'user.%s' % split_did[4], did
        if len(split_did) > 3:
            if 'user.%s' % (split_did[3]) in scopes:
                return 'user.%s' % split_did[3], did
        return 'user', did
    if did.startswith('/eic/group/'):
        if len(split_did) > 4:
            if 'group.%s' % (split_did[4]) in scopes:
                return 'group.%s' % split_did[4], did
        return 'group', did
    scope = 'eic'
    return scope, did