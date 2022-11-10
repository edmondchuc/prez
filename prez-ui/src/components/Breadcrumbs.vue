<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
    <div id="breadcrumbs">
        <RouterLink to="/" class="breadcrumb">Home</RouterLink>
    </div>
</template>

<style lang="scss" scoped>
#breadcrumbs {
    display: flex;
    flex-direction: row;
    gap: 12px;

    a.breadcrumb {
        
    }
}
</style>