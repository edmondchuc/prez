import os
import time

import requests

os.system("docker context use default")
response = os.system(
    "docker run -d -v ${PWD}/dev/dev-config.ttl:/fuseki/config.ttl -p 3030:3030 ghcr.io/zazuko/fuseki-geosparql:4.7.0"
)

time.sleep(15)


def setup_sp():
    url = "http://localhost:3030/sp/"

    payload = {}
    files = [
        (
            "myfile",
            (
                "geofabric_small.ttl",
                open("tests/data/spaceprez/input/geofabric_small.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile2",
            (
                "gnaf_small.ttl",
                open("tests/data/spaceprez/input/gnaf_small.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile3",
            (
                "labels.ttl",
                open("tests/data/spaceprez/input/labels.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile4",
            (
                "sandgate.ttl",
                open("tests/data/spaceprez/input/sandgate.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile5",
            (
                "multiple_object.ttl",
                open("tests/data/spaceprez/input/multiple_object.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile6",
            (
                "dublin_core_terms.ttl",
                open("tests/data/vocprez/input/dublin_core_terms.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
    ]
    headers = {}

    response = requests.request(
        "POST",
        url,
        headers=headers,
        data=payload,
        files=files,
        params={"graph": "http://exampledatagraph"},
    )

    print(response.text)


def setup_vp():
    url = "http://localhost:3030/vp/"

    payload = {}
    files = [
        (
            "myfile",
            (
                "alteration-types.ttl",
                open("tests/data/vocprez/input/alteration-types.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile2",
            (
                "contacttype.ttl",
                open("tests/data/vocprez/input/contacttype.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile6",
            (
                "dublin_core_terms.ttl",
                open("tests/data/vocprez/input/dublin_core_terms.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
    ]
    headers = {}

    response = requests.request(
        "POST",
        url,
        headers=headers,
        data=payload,
        files=files,
        params={"graph": "http://exampledatagraph"},
    )

    print(response.text)


def setup_cp():
    url = "http://localhost:3030/cp/"

    payload = {}
    files = [
        (
            "myfile",
            (
                "_idn-ac.ttl",
                open("tests/data/catprez/input/_idn-ac.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile2",
            (
                "_idn-dc.ttl",
                open("tests/data/catprez/input/_idn-dc.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile3",
            (
                "_system-catalog.ttl",
                open("tests/data/catprez/input/_system-catalog.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile4",
            (
                "AAC-SA.ttl",
                open("tests/data/catprez/input/AAC-SA.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile5",
            (
                "agents.ttl",
                open("tests/data/catprez/input/agents.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
        (
            "myfile6",
            (
                "dublin_core_terms.ttl",
                open("tests/data/vocprez/input/dublin_core_terms.ttl", "rb"),
                "application/octet-stream",
            ),
        ),
    ]
    headers = {}

    response = requests.request(
        "POST",
        url,
        headers=headers,
        data=payload,
        files=files,
        params={"graph": "http://exampledatagraph"},
    )

    print(response.text)


setup_sp()
setup_vp()
setup_cp()
