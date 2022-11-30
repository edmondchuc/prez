<script setup>
import { RouterLink } from "vue-router";
import { useUiStore } from "@/stores/ui";

const ui = useUiStore();
</script>

<template>
    <div id="breadcrumbs">
        <RouterLink to="/" class="breadcrumb">Home</RouterLink>
        <RouterLink v-for="breadcrumb in ui.breadcrumbs" :to="breadcrumb.url" class="breadcrumb">{{ breadcrumb.name }}</RouterLink>
    </div>
</template>

<style lang="scss" scoped>
@import "@/assets/sass/_variables.scss";

#breadcrumbs {
    display: flex;
    flex-direction: row;
    gap: 12px;

    a.breadcrumb {
        font-size: 0.8em;
        color: $headerColor;

        &:not(:last-child)::after {
            content: ">";
        }
    }
}
</style>