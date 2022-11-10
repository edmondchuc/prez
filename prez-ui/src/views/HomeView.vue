<script setup>
import { inject, computed } from "vue";
import { RouterLink } from "vue-router";

const enabledPrezs = computed(() => {
    return inject("config").enabledPrezs.sort((a, b) => a.localeCompare(b));
});

const prezDescriptions = {
    "VocPrez": `vp desc`,
    "SpacePrez": `sp desc`,
    "CatPrez": `cp desc`
};
</script>

<template>
    <h1>System Home</h1>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Hic ex at nobis obcaecati? Praesentium tenetur inventore ratione temporibus cumque incidunt quo, recusandae, labore voluptatibus repudiandae iure deserunt maxime similique placeat.</p>
    <div class="prez-card-container">
        <div v-for="prez in enabledPrezs" class="prez-card">
            <RouterLink :to="prez.toLowerCase()"><h4>{{ prez }}</h4></RouterLink>
            <p>{{ prezDescriptions[prez] }}</p>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.prez-card-container {
    display: flex;
    flex-direction: row;
    gap: 20px;

    .prez-card {
        padding: 20px;
        background-color: #d5d5d5;
        flex: 1;
        max-width: 300px;

        h4 {
            margin-top: 0;
        }
    }
}
</style>