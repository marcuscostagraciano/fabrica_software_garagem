import axios from "axios";

export default class CategoriasApi {
    async getAll() {
        const { data } = await axios.get("/categorias/");
        return data.results;
    }
    async add(categoria) {
        const { data } = await axios.post("/categorias/", categoria);
        return data.results;
    }
    async update(categoria) {
        const { data } = await axios.put(`/categorias/${categoria.id}/`, categoria);
        return data.results;
    }
    async delete(id) {
        const { data } = await axios.delete(`/categorias/${id}/`);
        return data.results;
    }
    async get(id) {
        const { data } = await axios.get(`/categorias/${id}/`);
        return data;
    }
}