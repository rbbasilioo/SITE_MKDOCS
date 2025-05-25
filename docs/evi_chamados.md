

``` mermaid
graph LR
  A[Chamado] --> B{Bug/Impossibilidade de atendimento?};
  B -->|Sim| C[Encaminhar para fila ES6 Manutenção];
  C --> D[Atendimento ES6];
```