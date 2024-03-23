import axios from "axios";

export default class VeiculosApi {
    async getVeiculos() {
        const { data } = await axios.get("/veiculos/");
        return data.results;
    }
    async addVeiculo(veiculo) {
        const { data } = await axios.post("/veiculos/", veiculo);
        return data.results;
    }
    async updateVeiculo(veiculo) {
        const { data } = await axios.put(`/veiculos/${veiculo.id}/`, veiculo);
        return data.results;
    }
    async deleteVeiculo(id) {
        const { data } = await axios.delete(`/veiculos/${id}/`);
        return data.results;
    }
    async getVeiculo(id) {
        const { data } = await axios.get(`/veiculos/${id}/`);
        return data;
    }
}