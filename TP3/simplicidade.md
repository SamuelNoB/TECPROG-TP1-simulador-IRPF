# Simplicidade

## Conceito

É a característica mais importante de um código, nele se observa o design e a facilidade de entendimento do código, deixando-o coerente e consistente, evitando códigos longos e confusos o que facilita futuros programadores de implementarem novas funcionalidades ao projeto caso necessário.

## Implementação

O Grupo percebeu que no arquivo `src/models/Faixa_de_imposto.py` existia um pedaço de código que podia ser refatorado de maneira com que se reduziria o tamanho do código, sua complexidade e até mesmo melhorava seu funcionamento evitando em um contexto geral da aplicação a criação de complexidade desnecessária.

### Trechos de código

#### Anterior

```python
def calcular_imposto(self) -> dict:
    rendimento = self.rbt
    total_imposto = 0
    calculado = {
      'faixa_1': { 'valor_imposto': 0, 'valor_base': 0 },
      'faixa_2': { 'valor_imposto': 0, 'valor_base': 0 },
      'faixa_3': { 'valor_imposto': 0, 'valor_base': 0 },
      'faixa_4': { 'valor_imposto': 0, 'valor_base': 0 },
      'faixa_5': { 'valor_imposto': 0, 'valor_base': 0 },
      'total':{'valor_imposto': 0, 'valor_base':0 }
    }


    maximo_anterior = 0
    for faixa in self.tabela_irrf_2022:

      valor_maximo_na_faixa = round(self.tabela_irrf_2022[faixa]['max'] - maximo_anterior, 2)
      maximo_anterior = self.tabela_irrf_2022[faixa]['max']

      if(rendimento <= valor_maximo_na_faixa):
        calculado[faixa]['valor_base'] = rendimento
        calculado[faixa]['valor_imposto'] = self.normal_round(self.tabela_irrf_2022[faixa]['aliquota'] * rendimento, 4)
        total_imposto+=calculado[faixa]['valor_imposto'] 
        break
        
      else:
        calculado[faixa]['valor_base'] = valor_maximo_na_faixa
        rendimento = round(rendimento - calculado[faixa]['valor_base'], 2)
        calculado[faixa]['valor_imposto'] = self.normal_round(
          self.tabela_irrf_2022[faixa]['aliquota'] * valor_maximo_na_faixa, 4
          )
        total_imposto+=calculado[faixa]['valor_imposto'] 

    calculado['total']['valor_base'] = self.rbt
    calculado['total']['valor_imposto'] = self.normal_round(total_imposto, 2)
    return calculado
```

#### Refatorado

```python
    def calcular_imposto(self) -> dict:
        rendimento = self.rbt
        total_imposto = 0
        calculado = {}

        maximo_anterior = 0
        for faixa in self.tabela_irrf_2022:

            valor_maximo_na_faixa = round(
                self.tabela_irrf_2022[faixa]["max"] - maximo_anterior, 2
            )
            maximo_anterior = self.tabela_irrf_2022[faixa]["max"]

            if rendimento <= valor_maximo_na_faixa:
                calculado[faixa] = {
                    "valor_base": rendimento,
                    "valor_imposto": self.normal_round(
                        self.tabela_irrf_2022[faixa]["aliquota"] * rendimento,
                        4,
                    ),
                }

                total_imposto += calculado[faixa]["valor_imposto"]
                break

            else:
                calculado[faixa] = {
                    "valor_base": valor_maximo_na_faixa,
                    "valor_imposto": self.normal_round(
                        self.tabela_irrf_2022[faixa]["aliquota"]
                        * valor_maximo_na_faixa,
                        4,
                    ),
                }
                rendimento = round(
                    rendimento - calculado[faixa]["valor_base"], 2
                )
                total_imposto += calculado[faixa]["valor_imposto"]

        calculado["total"] = {
            "valor_imposto": self.normal_round(total_imposto, 2),
            "valor_base": self.rbt,
        }

        return calculado
```

### Arquivos

* `src/models/Faixa_de_imposto.py`
* `tests/test_faixas_de_imposto.py`

### Mal cheiros

O grupo identificou os seguintes mal cheiros nos códigos refatorados:

* Código duplicado
* Método longo
* Campo temporário
