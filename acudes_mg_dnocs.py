# arquivo: acudes_minasgerais_dnocs_dataset.py

# # =========================
# Esse script geolocaliza açudes do estado de Minas Gerais
# Base de dados formada a partir de arquivos coletados diretamente no Departamento Nacional de Obras contra as Secas
# Dados cruzados com a base da ANA - Agência Nacional das Águas, IBGE - Instituto Brasileiro Geográfico e Estatístico, e OpenStreetMap
# Reservatórios construídos e sob administração do DNOCS
# =========================
# formato de saída: GeoJSON e JSON (compatível com QGIS)


import json

acudes_minas_gerais = [
    {
        "nome": "Angical",
        "municipios_limite": ["Monte Azul"],
        "lat": -15.1258,
        "lon": -42.8764
    },
    {
        "nome": "Catuti",
        "municipios_limite": ["Catuti"],
        "lat": -15.35677932118466,
        "lon": -42.96970511835213
    },
    {
        "nome": "Coração de Jesus",
        "municipios_limite": ["Coração de Jesus"],
        "lat": -16.6847,
        "lon": -44.3639
    },
    {
        "nome": "Matrona",
        "municipios_limite": ["Salinas"],
        "lat": -16.100260418903822,
        "lon": -42.264248259533524
    },
    {
        "nome": "Miralta",
        "municipios_limite": ["Montes Claros"],
        "lat": -16.519185098437365,
        "lon": -43.91358358833199
    }
]

if __name__ == "__main__":
    # Salva como JSON simples
    with open("acudes_minas_gerais.json", "w", encoding="utf-8") as f:
        json.dump(acudes_minas_gerais, f, ensure_ascii=False, indent=2)

    # Gera GeoJSON
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for acude in acudes_minas_gerais:
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

    with open("acudes_minas_gerais.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"Arquivos gerados: acudes_minas_gerais.json e acudes_minas_gerais.geojson")
    print(f"Total de açudes com coordenadas: {len(geojson['features'])}")