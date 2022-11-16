import { createRouter, createWebHistory } from "vue-router";
import pinia from "@/stores/pinia";
import { useUiStore } from "@/stores/ui";

const ui = useUiStore(pinia);

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: () => import("@/views/HomeView.vue")
        },
        {
            path: "/vocprez",
            name: "vocprez home",
            component: () => import("@/views/vocprez/VocPrezHomeView.vue")
        },
        {
            path: "/vocprez/about",
            name: "vocprez about",
            component: () => import("@/views/vocprez/VocPrezAboutView.vue")
        },
        {
            path: "/vocprez/profiles",
            name: "vocprez profiles",
            component: () => import("@/views/vocprez/VocPrezProfilesView.vue")
        },
        {
            path: "/vocprez/vocab",
            name: "vocabs",
            component: () => import("@/views/vocprez/VocabsView.vue")
        },
        {
            path: "/vocprez/vocab/:vocabId",
            name: "vocab",
            component: () => import("@/views/vocprez/VocabView.vue")
        },
        {
            path: "/vocprez/vocab/:vocabId/:conceptId",
            name: "concept",
            component: () => import("@/views/vocprez/ConceptView.vue")
        },
        {
            path: "/vocprez/collection",
            name: "collections",
            component: () => import("@/views/vocprez/CollectionsView.vue")
        },
        {
            path: "/vocprez/collection/:collectionId",
            name: "collection",
            component: () => import("@/views/vocprez/CollectionView.vue")
        },
        {
            path: "/spaceprez",
            name: "spaceprez home",
            component: () => import("@/views/spaceprez/SpacePrezHomeView.vue")
        },
        {
            path: "/spaceprez/conformance",
            name: "spaceprez conformance",
            component: () => import("@/views/spaceprez/ConformanceView.vue")
        },
        {
            path: "/spaceprez/about",
            name: "spaceprez about",
            component: () => import("@/views/spaceprez/SpacePrezAboutView.vue")
        },
        {
            path: "/spaceprez/profiles",
            name: "spaceprez profiles",
            component: () => import("@/views/spaceprez/SpacePrezProfilesView.vue")
        },
        {
            path: "/spaceprez/dataset",
            name: "datasets",
            component: () => import("@/views/spaceprez/DatasetsView.vue")
        },
        {
            path: "/spaceprez/dataset/:datasetId",
            name: "dataset",
            component: () => import("@/views/spaceprez/DatasetView.vue")
        },
        {
            path: "/spaceprez/dataset/:datasetId/collections",
            name: "feature collections",
            component: () => import("@/views/spaceprez/FeatureCollectionsView.vue")
        },
        {
            path: "/spaceprez/dataset/:datasetId/collections/:featureCollectionId",
            name: "feature collection",
            component: () => import("@/views/spaceprez/FeatureCollectionView.vue")
        },
        {
            path: "/spaceprez/dataset/:datasetId/collections/:featureCollectionId/items",
            name: "features",
            component: () => import("@/views/spaceprez/FeaturesView.vue")
        },
        {
            path: "/spaceprez/dataset/:datasetId/collections/:featureCollectionId/items/:featureId",
            name: "feature",
            component: () => import("@/views/spaceprez/FeatureView.vue")
        },
        {
            path: "/catprez",
            name: "catprez home",
            component: () => import("@/views/catprez/CatPrezHomeView.vue")
        },
        {
            path: "/catprez/about",
            name: "catprez about",
            component: () => import("@/views/catprez/CatPrezAboutView.vue")
        },
        {
            path: "/catprez/profiles",
            name: "catprez profiles",
            component: () => import("@/views/catprez/CatPrezProfilesView.vue")
        },
        {
            path: "/catprez/catalog",
            name: "catalogs",
            component: () => import("@/views/catprez/CatalogsView.vue")
        },
        {
            path: "/catprez/catalog/:catalogId",
            name: "catalog",
            component: () => import("@/views/catprez/CatalogView.vue")
        },
        {
            path: "/catprez/catalog/:catalogId/:resourceId",
            name: "resource",
            component: () => import("@/views/catprez/ResourceView.vue")
        },
        {
            path: "/sparql",
            name: "sparql",
            component: () => import("@/views/SparqlView.vue")
        },
        {
            path: "/about",
            name: "about",
            component: () => import("@/views/AboutView.vue")
        },
        {
            path: "/search",
            name: "search",
            component: () => import("@/views/SearchView.vue")
        },
        {
            path: "/profiles",
            name: "profiles",
            component: () => import("@/views/ProfilesView.vue")
        },
        {
            path: "/object",
            name: "object",
            component: () => import("@/views/ObjectView.vue")
        },
    ]
});

router.beforeEach(() => {
    ui.updateRightNavConfig({enabled: true, profileData: "", currentUrl: ""});
    return true;
});

export default router;
