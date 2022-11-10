<script setup>
import { onMounted } from "vue";
import { useUiStore } from "@/stores/ui";

const ui = useUiStore();

onMounted(() => {
    ui.updateRightNavConfig({enabled: true, profiles: ["1", "2", "3"]});
});
</script>

<template>
    <h1>SpacePrez Home</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis in libero qui earum rem facilis optio culpa nobis magnam commodi. Sunt aspernatur obcaecati eos expedita aperiam magnam ipsum incidunt impedit?</p>
</template>

<style lang="scss" scoped>

</style>