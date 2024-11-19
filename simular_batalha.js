document.addEventListener('DOMContentLoaded', function () {
    console.log("Carregando lista de heróis...");

    // Carregar a lista de heróis
    fetch('/herois')
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro ao buscar heróis: ${response.statusText}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Heróis recebidos:", data);
            const heroi1Select = document.getElementById('heroi1');
            const heroi2Select = document.getElementById('heroi2');

            if (!data || data.length === 0) {
                console.warn("Nenhum herói encontrado no servidor.");
                alert("Nenhum herói disponível para carregar.");
                return;
            }

            // Preencher os selects com os heróis recebidos
            data.forEach(heroi => {
                const option1 = document.createElement('option');
                option1.value = heroi.id;
                option1.textContent = heroi.nome_heroi;
                heroi1Select.appendChild(option1);

                const option2 = document.createElement('option');
                option2.value = heroi.id;
                option2.textContent = heroi.nome_heroi;
                heroi2Select.appendChild(option2);
            });
        })
        .catch(error => {
            console.error("Erro ao carregar heróis:", error);
            alert("Erro ao carregar a lista de heróis. Veja o console para mais detalhes.");
        });

    // Enviar o formulário de batalhas
    const formBatalha = document.getElementById('form-simulacao-batalha');
    formBatalha.addEventListener('submit', function (event) {
        event.preventDefault();

        console.log("Enviando dados da batalha...");

        const data = {
            heroi_id_1: parseInt(document.getElementById('heroi1').value),
            heroi_id_2: parseInt(document.getElementById('heroi2').value),
            fatores_aleatorios_1: Array.from(document.querySelectorAll('input[name="fatores_aleatorios_1"]:checked')).map(el => el.value),
            fatores_estrategicos_1: Array.from(document.querySelectorAll('input[name="fatores_estrategicos_1"]:checked')).map(el => el.value),
            fatores_aleatorios_2: Array.from(document.querySelectorAll('input[name="fatores_aleatorios_2"]:checked')).map(el => el.value),
            fatores_estrategicos_2: Array.from(document.querySelectorAll('input[name="fatores_estrategicos_2"]:checked')).map(el => el.value)
        };

        console.log("Dados da batalha:", data);

        fetch('/batalha', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(async response => {
                if (!response.ok) {
                    const errorText = await response.text();
                    console.error('Erro no backend:', errorText);
                    throw new Error(`Erro ${response.status}: ${response.statusText}`);
                }
                return response.json();
            })
            .then(responseData => {
                console.log('Dados da resposta JSON:', responseData);

                if (responseData.error) {
                    throw new Error(responseData.error);
                }

                // Exibir o vencedor
                document.getElementById('mensagem-resultado').innerText = `O vencedor é ${responseData.vencedor}`;
                document.getElementById('resultado-batalha').style.display = 'block';

                // Exibir estatísticas antes e depois da batalha
                const estatisticasAntes = responseData.estatisticas_antes || {};
                const estatisticasDepois = responseData.estatisticas_depois || {};
                const fatores = responseData.fatores || {};

                const estatisticasElemento = document.getElementById('estatisticas-batalha');
                estatisticasElemento.innerHTML = `
                    <h3>Estatísticas da Batalha</h3>
                    <br><hr><br>
                    <div class="estatísticas-antes">
                        <h3>Antes da Batalha:</h3>
                        <br>
                        <p><strong>${estatisticasAntes.heroi_1?.nome || 'Herói 1'}</strong></p>
                        <ul>
                            <li>Força: ${estatisticasAntes.heroi_1?.forca || 'N/A'}</li>
                            <li>Popularidade: ${estatisticasAntes.heroi_1?.popularidade || 'N/A'}</li>
                        </ul>
                        <br>
                        <p><strong>${estatisticasAntes.heroi_2?.nome || 'Herói 2'}</strong></p>
                        <ul>
                            <li>Força: ${estatisticasAntes.heroi_2?.forca || 'N/A'}</li>
                            <li>Popularidade: ${estatisticasAntes.heroi_2?.popularidade || 'N/A'}</li>
                        </ul>
                    </div>
                    <div>
                    <div class="estatistica-depois">
                        <br>
                        <h3>Depois da Batalha:</h3>
                        <br>
                        <p><strong>${estatisticasDepois.heroi_1?.nome || 'Herói 1'}</strong></p>
                        <ul>
                            <li>Força: ${estatisticasDepois.heroi_1?.forca || 'N/A'}</li>
                            <li>Popularidade: ${estatisticasDepois.heroi_1?.popularidade || 'N/A'}</li>
                            <br>
                        </ul>
                        <p><strong>${estatisticasDepois.heroi_2?.nome || 'Herói 2'}</strong></p>
                        <ul>
                            <li>Força: ${estatisticasDepois.heroi_2?.forca || 'N/A'}</li>
                            <li>Popularidade: ${estatisticasDepois.heroi_2?.popularidade || 'N/A'}</li>
                        </ul>
                    </div>
                    <div class="desempenho">
                        <br>
                        <h3>Desempenho</h3>
                    </div>
                `;

                estatisticasElemento.style.display = 'block';

                console.log("Batalha concluída com sucesso.");
            })
            .catch(error => {
                console.error('Erro ao iniciar batalha:', error);
                alert(`Erro ao iniciar batalha: ${error.message}`);
            });
    });
});
