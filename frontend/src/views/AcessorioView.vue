<script setup>
import { ref, reactive, onMounted } from "vue";

import AcessoriosApi from "@/api/acessorios";
const acessoriosApi = new AcessoriosApi();

const defaultAcessorio = { id: null, descricao: "" };
const acessorios = ref([]);
const acessorio = reactive({ ...defaultAcessorio });
const isEditando = ref(false)

onMounted(async () => {
    acessorios.value = await acessoriosApi.getAll();
});

function limpar() {
    isEditando.value = false
    Object.assign(acessorio, { ...defaultAcessorio });
}

async function salvar() {
    if (acessorio.id) {
        await acessoriosApi.update(acessorio);
    } else {
        await acessoriosApi.add(acessorio);
    }
    acessorios.value = await acessoriosApi.getAll();
    limpar();
}

function editar(acessorio_para_editar) {
    isEditando.value = true
    Object.assign(acessorio, acessorio_para_editar);
}

async function excluir(id) {
    await acessoriosApi.delete(id);
    acessorios.value = await acessoriosApi.getAll();
    limpar();
}

</script>

<template>
    <h1 class="my-3">Acessórios</h1>
    <v-form class="mx-6">
        <v-text-field v-model="acessorio.descricao" name="descricao" label="Descrição"></v-text-field>

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
            <tr v-for="acessorio in acessorios" :key="acessorio.name" @click="editar(acessorio)">
                <td>{{ acessorio.id }}</td>
                <td>{{ acessorio.descricao }}</td>
                <td><button @click="excluir(acessorio.id)" class="excluir">X</button></td>
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