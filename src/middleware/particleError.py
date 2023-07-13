def particleError(particle):
    # Retorna um erro caso a particula não seja n, p ou e
    if particle not in ['n', 'p', 'e']:
        raise ValueError(
            'Invalid particle type. The particle must be "n", "p", or "e".')
