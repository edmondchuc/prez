import { ref } from "vue";
import { defineStore } from "pinia";

export const useUiStore = defineStore("ui", () => {
    // state
    const rightNavConfig = ref({
        enabled: true,
        profileData: "",
        currentUrl: ""
    });

    const pageTitle = ref("Prez");

    // getters

    // actions
    function updateRightNavConfig(config) {
        rightNavConfig.value = config;
    }

    return {
        // state
        rightNavConfig,
        pageTitle,

        // getters

        // actions
        updateRightNavConfig,
    }
});
