

``` mermaid
graph LR
  A[Chamado] --> B{Bug/Impossibilidade de atendimento?};
  B -->|Sim| C[Encaminhar para fila ES6 Manutenção];
  C --> D[Atendimento ES6];
```




## Evidências DFe Manager

- Encaminhar TODOS os logs do monneto do processo do problema;
  - dfe.log,nfe.log,dados_de_ambiente.log,etc.

- Encaminhar uma doc (word) com prints e passo a passo da análise;
- Se possével, reproduzir o problema;

## Evidências Synchro4DFe