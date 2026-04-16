# arquivo: acudes_alagoas_dnocs_dataset.py

# # =========================
# Esse script geolocaliza açudes do estado de Alagoas
# Base de dados formada a partir de arquivos coletados diretamente no Departamento Nacional de Obras contra as Secas
# Dados cruzados com a base da ANA - Agência Nacional das Águas e IBGE - Instituto Brasileiro Geográfico e Estatístico
# Reservatórios construídos e sob administração do DNOCS
# =========================
# formato de saída: GeoJSON e JSON (compatível com QGIS)

import json

acudes_alagoas = [
    {
        "nome": "Arapiraca",
        "municipios_limite": ["Arapiraca"],
        "lat": -9.6606,
        "lon": -36.7664
    },
    {
        "nome": "Campo Grande",
        "municipios_limite": ["Campo Grande"],
        "lat": -9.9431964,
        "lon": -36.7863070
    },
    {
        "nome": "Caraibinhas (Entra Gavião)",
        "municipios_limite": ["Palmeira dos Índios"],
        "lat": -9.367,
        "lon": -36.617
    },
    {
        "nome": "Colégio (Mandacaru)",
        "municipios_limite": ["Feira Grande"],
        "lat": -9.9523201,
        "lon": -36.714
    },
    {
        "nome": "Craíbas dos Nunes",
        "municipios_limite": ["Craíbas"],
        "lat": -9.6249657,
        "lon": -36.821
    },
    {
        "nome": "Dois Riachos",
        "municipios_limite": ["Dois Riachos"],
        "lat": -9.3591031,
        "lon": -37.0122551
    },
    {
        "nome": "Gravatá (Bom Vermelho)",
        "municipios_limite": ["Mata Grande"],
        "lat": -8.9944962,
        "lon": -37.6826372
    },
    {
        "nome": "Jacaré dos Homens",
        "municipios_limite": ["Jacaré dos Homens"],
        "lat": -9.6331,
        "lon": -37.2006
    },
    {
        "nome": "Jaramataia",
        "municipios_limite": ["Jaramataia"],
        "lat": -9.658,
        "lon": -37.002
    },
    {
        "nome": "Major Isidoro",
        "municipios_limite": ["Major Isidoro"],
        "lat": -9.53476632005915,
        "lon": -36.97627473651446
    },
    {
        "nome": "Maravilha",
        "municipios_limite": ["Maravilha"],
        "lat": -9.236,
        "lon": -37.355
    },
    {
        "nome": "Pai Mané",
        "municipios_limite": ["Dois Riachos"],
        "lat": -9.312,
        "lon": -37.054
    },
    {
        "nome": "Palmeira dos Índios",
        "municipios_limite": ["Igaci"],
        "lat": -9.284,
        "lon": -36.677
    },
    {
        "nome": "Pariconha",
        "municipios_limite": ["Água Branca"],
        "lat": -9.254,
        "lon": -37.997
    },
    {
        "nome": "Poço das Trincheiras",
        "municipios_limite": ["Poço das Trincheiras"],
        "lat": -9.3087693,
        "lon": -37.2798461
    },
    {
        "nome": "Ponciano",
        "municipios_limite": ["Girau do Ponciano"],
        "lat": -9.877,
        "lon": -36.829
    },
    {
        "nome": "Retiro",
        "municipios_limite": ["Palestina"],
        "lat": -9.6697475,
        "lon": -37.329
    },
    {
        "nome": "Riacho do Bode",
        "municipios_limite": ["Santana do Ipanema"],
        "lat": -9.371,
        "lon": -37.245
    },
    {
        "nome": "São José da Tapera",
        "municipios_limite": ["São José da Tapera"],
        "lat": -9.558,
        "lon": -37.381
    },
    {
        "nome": "Sertão de Baixo (São Marcos)",
        "municipios_limite": ["Major Isidoro"],
        "lat": -9.5672396,
        "lon": -36.9914958
    },
    {
        "nome": "Sinimbu (Barragem Velha)",
        "municipios_limite": ["Delmiro Gouveia"],
        "lat": -9.3411482,
        "lon": -37.953
    },
    {
        "nome": "Socorro",
        "municipios_limite": ["Mata Grande"],
        "lat": -8.963,
        "lon": -37.766
    },
    {
        "nome": "Travessia",
        "municipios_limite": ["Major Isidoro"],
        "lat": -9.5695388,
        "lon": -36.9244167
    }
]

if __name__ == "__main__":
    with open("acudes_alagoas.json", "w", encoding="utf-8") as f:
        json.dump(acudes_alagoas, f, ensure_ascii=False, indent=2)

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for acude in acudes_alagoas:
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

    with open("acudes_alagoas.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"Arquivos gerados: acudes_alagoas.json e acudes_alagoas.geojson")
    print(f"Total de açudes com coordenadas: {len(geojson['features'])}")