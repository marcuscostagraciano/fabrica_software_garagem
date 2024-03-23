import axios from "axios";

export default class ModelosApi {
    async getModelos() {
        const { data } = await axios.get("/modelos/");
        return data.results;
    }
    async addMarca(modelo) {
        const { data } = await axios.post("/modelos/", modelo);
        return data.results;
    }
    async updateMarca(modelo) {
        const { data } = await axios.put(`/modelos/${modelo.id}/`, modelo);
        return data.results;
    }
    async deleteMarca(id) {
        const { data } = await axios.delete(`/modelos/${id}/`);
        return data.results;
    }
    async getMarca(id) {
        const { data } = await axios.get(`/modelos/${id}/`);
        return data;
    }
}