<script setup>
import AltNav from "@/components/navs/AltNav.vue";

const props = defineProps({
    profileData: String,
    currentUrl: String
});
</script>

<template>
    <div id="right-nav">
        <Transition name="fade">
            <AltNav v-show="!!props.profileData" :profileData="props.profileData" :currentUrl="props.currentUrl" />
        </Transition>
        <div>some other stuff</div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/assets/sass/_transitions.scss";

#right-nav {
    min-width: 260px;
    display: flex;
    flex-direction: column;
    padding: 16px;
}
</style>