<script setup>
import AltNav from "@/components/navs/AltNav.vue";

const props = defineProps({
    profiles: Array
});
</script>

<template>
    <div id="right-nav">
        <AltNav v-if="props.profiles.length > 0" :profiles="props.profiles" />
        <div>some other stuff</div>
    </div>
</template>

<style lang="scss" scoped>
#right-nav {
    min-width: 260px;
    display: flex;
    flex-direction: column;
    padding: 16px;
}
</style>