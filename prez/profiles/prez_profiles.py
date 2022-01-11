from connegp import Profile, RDF_MEDIATYPES


sdo = Profile(
    uri="https://schema.org",
    id="sdo",
    label="schema.org",
    comment="Schema.org is a collaborative, community activity with a mission to create, maintain, and promote schemas "
    "for structured data on the Internet, on web pages, in email messages, and beyond.",
    mediatypes=RDF_MEDIATYPES,
    default_mediatype="text/turtle",
    languages=["en"],
    default_language="en",
)

dd = Profile(
    uri="https://w3id.org/profile/dd",
    id="dd",
    label="Drop-Down List",
    comment="A simple data model to provide items for form drop-down lists. The basic information is an ID & name tuple "
    "and the optional extra value is an item's parent. For vocabularies, this is then URI, prefLabel or URI, "
    "prefLabel & broader Concept",
    mediatypes=["application/json"],
    default_mediatype="application/json",
    languages=["en"],
    default_language="en",
)

dcat = Profile(
    uri="https://www.w3.org/TR/vocab-dcat/",
    id="dcat",
    label="DCAT",
    comment="Dataset Catalogue Vocabulary (DCAT) is a W3C-authored RDF vocabulary designed to "
    "facilitate interoperability between data catalogs "
    "published on the Web.",
    mediatypes=["text/html"] + RDF_MEDIATYPES,
    default_mediatype="text/html",
    languages=["en"],
    default_language="en",
)

mem = Profile(
    uri="https://w3id.org/profile/mem",  # the ConnegP URI for member Data Model
    id="mem",
    label="Members",
    comment="A very basic data model that lists the members of container objects only, i.e. not their other "
    "properties",
    mediatypes=["text/html", "application/json"] + RDF_MEDIATYPES,
    default_mediatype="text/html",
    languages=["en"],
    default_language="en",
)

alt = Profile(
    uri="http://www.w3.org/ns/dx/conneg/altr",  # the ConnegP URI for Alt Rep Data Model
    id="alt",
    label="Alternate Representations",
    comment="The representation of the resource that lists all other representations (profiles and Media Types)",
    mediatypes=["text/html", "application/json"] + RDF_MEDIATYPES,
    default_mediatype="text/html",
    languages=["en"],
    default_language="en",
)

profiles = Profile(
    uri="http://example.com/profile/profiles",
    id="profiles",
    label="Profiles",
    comment="List of profiles",
    mediatypes=["text/html", "application/json"],
    default_mediatype="text/html",
    languages=["en"],
    default_language="en",
)
