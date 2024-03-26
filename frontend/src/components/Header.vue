<script setup>
import { onBeforeMount, ref } from 'vue';
import { routes } from '../router'

const windowWidth = ref(0)
const isMobile = ref(false)
const mobileNav = ref(false)

function checkScreenWidth() {
    windowWidth.value = window.innerWidth
    if (windowWidth.value < 1130) {
        isMobile.value = true
    }
    else {
        isMobile.value = false
        mobileNav.value = false
    }
}

onBeforeMount(() => {
    window.addEventListener("resize", checkScreenWidth)
    checkScreenWidth()
})
</script>

<template>
    <v-app-bar density="comfortable">
        <v-col cols="5">
            Garagem app
        </v-col>

        <v-col>
            <v-btn v-show="!isMobile" v-for="route in routes" class="px-2 py-0">
                <router-link :to="route.path">{{ route.name }}</router-link>
            </v-btn>
        </v-col>

        <v-col v-show="isMobile" class="text-right" id="mobile-navbar">
            <v-menu location="bottom">
                <template v-slot:activator="{ props }">
                    <v-btn color="primary" dark v-bind="props" icon="mdi-menu">
                    </v-btn>
                </template>

                <v-list>
                    <v-list-item v-for="route in routes">
                        <v-list-item-title class="text-button text-center"><router-link :to="route.path">{{ route.name
                                }}</router-link></v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-col>
    </v-app-bar>
</template>

<style scoped>
.v-col {
    text-align: center;
}

a {
    text-decoration: none;
}
</style>