def test_deve_criar_e_listar_movimentacao(client):
    payload = {
        "descricao": "Teste Automatizado",
        "valor": 100.50,
        "tipo": "entrada",
        "categoria": "Investimento",
        "data_movimentacao": "2026-04-30"
    }
    
    response_post = client.post("/movimentacoes/", json=payload)
    
    assert response_post.status_code == 201
    data = response_post.json()
    assert data["descricao"] == "Teste Automatizado"
    assert "id" in data

    response_get = client.get("/movimentacoes/")
    
    assert response_get.status_code == 200
    assert len(response_get.json()) == 1
    assert response_get.json()[0]["valor"] == 100.50