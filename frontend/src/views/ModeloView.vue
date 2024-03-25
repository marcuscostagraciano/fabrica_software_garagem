<script setup>
import { ref, reactive, onMounted } from "vue";

import TableHeaderList from "../components/TableHeaderList.vue";

import CategoriasApi from "@/api/categorias"
import MarcasApi from "@/api/marcas"
import ModelosApi from "@/api/modelos";

const categoriasApi = new CategoriasApi();
const marcasApi = new MarcasApi();
const modelosApi = new ModelosApi();

const categorias = ref([])
const marcas = ref([])

const defaultModelo = { id: null, nome: "", categoria: null, marca: null };
const modelos = ref([]);
const modelo = reactive({ ...defaultModelo });

const isEditando = ref(false)

onMounted(async () => {
    modelos.value = await modelosApi.getAll();

    categorias.value = await categoriasApi.getAll();

    marcas.value = await marcasApi.getAll();
});

function limpar() {
    isEditando.value = false
    Object.assign(modelo, { ...defaultModelo });
}

async function salvar() {
    if (modelo.id) {
        await modelosApi.update(modelo);
    } else {
        await modelosApi.add(modelo);
    }
    modelos.value = await modelosApi.getAll();
    limpar();
}

function editar(modelo_para_editar) {
    isEditando.value = true
    Object.assign(modelo, modelo_para_editar);
}

async function excluir(id) {
    await modelosApi.delete(id);
    modelos.value = await modelosApi.getAll();
    limpar();
}

const theader_text = [
    "Nome", "Categoria",
    "Marca"
]

</script>

<template>
    <h1 class="my-3">Modelos</h1>
    <v-form class="mx-6">
        <v-text-field v-model="modelo.nome" name="nome" label="Nome"></v-text-field>

        <v-select :items="categorias" item-title="descricao" item-value="id" v-model="modelo.categoria"
            label="Categoria"></v-select>
        <v-select :items="marcas" item-title="nome" item-value="id" v-model="modelo.marca" label="Marca"></v-select>

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
            <tr v-for="modelo in modelos" :key="modelo.name" @click="editar(modelo)">
                <td>{{ modelo.id }}</td>
                <td>{{ modelo.nome }}</td>
                <td>{{ categorias.filter((item) => item.id == modelo.categoria)[0].descricao }}</td>
                <td>{{ marcas.filter((item) => item.id == modelo.marca)[0].nome }}</td>

                <!-- Que sirvam de cicatrizes -->
                <!-- <td>{{ lista_categorias[modelo.categoria - 1]["descricao"] }}</td> -->
                <!-- <td>{{ lista_marcas[modelo.marca - 1]["nome"] }}</td> -->
                <!-- <td>{{ modelo.categoria }}</td> -->
                <!-- <td>{{ categorias.filter((categoria) => categoria['id'] == modelo.categoria)[0]["descricao"] }}</td> -->
                <!-- <td>{{ getDescCategoria(modelo.categoria)["descricao"] }}</td> -->
                <!-- <td>{{ getDescMarca(modelo.marca)["nome"] }}</td> -->
                <!-- <td>{{ modelo.marca }}</td> -->
                <td><button @click="excluir(modelo.id)" class="excluir">X</button></td>
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