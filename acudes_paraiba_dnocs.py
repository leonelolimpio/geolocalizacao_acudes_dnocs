# arquivo: acudes_paraiba_simplificado.py

# =========================
# EEsse script geolocaliza açudes do estado da Paraíba
# Base de dados formada a partir de arquivos coletados diretamente no Departamento Nacional de Obras contra as Secas
# Dados cruzados com a base da ANA - Agência Nacional das Águas e IBGE - Instituto Brasileiro Geográfico e Estatístico
# Reservatórios construídos e sob administração do DNOCS pelo programa de Açudagem Pública
# =========================
# formato de saída: GeoJSON e JSON (compatível com QGIS)

import json

acudes_paraiba = [
    {
        "nome": "Algodões",
        "municipios_limite": ["Remígio"],
        "lat": -6.9528,
        "lon": -35.7842
    },
    {
        "nome": "Barra do Xandu",
        "municipios_limite": ["Cabaceiras"],
        "lat": -7.4431,
        "lon": -36.2478
    },
    {
        "nome": "Batalhão",
        "municipios_limite": ["Taperoá"],
        "lat": -7.2075,
        "lon": -36.8269
    },
    {
        "nome": "Bodocongó",
        "municipios_limite": ["Campina Grande"],
        "lat": -7.2131,
        "lon": -35.9165
    },
    {
        "nome": "Brabo",
        "municipios_limite": ["Cabaceiras"],
        "lat": -7.4768,
        "lon": -36.2567
    },
    {
        "nome": "Cajazeiras I - Açude Grande",
        "municipios_limite": ["Cajazeiras"],
        "lat": -6.8904317256097505,
        "lon": -38.575467487705865
    },
    {
        "nome": "Cedro II",
        "municipios_limite": ["Princesa Isabel"],
        "lat": -7.7395,
        "lon": -37.9923
    },
    {
        "nome": "Congo dos Campos",
        "municipios_limite": ["São José do Cariré"],
        "lat": -6.4292,
        "lon": -36.6179
    },
    {
        "nome": "Cruz de Pocinhos",
        "municipios_limite": ["Pocinhos"],
        "lat": -7.0858,
        "lon": -36.0653
    },
    {
        "nome": "Cruz do Riacho",
        "municipios_limite": ["Umbuzeiro"],
        "lat": -7.6950,
        "lon": -35.6583
    },
    {
        "nome": "Curimataú",
        "municipios_limite": ["Cuité"],
        "lat": -6.4864,
        "lon": -36.1367
    },
    {
        "nome": "Dona Inês",
        "municipios_limite": ["Bananeiras"],
        "lat": -6.7467,
        "lon": -35.6317
    },
    {
        "nome": "Engº Arco Verde",
        "municipios_limite": ["Condado"],
        "lat": -6.9086,
        "lon": -37.5889
    },
    {
        "nome": "Engº Ávidos",
        "municipios_limite": ["Cajazeiras"],
        "lat": -6.985823427656068,
        "lon": -38.45404350589716
    },
    {
        "nome": "Boqueirão de Cabaceiras",
        "municipios_limite": ["Boqueirão", "Cabaceiras"],
        "lat": -7.4889,
        "lon": -36.1408
    },
    {
        "nome": "Escondido",
        "municipios_limite": ["Belém do Brejo da Cruz"],
        "lat": -6.188947407735043,
        "lon": -37.54384530601927
    },
    {
        "nome": "Estevam Marinho - Curema",
        "municipios_limite": ["Curemas"],
        "lat": -6.7525,
        "lon": -37.9947
    },
    {
        "nome": "Fragoso",
        "municipios_limite": ["Solânea"],
        "lat": -6.7772,
        "lon": -35.6619
    },
    {
        "nome": "Gado Bravo",
        "municipios_limite": ["Aroeiras"],
        "lat": -7.5425,
        "lon": -35.7111
    },
    {
        "nome": "Ingá II",
        "municipios_limite": ["Ingá"],
        "lat": -7.2808,
        "lon": -35.6092
    },
    {
        "nome": "Jatobá I",
        "municipios_limite": ["Patos"],
        "lat": -7.0025,
        "lon": -37.2892
    },
    {
        "nome": "Jatobá II",
        "municipios_limite": ["Princesa Isabel"],
        "lat": -7.7395,
        "lon": -37.9923
    },
    {
        "nome": "Lagoa do Arroz",
        "municipios_limite": ["Cajazeiras"],
        "lat": -6.797372844250824,
        "lon": -38.572736178749395
    },
    {
        "nome": "Lagoa do Meio",
        "municipios_limite": ["Taperoá"],
        "lat": -7.2075,
        "lon": -36.8269
    },
    {
        "nome": "Macapá",
        "municipios_limite": ["Princesa Isabel"],
        "lat": -7.7395,
        "lon": -37.9923
    },
    {
        "nome": "Mãe d'água",
        "municipios_limite": ["Coremas"],
        "lat": -7.0292,
        "lon": -37.9536
    },
    {
        "nome": "Mogeiro",
        "municipios_limite": ["Mogeiro"],
        "lat": -7.2992,
        "lon": -35.4792
    },
    {
        "nome": "Negrinhos",
        "municipios_limite": ["Soledade"],
        "lat": -7.0572,
        "lon": -36.3692
    },
    {
        "nome": "Pilões",
        "municipios_limite": ["São João do Rio do Peixe"],
        "lat": -6.693039,
        "lon": -38.519116
    },
    {
        "nome": "Poções",
        "municipios_limite": ["Conceição"],
        "lat": -7.889000,
        "lon": -36.997000
    },
    {
        "nome": "Riacho dos Cavalos",
        "municipios_limite": ["Catolé do Rocha"],
        "lat": -6.420120,
        "lon": -37.659022
    },
    {
        "nome": "Riacho Santo Antonio",
        "municipios_limite": ["Cabaceiras"],
        "lat": -7.4768,
        "lon": -36.2567
    },
    {
        "nome": "Santa Inês",
        "municipios_limite": ["Conceição"],
        "lat": -7.5622,
        "lon": -38.5200
    },
    {
        "nome": "Santa Luzia",
        "municipios_limite": ["Santa Luzia do Sabugi"],
        "lat": -6.8719,
        "lon": -36.9192
    },
    {
        "nome": "São Gonçalo",
        "municipios_limite": ["Sousa"],
        "lat": -6.8451,
        "lon": -38.3154
    },
    {
        "nome": "São Mamede",
        "municipios_limite": ["São Mamede"],
        "lat": -6.9306,
        "lon": -37.0719
    },
    {
        "nome": "São Pedro",
        "municipios_limite": ["Campina Grande"],
        "lat": -7.2203,
        "lon": -35.8811
    },
    {
        "nome": "Serra Branca",
        "municipios_limite": ["Serra Branca"],
        "lat": -7.4806,
        "lon": -36.6653
    },
    {
        "nome": "Soledade",
        "municipios_limite": ["Soledade"],
        "lat": -7.0572,
        "lon": -36.3692
    },
    {
        "nome": "Sumé",
        "municipios_limite": ["Sumé"],
        "lat": -7.6736,
        "lon": -36.9053
    },
    {
        "nome": "Tribofe",
        "municipios_limite": ["Belém"],
        "lat": -6.6960,
        "lon": -35.5309
    }
]

# Isso transforma as informações de latitude e longitude em ponto geométricos

if __name__ == "__main__":
    with open("acudes_paraiba.json", "w", encoding="utf-8") as f:
        json.dump(acudes_paraiba, f, ensure_ascii=False, indent=2)

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for acude in acudes_paraiba:
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

    with open("acudes_paraiba.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"Arquivos gerados: acudes_paraiba.json e acudes_paraiba.geojson")
    print(f"Total de açudes com coordenadas: {len(geojson['features'])}")