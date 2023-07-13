def particleError(particle):
    if particle not in ['n', 'p', 'e']:
        raise ValueError(
            'Invalid particle type. The particle must be "n", "p", or "e".')
