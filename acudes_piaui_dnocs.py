# arquivo: acudes_piaui_dnocs_dataset.py

# # =========================
# Esse script geolocaliza açudes do estado do Piauí
# Base de dados formada a partir de arquivos coletados diretamente no Departamento Nacional de Obras contra as Secas
# Dados cruzados com a base da ANA - Agência Nacional das Águas, IBGE - Instituto Brasileiro Geográfico e Estatístico, e OpenStreetMap
# Reservatórios construídos e sob administração do DNOCS
# =========================
# formato de saída: GeoJSON e JSON (compatível com QGIS)

import json

acudes_piaui = [
    {
        "nome": "Aldeias",
        "municipios_limite": ["São Raimundo Nonato"],
        "lat": -9.0153,
        "lon": -42.6981
    },
    {
        "nome": "Algodoes II",
        "municipios_limite": ["Curimatá"],
        "lat": -10.0347,
        "lon": -44.2956
    },
    {
        "nome": "Anajás",
        "municipios_limite": ["Piripiri"],
        "lat": -4.2733,
        "lon": -41.7764
    },
    {
        "nome": "Barreiras",
        "municipios_limite": ["Fronteiras"],
        "lat": -7.0847,
        "lon": -40.6144
    },
    {
        "nome": "Beneditinos",
        "municipios_limite": ["Beneditinos"],
        "lat": -5.4567,
        "lon": -42.3633
    },
    {
        "nome": "Bocaina",
        "municipios_limite": ["Bocaina"],
        "lat": -6.9417,
        "lon": -41.3200
    },
    {
        "nome": "Bonfim",
        "municipios_limite": ["São Raimundo Nonato"],
        "lat": -9.0153,
        "lon": -42.6981
    },
    {
        "nome": "Cajazeiras",
        "municipios_limite": ["Pio IX"],
        "lat": -6.8308,
        "lon": -40.6092
    },
    {
        "nome": "Caldeirão",
        "municipios_limite": ["Piripiri"],
        "lat": -4.3503,
        "lon": -41.7153
    },
    {
        "nome": "Campo Maior",
        "municipios_limite": ["Campo Maior"],
        "lat": -4.8275,
        "lon": -42.1686
    },
    {
        "nome": "Caracol",
        "municipios_limite": ["Caracol"],
        "lat": -9.2797,
        "lon": -43.3297
    },
    {
        "nome": "Estreito",
        "municipios_limite": ["Padre Marcos"],
        "lat": -7.3511,
        "lon": -40.9025
    },
    {
        "nome": "Fátima",
        "municipios_limite": ["Picos"],
        "lat": -7.0769,
        "lon": -41.4669
    },
    {
        "nome": "Ingazeiras",
        "municipios_limite": ["Paulistana"],
        "lat": -8.1397,
        "lon": -41.1500
    },
    {
        "nome": "Jenipapo",
        "municipios_limite": ["São João do Piauí", "São José do Piauí"],
        "lat": -8.3453,
        "lon": -42.2642
    },
    {
        "nome": "Joana",
        "municipios_limite": ["Pedro II"],
        "lat": -4.4253,
        "lon": -41.4583
    },
    {
        "nome": "Malhadinha",
        "municipios_limite": ["Dirceu Arcoverde"],
        "lat": -9.3378,
        "lon": -42.4344
    },
    {
        "nome": "Nonato",
        "municipios_limite": ["São Raimundo Nonato"],
        "lat": -9.0153,
        "lon": -42.6981
    },
    {
        "nome": "Pé de Serra",
        "municipios_limite": ["Piripiri"],
        "lat": -4.2733,
        "lon": -41.7764
    },
    {
        "nome": "Pedra Redonda",
        "municipios_limite": ["Conceição do Canindé"],
        "lat": -7.8767,
        "lon": -40.8858
    },
    {
        "nome": "Petrônio Portela",
        "municipios_limite": ["São Raimundo Nonato"],
        "lat": -9.0153,
        "lon": -42.6981
    },
    {
        "nome": "Piaus",
        "municipios_limite": ["São Julião"],
        "lat": -7.0858,
        "lon": -40.8264
    },
    {
        "nome": "Poços",
        "municipios_limite": ["Simplício Mendes"],
        "lat": -7.8542,
        "lon": -41.9100
    },
    {
        "nome": "Salinas",
        "municipios_limite": ["São Francisco do Piauí"],
        "lat": -7.2503,
        "lon": -42.5433
    },
    {
        "nome": "Umburanas",
        "municipios_limite": ["Piripiri"],
        "lat": -4.2733,
        "lon": -41.7764
    }
]

if __name__ == "__main__":
    # Salva como JSON simples
    with open("acudes_piaui.json", "w", encoding="utf-8") as f:
        json.dump(acudes_piaui, f, ensure_ascii=False, indent=2)

    # Gera GeoJSON
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for acude in acudes_piaui:
        if acude["lat"] is not None and acude["lon"] is not None:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [acude["lon"], acude["lat"]]
                },
                "properties": {
                    "nome": acude["nome"],
                    "municipios_limite": acude["municipios_limite"]
                }
            }
            geojson["features"].append(feature)

    with open("acudes_piaui.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"Arquivos gerados: acudes_piaui.json e acudes_piaui.geojson")
    print(f"Total de açudes com coordenadas: {len(geojson['features'])}")