<script setup>
import { onMounted, ref } from "vue";
import { RouterLink, useRoute } from "vue-router";
import { DataFactory } from "n3";
import { useUiStore } from "@/stores/ui";
import { useRdfStore } from "@/composables/rdfStore";

const { namedNode } = DataFactory;

// function sleep(ms) {
//     return new Promise(resolve => setTimeout(resolve, ms));
// }

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

<https://w3id.org/profile/dd>
    a prof:Profile ;
    dcterms:description "A simple data model to provide items for form drop-down lists. The basic information is an ID & name tuple and the optional extra value is an item's parent. For vocabularies, this is then URI, prefLabel or URI, prefLabel & broader Concept" ;
    dcterms:identifier "dd" ;
    dcterms:title "Drop-Down List" ;
    altr-ext:hasDefaultResourceFormat "application/json" ;
    altr-ext:hasResourceFormat
        "application/json" ,
        "text/csv"
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

<https://example.com/vocab1> a skos:ConceptScheme ;
    skos:prefLabel "Vocab 1"@en ;
    dcterms:identifier "vocab1"^^xsd:token ;
.
<https://example.com/vocab2> a skos:ConceptScheme ;
    skos:prefLabel "Vocab 2"@en ;
    dcterms:identifier "vocab2"^^xsd:token ;
    dcterms:description """some desc""" ;
.
<https://example.com/vocab3> a skos:ConceptScheme ;
    skos:prefLabel "Vocab 3"@en ;
    dcterms:identifier "vocab3"^^xsd:token ;
    dcterms:description """some desc""" ;
.`;

const route = useRoute();
const ui = useUiStore();
const { store, prefixes, parseIntoStore, qname } = useRdfStore();

const vocabs = ref([]);

onMounted(() => {
    // API request

    // RDF parsing
    parseIntoStore(turtleData);

    // RDF querying
    store.value.forSubjects(subject => { // for each concept scheme
        let v = {
            iri: subject.id
        };
        store.value.forEach(q => { // get preds & objs for each subj
            // console.log("quad", q);
            // console.log("s", q.subject.value);
            // console.log("p", q.predicate.value);
            // console.log("o", q.object.value);
            // console.log("o lang", q.object.language);
            // console.log("p", q.predicate.toJSON());
            // console.log("o", q.object.toJSON());
            if (q.predicate.value === qname("skos:prefLabel")) {
                v.title = q.object.value;
            } else if (q.predicate.value === qname("dcterms:identifier")) {
                v.id = q.object.value;
            } else if (q.predicate.value === qname("dcterms:description")) {
                v.description = q.object.value;
            }
        }, subject, null, null);
        vocabs.value.push(v);
    }, namedNode(qname("a")), namedNode(qname("skos:ConceptScheme")));

    // update alt profiles nav
    ui.updateRightNavConfig({enabled: true, profileData: profileData, currentUrl: route.path});
});
</script>

<template>
    <h1>Vocabs</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis in libero qui earum rem facilis optio culpa nobis magnam commodi. Sunt aspernatur obcaecati eos expedita aperiam magnam ipsum incidunt impedit?</p>
    <div class="list">
        <RouterLink class="list-item" v-for="vocab in vocabs" :to="`/vocprez/vocab/${vocab.id}`">
            <h4 class="list-item-title">{{ vocab.title }}</h4>
            <div v-if="!!vocab.description" class="list-item-desc">{{ vocab.description }}</div>
        </RouterLink>
    </div>
</template>

<style lang="scss" scoped>
@import "@/assets/sass/_variables.scss";

.list {
    display: flex;
    flex-direction: column;
    gap: 12px;

    a.list-item {
        display: flex;
        flex-direction: column;
        gap: 6px;
        background-color: $cardBg;
        padding: 10px;

        .list-item-title {
            margin: 0;
        }

        .list-item-desc {
            font-style: italic;
            color: grey;
            font-size: 0.8rem;
        }
    }
}
</style>