import axios from "axios";

export default class ModelosApi {
    async getAll() {
        const { data } = await axios.get("/modelos/");
        return data.results;
    }
    async add(modelo) {
        const { data } = await axios.post("/modelos/", modelo);
        return data.results;
    }
    async update(modelo) {
        const { data } = await axios.put(`/modelos/${modelo.id}/`, modelo);
        return data.results;
    }
    async delete(id) {
        const { data } = await axios.delete(`/modelos/${id}/`);
        return data.results;
    }
    async get(id) {
        const { data } = await axios.get(`/modelos/${id}/`);
        return data;
    }
}