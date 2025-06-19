

``` mermaid
graph LR
  A[Chamado] --> B{Bug/Impossibilidade de atendimento?};
  B -->|Sim| C[Encaminhar para fila ES6 Manutenção];
  C --> D[Atendimento ES6];
```

!!! note
    Caracterizar todos chamdos encaminhados corretamente!

## Evidências DFe Manager

- Encaminhar TODOS os logs do momento do processo do problema;

!!! note
    dfe.log,nfe.log,dados_de_ambiente.log,etc.

- Encaminhar uma doc (word) com prints e passo a passo da análise;
- Se possível, reproduzir o problema;

## Evidências Synchro4DFe

- Encaminhar TODOS os logs do momento do processo do problema;

!!! note
    Os logs são baseados no trace_id de cada erro.Na maioria dos processos os logs são registrados modulo-backend e modulo-bff.Para operações de bugs em tela é o modulo-frontend.

- Encaminhar uma doc (word) com prints e passo a passo da análise;
- Se possível, reproduzir o problema;