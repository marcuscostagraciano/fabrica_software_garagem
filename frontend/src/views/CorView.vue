<script setup>
import { ref, reactive, onMounted } from "vue";

import CoresApi from "@/api/cores";
const coresApi = new CoresApi();

const defaultCor = { id: null, descricao: "" };
const cores = ref([]);
const cor = reactive({ ...defaultCor });
const isEditando = ref(false)

onMounted(async () => {
    cores.value = await coresApi.getAll();
});

function limpar() {
    isEditando.value = false
    Object.assign(cor, { ...defaultCor });
}

async function salvar() {
    if (cor.id) {
        await coresApi.update(cor);
    } else {
        await coresApi.add(cor);
    }
    cores.value = await coresApi.getAll();
    limpar();
}

function editar(cor_para_editar) {
    isEditando.value = true
    Object.assign(cor, cor_para_editar);
}

async function excluir(id) {
    await coresApi.delete(id);
    cores.value = await coresApi.getAll();
    limpar();
}

</script>

<template>
    <h1 class="my-3">Cores</h1>
    <v-form class="mx-6">
        <v-text-field v-model="cor.descricao" name="descricao" label="Descrição"></v-text-field>

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
        <thead>
            <tr>
                <th>
                    Código
                </th>
                <th>
                    Descrição
                </th>
                <th>
                    Excluir
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="cor in cores" :key="cor.name" @click="editar(cor)">
                <td>{{ cor.id }}</td>
                <td>{{ cor.descricao }}</td>
                <td><button @click="excluir(cor.id)" class="excluir">X</button></td>
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