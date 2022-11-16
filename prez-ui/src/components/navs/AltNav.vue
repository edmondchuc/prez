<script setup>
import { ref, watch } from "vue";
import { RouterLink } from "vue-router";
import { DataFactory } from "n3";
import { useRdfStore } from "@/composables/rdfStore";

const { namedNode } = DataFactory;

const mediatypeNames = {
    "text/html": "HTML",
    "application/json": "JSON",
    "application/ld+json": "JSON-LD",
    "text/turtle": "Turtle",
    "application/rdf+xml": "RDF/XML",
    "text/csv": "CSV"
};

const { store, prefixes, parseIntoStore, qname, clearStore } = useRdfStore();

const profiles = ref([]);

const props = defineProps({
    profileData: String,
    currentUrl: String
});

watch(() => props.profileData, (newData, oldData) => {
    // clear profiles
    clearStore();
    profiles.value = [];

    if (!!newData) {
        parseIntoStore(newData);

        store.value.forSubjects(subject => { // for each profile
            let p = {
                uri: subject.id,
                mediatypes: []
            };
            store.value.forEach(q => { // get preds & objs for each subj
                if (q.predicate.value === qname("dcterms:title")) {
                    p.title = q.object.value;
                } else if (q.predicate.value === qname("dcterms:identifier")) {
                    p.id = q.object.value;
                } else if (q.predicate.value === qname("dcterms:description")) {
                    p.description = q.object.value;
                } else if (q.predicate.value === qname("altr-ext:hasDefaultResourceFormat")) {
                    p.defaultMediatype = q.object.value;
                } else if (q.predicate.value === qname("altr-ext:hasResourceFormat")) {
                    p.mediatypes.push(q.object.value);
                }
            }, subject, null, null);
            profiles.value.push(p);
        }, namedNode(qname("a")), namedNode(qname("prof:Profile")));
    }
});
</script>

<template>
    <div>
        <h4>Alternate Profiles</h4>
        <div id="profiles">
            <div v-for="profile in profiles" class="profile">
                <RouterLink :to="`${props.currentUrl}?_profile=${profile.id}`" class="profile-title"><h5>{{ profile.title }}</h5></RouterLink>
                <div class="mediatypes">
                    <RouterLink
                        v-for="mediatype in profile.mediatypes"
                        :to="`${props.currentUrl}?_profile=${profile.id}&_mediatype=${mediatype}`"
                        class="mediatype"
                    >{{ mediatypeNames[mediatype] }}</RouterLink>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/assets/sass/_variables.scss";

h4 {
    font-size: 1.1rem;
}

#profiles {
    display: flex;
    flex-direction: column;
    gap: 12px;

    .profile {
        display: flex;
        flex-direction: column;
        gap: 8px;

        .profile-title {
            h5 {
                font-size: 1rem;
                margin: 0;
            }
        }
        .mediatypes {
            display: flex;
            flex-direction: row;
            gap: 8px;
            flex-wrap: wrap;

            a.mediatype {
                padding: 6px;
                background-color: #55828b;
                color: white;
                border-radius: 4px;
                font-size: 0.8rem;  
            }
        }
    }
}
</style>