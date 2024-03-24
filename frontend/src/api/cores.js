import axios from "axios";

export default class CoresApi {
    async getAll() {
        const { data } = await axios.get("/cores/");
        return data.results;
    }
    async add(cor) {
        const { data } = await axios.post("/cores/", cor);
        return data.results;
    }
    async update(cor) {
        const { data } = await axios.put(`/cores/${cor.id}/`, cor);
        return data.results;
    }
    async delete(id) {
        const { data } = await axios.delete(`/cores/${id}/`);
        return data.results;
    }
    async get(id) {
        const { data } = await axios.get(`/cores/${id}/`);
        return data;
    }
}