<script setup>
import { inject } from "vue";
import { RouterView } from "vue-router";
import { useUiStore } from "@/stores/ui";
import MainNav from "@/components/navs/MainNav.vue";
import Breadcrumbs from "@/components/Breadcrumbs.vue";
import RightSideBar from "@/components/navs/RightSideBar.vue";

const sidenav = inject("config").sidenav;

const ui = useUiStore();
</script>

<template>
    <header>
        <div id="header-content">
            <div id="header-html">header</div>
            <Breadcrumbs />
        </div>
    </header>
    <main>
        <div id="main-content" :class="`${sidenav ? 'sidenav' : ''}`">
            <MainNav :sidenav="sidenav" />
            <div id="content">
                <div id="content-body">
                    <RouterView />
                </div>
                <RightSideBar v-show="ui.rightNavConfig.enabled" :profiles="ui.rightNavConfig.profiles" />
            </div>
        </div>
    </main>
    <footer>
        <div id="footer-content">
            footer
        </div>
    </footer>
</template>

<style lang="scss">
@import "@/assets/sass/_variables.scss";

body {
    margin: 0;
    height: 100vh;
    font-family: $bodyFont;
}

h1, h2, h3, h4, h5, h6 {
    font-family: $headerFont;
}

a {
    color: $linkColor;
    text-decoration: none;
}

#app {
    display: flex;
    flex-direction: column;
    height: 100%;

    header {
        background-color: $headerBg;
        color: $headerColor;
        display: flex;

        #header-content {
            width: 100%;
            max-width: $pageMaxWidth;
            margin: 0 auto;
        }
    }

    main {
        flex-grow: 1;
        display: flex;
        background-color: $mainBg;

        #main-content {
            width: 100%;
            max-width: $pageMaxWidth;
            margin: 0 auto;
            display: flex;
            flex-direction: column;

            &.sidenav {
                flex-direction: row;
            }

            #content {
                flex-grow: 1;
                display: flex;
                flex-direction: row;

                #content-body {
                    display: flex;
                    flex-direction: column;
                    padding: 16px;
                    flex-grow: 1;
                }
            }
        }
    }

    footer {
        background-color: $footerBg;
        color: $footerColor;

        #footer-content {
            width: 100%;
            max-width: $pageMaxWidth;
            margin: 0 auto;
        }
    }
}
</style>
