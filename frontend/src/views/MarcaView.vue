<script setup>
import { ref, reactive, onMounted } from "vue";

import TableHeaderList from "../components/TableHeaderList.vue";

import MarcasApi from "@/api/marcas";
const marcasApi = new MarcasApi();

const defaultMarca = { id: null, nome: "", nacionalidade: "" };
const marcas = ref([]);
const marca = reactive({ ...defaultMarca });
const isEditando = ref(false)

onMounted(async () => {
    marcas.value = await marcasApi.getAll();
});

function limpar() {
    isEditando.value = false
    Object.assign(marca, { ...defaultMarca });
}

async function salvar() {
    if (marca.id) {
        await marcasApi.update(marca);
    } else {
        await marcasApi.add(marca);
    }
    marcas.value = await marcasApi.getAll();
    limpar();
}

function editar(marca_para_editar) {
    isEditando.value = true
    Object.assign(marca, marca_para_editar);
}

async function excluir(id) {
    await marcasApi.delete(id);
    marcas.value = await marcasApi.getAll();
    limpar();
}

const theader_text = [
    "Nome", "Nacionalidade"
]

</script>

<template>
    <h1 class="my-3">Marcas</h1>
    <v-form class="mx-6">
        <v-text-field v-model="marca.nome" name="nome" label="Nome"></v-text-field>
        <v-text-field v-model="marca.nacionalidade" name="nacionalidade" label="Nacionalidade"></v-text-field>

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
        <TableHeaderList :th_text="theader_text" />
        <tbody>
            <tr v-for="marca in marcas" :key="marca.name" @click="editar(marca)">
                <td>{{ marca.id }}</td>
                <td>{{ marca.nome }}</td>
                <td>{{ marca.nacionalidade }}</td>
                <td><button @click="excluir(marca.id)" class="excluir">X</button></td>
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