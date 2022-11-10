import { ref } from "vue";
import { defineStore } from "pinia";

export const useUiStore = defineStore("ui", () => {
    // state
    const rightNavConfig = ref({
        enabled: true,
        profiles: []
    });

    // getters

    // actions
    function updateRightNavConfig(config) {
        rightNavConfig.value = config;
    }

    return {
        // state
        rightNavConfig,

        // getters

        // actions
        updateRightNavConfig,
    }
});
