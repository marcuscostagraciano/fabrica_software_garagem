<script setup>
import { ref, reactive, onMounted } from "vue";

import TableHeaderList from "../components/TableHeaderList.vue";

import CategoriasApi from "@/api/categorias";
const categoriasApi = new CategoriasApi();

const defaultCategoria = { id: null, descricao: "" };
const categorias = ref([]);
const categoria = reactive({ ...defaultCategoria });
const isEditando = ref(false)

onMounted(async () => {
    categorias.value = await categoriasApi.getAll();
});

function limpar() {
    isEditando.value = false
    Object.assign(categoria, { ...defaultCategoria });
}

async function salvar() {
    if (categoria.id) {
        await categoriasApi.update(categoria);
    } else {
        await categoriasApi.add(categoria);
    }
    categorias.value = await categoriasApi.getAll();
    limpar();
}

function editar(categoria_para_editar) {
    isEditando.value = true
    Object.assign(categoria, categoria_para_editar);
}

async function excluir(id) {
    await categoriasApi.delete(id);
    categorias.value = await categoriasApi.getAll();
    limpar();
}

</script>

<template>
    <h1 class="my-3">Categorias</h1>
    <v-form class="mx-6">
        <v-text-field v-model="categoria.descricao" name="descricao" label="Descrição"></v-text-field>

        <v-container class="d-flex justify-center">
            <v-btn @click="salvar" class="bg-surface-variant">
                <p v-if="!isEditando">Adicionar</p>
                <p v-else>Atualizar</p>
            </v-btn>
            <v-btn @click="limpar" class="bg-surface-variant">Limpar</v-btn>
        </v-container>
    </v-form>
    <hr />

    <v-table density="comfortable">
        <TableHeaderList />
        <tbody>
            <tr v-for="categoria in categorias" :key="categoria.name" @click="editar(categoria)">
                <td>{{ categoria.id }}</td>
                <td>{{ categoria.descricao }}</td>
                <td><button @click="excluir(categoria.id)" class="excluir">X</button></td>
            </tr>
        </tbody>
    </v-table>
</template>

<style>
table {
    text-align: center !important;
}

thead tr th {
    text-align: center !important;
    color: #fff;
    background-color: #a6a29a;
    text-transform: uppercase;
}

.excluir {
    border-radius: 20px;
    height: 50%;
    width: 50%;
    background-color: red;
}
</style>