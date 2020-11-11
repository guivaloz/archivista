"""
Archivista, Sección Breadcrumb
"""
from pathlib import Path


class SeccionBreadcrumb():
    """ Sección Breadcrumb """

    def __init__(self, config, ruta, nivel):
        self.config = config
        if isinstance(ruta, str):
            self.ruta = Path(ruta)
        else:
            self.ruta = ruta
        self.nivel = nivel

    def alimentar(self):
        """ Alimentar """

    def contenido(self):
        """ Contenido entrega texto markdown """
        return """
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="#">Home</a></li>
                    <li class="breadcrumb-item"><a href="#">Library</a></li>
                    <li class="breadcrumb-item active" aria-current="page">Data</li>
                </ol>
            </nav>
        """

    def __repr__(self):
        """ Representación """
        return '<SeccionBreadcrumb>'
