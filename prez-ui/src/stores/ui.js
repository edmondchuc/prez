import { ref } from "vue";
import { defineStore } from "pinia";

export const useUiStore = defineStore("ui", () => {
    // state
    const rightNavConfig = ref({
        enabled: true,
        profiles: [],
        currentUrl: ""
    });

    const pageTitle = ref("Prez");
    const breadcrumbs = ref([]);

    // getters

    // actions
    function updateRightNavConfig(config) {
        rightNavConfig.value = config;
    }

    function setBreadcrumbs(breadcrumbsList) {
        breadcrumbs.value = breadcrumbsList;
    }

    return {
        // state
        rightNavConfig,
        pageTitle,
        breadcrumbs,

        // getters

        // actions
        updateRightNavConfig,
        setBreadcrumbs,
    }
});
