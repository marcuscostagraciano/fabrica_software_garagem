<script setup>
import { ref, reactive, onMounted } from "vue";
import AcessoriosApi from "@/api/acessorios";
const acessoriosApi = new AcessoriosApi();

const defaultAcessorio = { id: null, descricao: "" };
const acessorios = ref([]);
const acessorio = reactive({ ...defaultAcessorio });

onMounted(async () => {
    acessorios.value = await acessoriosApi.getAcessorios();
});

function limpar() {
    Object.assign(acessorio, { ...defaultAcessorio });
}

async function salvar() {
    if (acessorio.id) {
        await acessoriosApi.updateAcessorio(acessorio);
    } else {
        await acessoriosApi.addAcessorio(acessorio);
    }
    acessorios.value = await acessoriosApi.getAcessorios();
    limpar();
}

function editar(acessorio_para_editar) {
    Object.assign(acessorio, acessorio_para_editar);
}

async function excluir(id) {
    await acessoriosApi.deleteAcessorio(id);
    acessorios.value = await acessoriosApi.getAcessorios();
    limpar();
}

</script>

<template>
    <h1 class="my-3">Acessórios</h1>
    <v-form class="mx-6">
        <v-text-field v-model="acessorio.descricao" name="descricao" label="Descrição"></v-text-field>

        <v-container class="d-flex justify-center">
            <v-btn @click="salvar" class="bg-surface-variant">Adicionar</v-btn>
            <v-btn @click="limpar" class="bg-surface-variant">Limpar</v-btn>
        </v-container>
    </v-form>
    <hr />

    <ul>
        <li v-for="acessorio in acessorios" :key="acessorio.id">
            <span @click="editar(acessorio)">
                ({{ acessorio.id }}) - {{ acessorio.descricao }} -
            </span>
            <button @click="excluir(acessorio.id)">X</button>
        </li>
    </ul>
</template>

<style></style>