import axios from "axios";

export default class VeiculosApi {
    async getAll() {
        const { data } = await axios.get("/veiculos/");
        return data.results;
    }
    async add(veiculo) {
        const { data } = await axios.post("/veiculos/", veiculo);
        return data.results;
    }
    async update(veiculo) {
        const { data } = await axios.put(`/veiculos/${veiculo.id}/`, veiculo);
        return data.results;
    }
    async delete(id) {
        const { data } = await axios.delete(`/veiculos/${id}/`);
        return data.results;
    }
    async get(id) {
        const { data } = await axios.get(`/veiculos/${id}/`);
        return data;
    }
}