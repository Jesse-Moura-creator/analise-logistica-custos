#CALCULADORA PARA IDENTIFICAR PADRÕES DURANTE RECOLOCAÇÃO NO MERCADO DE TRABALHO

def calcular_probabilidades(total_candidaturas, periodo_dias, entrevistas_realizadas, selecoes):
    """
    Calcula as probabilidades médias de ser chamado para entrevista e de ser selecionado.

    Parâmetros:
    total_candidaturas (int): Quantidade total de vagas em que se candidatou
    periodo_dias (int): Período em dias em que as candidaturas foram feitas
    entrevistas_realizadas (int): Quantidade de entrevistas realizadas no período
    selecoes (int): Quantidade de vagas em que foi selecionado

    Retorna:
    dict: Dicionário com as probabilidades calculadas e métricas adicionais
    """

    # Cálculo das probabilidades
    prob_entrevista = (entrevistas_realizadas / total_candidaturas) * 100 if total_candidaturas > 0 else 0
    prob_selecao_das_entrevistas = (selecoes / entrevistas_realizadas) * 100 if entrevistas_realizadas > 0 else 0
    prob_selecao_das_candidaturas = (selecoes / total_candidaturas) * 100 if total_candidaturas > 0 else 0

    # Ajuste para 30 dias (média diária)
    candidaturas_por_dia = total_candidaturas / periodo_dias if periodo_dias > 0 else 0
    entrevistas_por_dia = entrevistas_realizadas / periodo_dias if periodo_dias > 0 else 0
    selecoes_por_dia = selecoes / periodo_dias if periodo_dias > 0 else 0

    # Projeção para 30 dias
    candidaturas_30dias = candidaturas_por_dia * 30
    entrevistas_30dias = entrevistas_por_dia * 30
    selecoes_30dias = selecoes_por_dia * 30

    return {
        'Probabilidade de ser chamado para entrevista': f"{prob_entrevista:.2f}%",
        'Probabilidade de seleção (dentre as entrevistas)': f"{prob_selecao_das_entrevistas:.2f}%",
        'Probabilidade de seleção (dentre todas as candidaturas)': f"{prob_selecao_das_candidaturas:.2f}%",
        'Métricas diárias': {
            'Candidaturas por dia': f"{candidaturas_por_dia:.2f}",
            'Entrevistas por dia': f"{entrevistas_por_dia:.2f}",
            'Seleções por dia': f"{selecoes_por_dia:.2f}"
        },
        'Projeção para 30 dias': {
            'Total de candidaturas': f"{candidaturas_30dias:.2f}",
            'Total de entrevistas': f"{entrevistas_30dias:.2f}",
            'Total de seleções': f"{selecoes_30dias:.2f}"
        }
    }

# Exemplo de uso
if __name__ == "__main__":
    print("Calculadora de Probabilidades de Entrevistas e Seleções\n")

    # Input dos dados
    total_candidaturas = int(input("Total de vagas em que se candidatou: "))
    periodo_dias = int(input("Período das candidaturas (em dias): "))
    entrevistas_realizadas = int(input("Quantidade de entrevistas realizadas: "))
    selecoes = int(input("Quantidade de seleções: "))

    # Cálculo
    resultados = calcular_probabilidades(total_candidaturas, periodo_dias, entrevistas_realizadas, selecoes)

    # Exibição dos resultados
    print("\n--- Resultados ---")
    for chave, valor in resultados.items():
        if isinstance(valor, dict):
            print(f"\n{chave}:")
            for sub_chave, sub_valor in valor.items():
                print(f"  {sub_chave}: {sub_valor}")
        else:
            print(f"{chave}: {valor}")
# UMA OBSERVAÇÃO É QUE, A SELEÇÃO PARA A VAGA, INDEPENDE SE FOI ACEITA PELO CANDIDATO OU NÃO. TEM APENAS O VIÉS DA PERSPECTIVA DA EMPRESA.
# MAS A CALCULADORA SERVE PARA O CANDIDATO ACOMPANHAR AS PROBABILIDADES E ESTATÍSTICAS NO SEU "FUNIL DE EMPREGABILIDADE" EM UM DETERMINADO PERÍODO