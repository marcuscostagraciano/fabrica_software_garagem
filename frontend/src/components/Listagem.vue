<script setup>
import { ref, reactive } from 'vue';

const props = defineProps(['api', 'default_format', 'list'])

const api = ref(props.api)
const default_fmt = ref(props.default_format)

const item = reactive({ ...default_fmt });

function limpar() {
    Object.assign(item, { ...default_fmt });
}

function editar(item_para_editar) {
    Object.assign(item, item_para_editar);
}

async function excluir(id) {
    await api.delete(id);
    items.value = await api.getAll();
    limpar();
}

</script>

<template>
    <ul>
        <li v-for="item_from_list in props.list" :key="item_from_list.id">
            <span @click="editar(item_from_list)">
                ({{ item_from_list.id }}) - {{ item_from_list.descricao }} -
            </span>
            <button @click="excluir(item_from_list.id)">X</button>
        </li>
    </ul>
</template>

<style scoped></style>