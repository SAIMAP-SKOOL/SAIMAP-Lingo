"""Carga el motor de escenas (scenes_it.py + piezas) en un espacio de nombres reutilizable."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))


def load(TR=None, SEEN=None, LOC=None, POET=None):
    ns = {'__file__': os.path.join(HERE, 'scenes_it.py'), 'NO_WRITE': True, 'TR': TR if TR is not None else {}, 'SEEN': SEEN, 'LOC': LOC or {}, 'POET': POET}
    exec(open(os.path.join(HERE, 'scenes_it.py'), encoding='utf8').read(), ns)
    exec(open(os.path.join(HERE, 'scenes_local.py'), encoding='utf8').read(), ns)
    return ns
