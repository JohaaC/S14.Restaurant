import json
from pathlib import Path


class ArchivoServicio:

    def leer_json(self, ruta):

        ruta = Path(ruta)

        if not ruta.exists():
            return []

        try:
            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                return json.load(archivo)

        except json.JSONDecodeError:

            return []

    def guardar_json(self, ruta, datos):

        ruta = Path(ruta)

        ruta.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            ruta,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )