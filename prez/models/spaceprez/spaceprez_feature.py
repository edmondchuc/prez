from typing import List, Dict, Optional

from rdflib import Graph
from rdflib.namespace import DCTERMS, SKOS, RDFS

from config import *
from models import PrezModel


class SpacePrezFeature(PrezModel):
    # class attributes for property grouping & order
    main_props = [
        DCTERMS.title,
        DCTERMS.description,
    ]
    geom_props = [GEO.hasGeometry]
    hidden_props = [
        DCTERMS.identifier,
    ]

    def __init__(
        self,
        graph: Graph,
        id: Optional[str] = None,
        uri: Optional[str] = None,
    ) -> None:
        super().__init__(graph)

        if id is None and uri is None:
            raise ValueError("Either an ID or a URI must be provided")

        query_by_id = f"""
            ?f dcterms:identifier ?id .
            FILTER (STR(?id) = "{id}")
        """

        query_by_uri = f"""
            BIND (<{uri}> as ?f) 
            ?f dcterms:identifier ?id .
        """

        r = self.graph.query(
            f"""
            PREFIX dcterms: <{DCTERMS}>
            PREFIX geo: <{GEO}>
            PREFIX rdfs: <{RDFS}>
            PREFIX skos: <{SKOS}>
            SELECT *
            WHERE {{
                {query_by_id if id is not None else query_by_uri}
                ?f a geo:Feature ;
                    dcterms:isPartOf ?coll ;
                    dcterms:title ?title .
                # OPTIONAL {{
                #     ?f rdfs:label|skos:prefLabel|dcterms:title ?label .
                # }}
                # BIND(COALESCE(?label, CONCAT("Feature ", ?id)) AS ?title)
                OPTIONAL {{
                    ?f skos:definition|dcterms:description ?desc .
                }}
                ?coll a geo:FeatureCollection ;
                    dcterms:identifier ?coll_id ;
                    rdfs:label|skos:prefLabel|dcterms:title ?coll_label .
                ?d a dcat:Dataset ;
                    dcterms:identifier ?d_id ;
                    rdfs:label|skos:prefLabel|dcterms:title ?d_label .
            }}
        """
        )

        result = r.bindings[0]
        self.uri = result["f"]
        self.id = result["id"]
        self.title = result["title"]
        self.description = result["desc"] if result.get("desc") else None
        self.collection = {
            "uri": result["coll"],
            "id": result["coll_id"],
            "title": result["coll_label"],
        }
        self.dataset = {
            "uri": result["d"],
            "id": result["d_id"],
            "title": result["d_label"],
        }
        self.geometries = {}

    # override
    def to_dict(self) -> Dict:
        props = self._get_properties()
        return {
            "uri": self.uri,
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "properties": props,
            "geometries": self.geometries,
            "collection": self.collection,
            "dataset": self.dataset,
        }

    # override
    def _get_props_dict(self) -> Dict:
        r = self.graph.query(
            f"""
            PREFIX rdfs: <{RDFS}>
            SELECT DISTINCT *
            WHERE {{
                <{self.uri}> ?p ?o .
                OPTIONAL {{
                    ?p rdfs:label ?pLabel .
                }}
                OPTIONAL {{
                    ?o rdfs:label ?oLabel .
                }}
                OPTIONAL {{
                    ?o ?p2 ?o2 .
                    FILTER(ISBLANK(?o))
                    OPTIONAL {{
                        ?p2 rdfs:label ?p2Label .
                    }}
                    OPTIONAL {{
                        ?o2 rdfs:label ?o2Label .
                    }}
                }}
            }}
        """
        )

        # group objects with the same predicate
        # (& bnodes with the same object)
        props_dict = {}
        for result in r.bindings:
            bnode = None
            if result.get("o2"):
                bnode = {
                    "uri": result["p2"],
                    "prefix": self._get_prefix(result["p2"]),
                    "label": result.get("p2Label"),
                    "value": result["o2"],
                    "oPrefix": self._get_prefix(result["o2"]),
                    "oLabel": result.get("o2Label"),
                }
            if props_dict.get(result["p"]):  # pred exists
                if bnode is not None:
                    obj = None
                    for o in props_dict[result["p"]]["objects"]:
                        if o["value"] == result["o"]:
                            obj = o
                    if obj is not None:  # obj exists
                        obj["bnodes"].append(bnode)
                    else:  # obj doesn't exist
                        obj = {
                            "value": result["o"],
                            "prefix": self._get_prefix(result["o"]),
                            "label": result.get("oLabel"),
                            "bnodes": [bnode],
                        }
                        props_dict[result["p"]]["objects"].append(obj)
                else:
                    obj = {
                        "value": result["o"],
                        "prefix": self._get_prefix(result["o"]),
                        "label": result.get("oLabel"),
                    }
                    props_dict[result["p"]]["objects"].append(obj)
            else:  # pred doesn't exists
                if bnode is not None:
                    obj = {
                        "value": result["o"],
                        "prefix": self._get_prefix(result["o"]),
                        "label": result.get("oLabel"),
                        "bnodes": [bnode],
                    }
                else:
                    obj = {
                        "value": result["o"],
                        "prefix": self._get_prefix(result["o"]),
                        "label": result.get("oLabel"),
                    }

                props_dict[result["p"]] = {
                    "uri": result["p"],
                    "prefix": self._get_prefix(result["p"]),
                    "label": result.get("pLabel"),
                    "objects": [obj],
                }
        return props_dict

    # override
    def _get_properties(self) -> List[Dict]:
        props_dict = self._get_props_dict()

        # group props in order, filtering out hidden props
        properties = []
        main_props = []
        geom_props = []
        other_props = []

        for uri, prop in props_dict.items():
            if uri in SpacePrezFeature.hidden_props:
                continue
            elif uri in SpacePrezFeature.main_props:
                main_props.append(prop)
            elif uri in SpacePrezFeature.geom_props:
                geom_props.append(prop)
                for bnode in prop["objects"][0]["bnodes"]:
                    bnode_prop_name = bnode["uri"].split("#")[1]
                    if bnode_prop_name in ["asDGGS", "asGeoJSON", "asWKT"]:
                        self.geometries[bnode_prop_name] = bnode["value"]
            else:
                other_props.append(prop)

        properties.extend(
            sorted(
                main_props,
                key=lambda p: self._sort_within_list(p, SpacePrezFeature.main_props),
            )
        )
        properties.extend(
            sorted(
                geom_props,
                key=lambda p: self._sort_within_list(p, SpacePrezFeature.geom_props),
            )
        )
        properties.extend(other_props)

        return properties
