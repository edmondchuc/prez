<script setup>
import { RouterLink } from "vue-router";

const props = defineProps({
    profiles: Array
});
</script>

<template>
    <div>
        <h4>Alternate Profiles</h4>
        <div id="profiles">
            <RouterLink v-for="profile in props.profiles" to="">Profile {{ profile }}</RouterLink>
        </div>
    </div>
</template>

<style lang="scss" scoped>
#profiles {
    display: flex;
    flex-direction: column;
    gap: 8px;
}
</style>