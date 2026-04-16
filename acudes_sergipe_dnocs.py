# arquivo: acudes_sergipe_dnocs_dataset.py

# # =========================
# Esse script geolocaliza açudes do estado de Sergipe
# Base de dados formada a partir de arquivos coletados diretamente no Departamento Nacional de Obras contra as Secas
# Dados cruzados com a base da ANA - Agência Nacional das Águas, IBGE - Instituto Brasileiro Geográfico e Estatístico, e OpenStreetMap
# Reservatórios construídos e sob administração do DNOCS
# =========================
# formato de saída: GeoJSON e JSON (compatível com QGIS)


import json

acudes_sergipe = [
    {
        "nome": "Alagadiço",
        "municipios_limite": ["Frei Paulo"],
        "lat": -10.48211475329094,
        "lon": -37.56772810843264
    },
    {
        "nome": "Algodoeiro",
        "municipios_limite": ["Nossa Senhora da Glória", "Porto da Folha"],
        "lat": -10.11976588436125,
        "lon": -37.6020719010072
    },
    {
        "nome": "Carira",
        "municipios_limite": ["Carira"],
        "lat": -10.3608,
        "lon": -37.7006
    },
    {
        "nome": "Coité",
        "municipios_limite": ["Frei Paulo"],
        "lat": -10.55184139804752,
        "lon": -37.57173677951719
    },
    {
        "nome": "Cumbe",
        "municipios_limite": ["Cumbe"],
        "lat": -10.3550,
        "lon": -37.1869
    },
    {
        "nome": "Glória",
        "municipios_limite": ["Nossa Senhora da Glória"],
        "lat": -10.233592169413827,
        "lon": -37.408192072002706
    },
    {
        "nome": "Itabaiana",
        "municipios_limite": ["Itabaiana"],
        "lat": -10.670654163784572,
        "lon": -37.41434989881878
    },
    {
        "nome": "Lagoa do Rancho",
        "municipios_limite": ["Porto da Folha"],
        "lat": -9.959014006337355,
        "lon": -37.444570258741386
    },
    {
        "nome": "Ribeirópolis",
        "municipios_limite": ["Ribeirópolis"],
        "lat": -10.5364,
        "lon": -37.4225
    },
    {
        "nome": "Taboca",
        "municipios_limite": ["Simão Dias"],
        "lat": -10.7389,
        "lon": -37.8106
    },
    {
        "nome": "Três Barras",
        "municipios_limite": ["Gracho Cardoso", "Itabi", "Gararu"],
        "lat": -10.20410757292822,
        "lon": -37.22338668787166
    }
]

if __name__ == "__main__":
    # Salva como JSON simples
    with open("acudes_sergipe.json", "w", encoding="utf-8") as f:
        json.dump(acudes_sergipe, f, ensure_ascii=False, indent=2)

    # Gera GeoJSON
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for acude in acudes_sergipe:
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

    with open("acudes_sergipe.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"Arquivos gerados: acudes_sergipe.json e acudes_sergipe.geojson")
    print(f"Total de açudes com coordenadas: {len(geojson['features'])}")