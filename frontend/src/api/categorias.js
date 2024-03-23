import axios from "axios";

export default class CategoriasApi {
    async getCategorias() {
        const { data } = await axios.get("/categorias/");
        return data.results;
    }
    async addCategorias(categoria) {
        const { data } = await axios.post("/categorias/", categoria);
        return data.results;
    }
    async updateCategoria(categoria) {
        const { data } = await axios.put(`/categorias/${categoria.id}/`, categoria);
        return data.results;
    }
    async deleteCategoria(id) {
        const { data } = await axios.delete(`/categorias/${id}/`);
        return data.results;
    }
    async getCategoria(id) {
        const { data } = await axios.get(`/categorias/${id}/`);
        return data;
    }
}