## NFS-e


- Encaminhar uma doc (word) com prints e passo a passo da análise;
- Se possível, reproduzir o problema;
- XML enviado e retornado pela prefeitura;
- XML de ENTRADA;
- nfse.log;
- dados_ambiente.log;
- DANFSE:

!!! info
      Quando houver solicitação de remoçao ou adicção de informação em DANFSE é necessário analisar o xml de entrada ou enviado a prefeitura.<br>
      Em casos de inclusão em um campo específico, viabilizar juntamente a prefeitura se esta informação é legal e obrigatória.


- Indicar a prefeitura e datalhes no descrição do chamado, exemplo abaixo:

```
Prefeitura: 
Padrão: 
Plugin?:(Sim ou não e o nome do arquivo.plugin) | Versão do plugin
DFe Manager ou Synchro4DFe:

```

!!! info
      Isto serve também para o e-mail de bombeiro, caso também de encaminhamento, realizar todas evidencias ao chamado também.

## Conector DFe Padrão

Todo processo do conector fica maior parte registrado no log all.log.Documentos e suas informações são consumidos pelo conector e colocados nas tabelas de entrada NFE_CONTROLE E NFE_XML, onde são enviados para o Synchro4DFe.Após Synchro4DFe se cominicado com Sefaz/Prefeituras, é disponibilizado o retorno para que o conector recupera nas tabelas de saída NFE_CONTROLE_SAIDA e NFE_XML_SAIDA par que as integrações ou sistemas legados obtém o retorno.

Para analises é necessário seguintes evidências:

- Todos arquivos da pasta /logs do mesmo(all.log, dados_ambiente.log,etc.);
- o arquivo de configuração (config.txt) é crucial para análise e indentificar possivél problema devido configurações;