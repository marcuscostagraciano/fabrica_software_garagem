import axios from "axios";

export default class CoresApi {
    async getCores() {
        const { data } = await axios.get("/cores/");
        return data.results;
    }
    async addCor(cor) {
        const { data } = await axios.post("/cores/", cor);
        return data.results;
    }
    async updateCor(cor) {
        const { data } = await axios.put(`/cores/${cor.id}/`, cor);
        return data.results;
    }
    async deleteCor(id) {
        const { data } = await axios.delete(`/cores/${id}/`);
        return data.results;
    }
    async getCor(id) {
        const { data } = await axios.get(`/cores/${id}/`);
        return data;
    }
}