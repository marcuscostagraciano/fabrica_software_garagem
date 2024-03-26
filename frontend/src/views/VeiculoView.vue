<script setup>
import { ref, reactive, onMounted } from "vue";

import TableHeaderList from "../components/TableHeaderList.vue";

import CoresApi from "@/api/cores"
import ModelosApi from "@/api/modelos"
import VeiculosApi from "@/api/veiculos";

const coresApi = new CoresApi();
const modelosApi = new ModelosApi();
const veiculosApi = new VeiculosApi();

const defaultVeiculo = {
    id: null, cor: null, modelo: null,
    ano: null, descricao: "", preco: null
};

const cores = ref([]);
const modelos = ref([]);
const veiculos = ref([]);

const veiculo = reactive({ ...defaultVeiculo });
const isEditando = ref(false)

onMounted(async () => {
    cores.value = await coresApi.getAll();
    modelos.value = await modelosApi.getAll();
    veiculos.value = await veiculosApi.getAll();
});

function limpar() {
    isEditando.value = false
    Object.assign(veiculo, { ...defaultVeiculo });
}

async function salvar() {
    if (veiculo.id) {
        await veiculosApi.update(veiculo);
    } else {
        await veiculosApi.add(veiculo);
    }
    veiculos.value = await veiculosApi.getAll();
    limpar();
}

function editar(veiculo_para_editar) {
    isEditando.value = true
    Object.assign(veiculo, veiculo_para_editar);
}

async function excluir(id) {
    await veiculosApi.delete(id);
    veiculos.value = await veiculosApi.getAll();
    limpar();
}

const theader_text = [
    "Cor", "Modelo", "Ano",
    "Descrição", "Preço"
]

</script>

<template>
    <h1 class="my-3">Veículos</h1>
    <v-form class="mx-6">
        <!-- <v-text-field v-model="veiculo.cor" name="cor" label="Cor"></v-text-field> -->
        <v-select :items="cores" item-title="descricao" item-value="id" v-model="veiculo.cor" label="Cor"></v-select>
        <!-- <v-text-field v-model="veiculo.modelo" name="modelo" label="Modelo"></v-text-field> -->
        <v-select :items="modelos" item-title="nome" item-value="id" v-model="veiculo.modelo" label="Modelo"></v-select>
        <v-text-field v-model="veiculo.ano" name="ano" label="Ano" type="number"></v-text-field>
        <v-text-field v-model="veiculo.descricao" name="descricao" label="Descrição"></v-text-field>
        <v-text-field v-model="veiculo.preco" name="preco" label="Preço"></v-text-field>

        <v-container class="d-flex justify-center">
            <v-btn @click="salvar" class="bg-surface-variant">
                <!-- <v-btn @click="console.log('SAVED')" class="bg-surface-variant"> -->
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
            <tr v-for="veiculo in veiculos" :key="veiculo.name" @click="editar(veiculo)">
                <td>{{ veiculo.id }}</td>
                <td>{{ veiculo.cor }}</td>
                <!-- <td>{{ cores.filter((item) => item.id == veiculo.modelo)[0].descricao }}</td> -->
                <!-- <td>{{ veiculo.modelo }}</td> -->
                <td>{{ modelos.filter((item) => item.id == veiculo.modelo)[0].nome }}</td>
                <td>{{ veiculo.ano }}</td>
                <td>{{ veiculo.descricao }}</td>
                <td>{{ veiculo.preco }}</td>
                <td><button @click="excluir(veiculo.id)" class="excluir">X</button></td>
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