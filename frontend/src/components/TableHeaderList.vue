<script setup>
const props = defineProps(["th_text"])
</script>

<template>
    <thead>
        <tr>
            <th>
                Código
            </th>
            <th v-if="props.th_text" v-for="text in props.th_text">
                {{ text }}
            </th>
            <th v-else>
                Descrição
            </th>
            <th>
                Excluir
            </th>
        </tr>
    </thead>
</template>

<style scoped></style>