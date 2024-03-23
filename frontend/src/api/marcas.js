import axios from "axios";

export default class MarcasApi {
    async getMarcas() {
        const { data } = await axios.get("/marcas/");
        return data.results;
    }
    async addMarca(marca) {
        const { data } = await axios.post("/marcas/", marca);
        return data.results;
    }
    async updateMarca(marca) {
        const { data } = await axios.put(`/marcas/${marca.id}/`, marca);
        return data.results;
    }
    async deleteMarca(id) {
        const { data } = await axios.delete(`/marcas/${id}/`);
        return data.results;
    }
    async getMarca(id) {
        const { data } = await axios.get(`/marcas/${id}/`);
        return data;
    }
}