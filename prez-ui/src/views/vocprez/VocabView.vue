<script setup>
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { DataFactory } from "n3";
import { useUiStore } from "@/stores/ui";
import { useRdfStore } from "@/composables/rdfStore";
import PropTable from "@/components/PropTable.vue";

const { namedNode } = DataFactory;

// function sleep(ms) {
//     return new Promise(resolve => setTimeout(resolve, ms));
// }

const today = new Date().toISOString().slice(0, 10);

const route = useRoute();
const ui = useUiStore();
const { store, prefixes, parseIntoStore, qname } = useRdfStore();

const profileData = `PREFIX altr-ext: <http://www.w3.org/ns/dx/conneg/altr-ext#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX prof: <http://www.w3.org/ns/dx/prof/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

<https://w3id.org/profile/vocpub>
    a prof:Profile ;
    dcterms:description "This is a profile of the taxonomy data model SKOS - i.e. SKOS with additional constraints." ;
    dcterms:identifier "vocpub" ;
    dcterms:title "VocPub" ;
    altr-ext:hasDefaultResourceFormat "text/html" ;
    altr-ext:hasResourceFormat
        "application/ld+json" ,
        "application/rdf+xml" ,
        "text/html" ,
        "text/turtle" ;
.

<https://www.w3.org/TR/vocab-dcat/>
    a prof:Profile ;
    dcterms:description "Dataset Catalog Vocabulary (DCAT) is a W3C-authored RDF vocabulary designed to facilitate interoperability between data catalogs" ;
    dcterms:identifier "dcat" ;
    dcterms:title "DCAT" ;
    altr-ext:hasDefaultResourceFormat "text/html" ;
    altr-ext:hasResourceFormat
        "application/ld+json" ,
        "application/rdf+xml" ,
        "text/html" ,
        "text/turtle" ;
.

altr-ext:alt-profile
    a prof:Profile ;
    dcterms:description "The representation of the resource that lists all other representations (profiles and Media Types)" ;
    dcterms:identifier "alt" ;
    dcterms:title "Alternates Profile" ;
    altr-ext:hasDefaultResourceFormat "text/html" ;
    altr-ext:hasResourceFormat
        "application/ld+json" ,
        "application/rdf+xml" ,
        "text/html" ,
        "text/turtle" ;
.`;

const turtleData = `PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

<https://example.com/${route.params.vocabId}> a skos:ConceptScheme ;
    skos:prefLabel "Vocab ${route.params.vocabId}"@en ;
    dcterms:identifier "vocab${route.params.vocabId}"^^xsd:token ;
    dcterms:description """some desc""" ;
    dcterms:created "${today}"^^xsd:date ;
    dcterms:modified "${today}"^^xsd:date ;
    dcterms:source "https://example.com/some_source"^^xsd:anyURI ;
    dcterms:creator <https://example.com/creator> ;
    dcterms:publisher <https://example.com/publisher> ;
    skos:hasTopConcept
        <https://example.com/concept1> ,
        <https://example.com/concept2> ,
        <https://example.com/concept3> ;
.`;

const conceptData = `PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

<https://example.com/concept1>
    a skos:Concept ;
    dcterms:identifier "concept1"^^xsd:token ;
    skos:narrower <https://example.com/concept1_1> ;
    skos:prefLabel "Concept 1"@en ;
.

<https://example.com/concept2>
    a skos:Concept ;
    dcterms:identifier "concept2"^^xsd:token ;
    skos:prefLabel "Concept 2"@en ;
.

<https://example.com/concept3>
    a skos:Concept ;
    dcterms:identifier "concept3"^^xsd:token ;
    skos:prefLabel "Concept 3"@en ;
.

<https://example.com/concept1_1>
    a skos:Concept ;
    dcterms:identifier "concept1_1"^^xsd:token ;
    skos:prefLabel "Concept 1.1"@en ;
    skos:broader <https://example.com/concept1> ;
.`;

const hiddenPreds = [
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
    "http://www.w3.org/2004/02/skos/core#hasTopConcept",
    "http://purl.org/dc/terms/identifier",
];

const properties = ref([]);
const vocab = ref({});
const concepts = ref([]);
const conceptCollapse = ref(true);
const haveConcepts = ref(false); // flag for whether the get concept request has been done

onMounted(() => {
    // API request

    // RDF parsing
    parseIntoStore(turtleData);
    
    // RDF querying
    const subject = store.value.getSubjects(namedNode(qname("a")), namedNode(qname("skos:ConceptScheme")))[0];
    vocab.value.iri = subject.id;
        store.value.forEach(q => { // get preds & objs
            if (q.predicate.value === qname("skos:prefLabel")) {
                vocab.value.title = q.object.value;
            } else if (q.predicate.value === qname("dcterms:description")) {
                vocab.value.description = q.object.value;
            }
            properties.value.push(q);
        }, subject, null, null);

    // update alt profiles nav
    ui.updateRightNavConfig({enabled: true, profileData: profileData, currentUrl: route.path});
});

function getConcepts() {
    // API request

    // RDF parsing
    parseIntoStore(conceptData);
    
    // RDF querying
    store.value.forSubjects(subject => { // for each concept
        let c = {
            iri: subject.id
        };
        store.value.forEach(q => { // get preds & objs for each subj
            if (q.predicate.value === qname("skos:prefLabel")) {
                c.title = q.object.value;
            } else if (q.predicate.value === qname("dcterms:identifier")) {
                c.id = q.object.value;
            }
        }, subject, null, null);
        concepts.value.push(c);
    }, namedNode(qname("a")), namedNode(qname("skos:Concept")));

    haveConcepts.value = true;
}
</script>

<template>
    <h1>{{ vocab.title }}</h1>
    <p>Instance IRI: <a :href="vocab.iri" target="_blank" rel="noopener noreferrer">{{ vocab.iri }}</a></p>
    <p>{{ vocab.description }}</p>
    <PropTable v-if="properties.length > 0" :properties="properties" :prefixes="prefixes" :hiddenPreds="hiddenPreds">
        <template #bottom>
            <tr>
                <th>Concepts</th>
                <td>
                    <button id="concept-collapse-btn" class="btn" @click="!haveConcepts && getConcepts(); conceptCollapse = !conceptCollapse">
                        <template v-if="conceptCollapse">Expand <i class="fa-regular fa-chevron-down"></i></template>
                        <template v-else>Collapse <i class="fa-regular fa-chevron-up"></i></template>
                    </button>
                    <div :class="`concepts ${conceptCollapse ? 'collapse' : ''}`">
                        <RouterLink v-for="concept in concepts" class="concept" :to="`${route.path}/${concept.id}`">{{ concept.title }}</RouterLink>
                    </div>
                </td>
            </tr>
        </template>
    </PropTable>
</template>

<style lang="scss" scoped>

button#concept-collapse-btn {
    margin-bottom: 12px;
}

.concepts {
    display: flex;
    flex-direction: column;
    gap: 8px;
    overflow: hidden;

    &.collapse {
        height: 0;
    }
}
</style>