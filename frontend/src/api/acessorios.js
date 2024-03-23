import axios from "axios";

export default class AcessoriosApi {
    async getAcessorios() {
        const { data } = await axios.get("/acessorios/");
        return data.results;
    }
    async addAcessorio(acessorio) {
        const { data } = await axios.post("/acessorios/", acessorio);
        return data.results;
    }
    async updateAcessorio(acessorio) {
        const { data } = await axios.put(`/acessorios/${acessorio.id}/`, acessorio);
        return data.results;
    }
    async deleteAcessorio(id) {
        const { data } = await axios.delete(`/acessorios/${id}/`);
        return data.results;
    }
    async getAcessorio(id) {
        const { data } = await axios.get(`/acessorios/${id}/`);
        return data;
    }
}