import axios from "axios";

export default class AcessoriosApi {
    async getAll() {
        const { data } = await axios.get("/acessorios/");
        return data.results;
    }
    async add(acessorio) {
        const { data } = await axios.post("/acessorios/", acessorio);
        return data.results;
    }
    async update(acessorio) {
        const { data } = await axios.put(`/acessorios/${acessorio.id}/`, acessorio);
        return data.results;
    }
    async delete(id) {
        const { data } = await axios.delete(`/acessorios/${id}/`);
        return data.results;
    }
    async get(id) {
        const { data } = await axios.get(`/acessorios/${id}/`);
        return data;
    }
}