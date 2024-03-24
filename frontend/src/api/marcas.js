import axios from "axios";

export default class MarcasApi {
    async getAll() {
        const { data } = await axios.get("/marcas/");
        return data.results;
    }
    async add(marca) {
        const { data } = await axios.post("/marcas/", marca);
        return data.results;
    }
    async update(marca) {
        const { data } = await axios.put(`/marcas/${marca.id}/`, marca);
        return data.results;
    }
    async delete(id) {
        const { data } = await axios.delete(`/marcas/${id}/`);
        return data.results;
    }
    async get(id) {
        const { data } = await axios.get(`/marcas/${id}/`);
        return data;
    }
}