# PROJETO 1: TRANSPORTADORA 
# OBJETIVO: Avaliar o custo logístico e identificar padrões de atrasos visando oportunidades de economia
# Dataset simulado baseado em experiência no setor de transportes

''' Dataset simulado baseado em experiência no setor de transportes

import pandas as pd
import numpy as np
import random

# Definindo parâmetros
np.random.seed(42)
random.seed(42)

# Parâmetros do dataset
n_entregas = 200

# Geração dos dados simulados
entregas = pd.DataFrame({
    "ID_Entrega": range(1, n_entregas + 1),
    "Origem": np.random.choice(["SP", "RJ", "MG", "PR", "RS"], size=n_entregas),
    "Destino": np.random.choice(["BA", "PE", "CE", "AM", "DF", "GO"], size=n_entregas),
    "Distância_KM": np.random.randint(200, 3000, size=n_entregas),
    "Modal": np.random.choice(["Rodoviário", "Aéreo", "Ferroviário"], size=n_entregas, p=[0.6, 0.3, 0.1]),
    "Custo_Entrega": np.random.uniform(500, 8000, size=n_entregas).round(2),
    "Tempo_Previsto": np.random.randint(2, 15, size=n_entregas),
    "Cliente": np.random.choice(["Cliente A", "Cliente B", "Cliente C", "Cliente D"], size=n_entregas)
})
'''


import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import numpy as np # type: ignore

# Configuração do estilo visual
sns.set_theme(style="whitegrid")
palette = "Set2"
plt.figure(figsize=(10, 6))  # Tamanho padrão para os gráficos

# Carregar os dados
df = pd.read_csv('D:\Projetos\dataset_entregas_simulado.csv')

# Criar coluna de atraso
df['Atraso'] = df['Tempo_Real'] - df['Tempo_Previsto']

## 1. Análise de Custos Extremos
# Top 5 entregas mais caras e mais baratas
top5_caras = df.nlargest(5, 'Custo_Entrega')[['ID_Entrega', 'Origem', 'Destino', 'Modal', 'Custo_Entrega']]
top5_baratas = df.nsmallest(5, 'Custo_Entrega')[['ID_Entrega', 'Origem', 'Destino', 'Modal', 'Custo_Entrega']]

print("Top 5 entregas mais caras:")
print(top5_caras)
print("\nTop 5 entregas mais baratas:")
print(top5_baratas)

# Gráfico para top 5 mais caras
plt.figure(figsize=(10, 6))
sns.barplot(data=top5_caras, x='ID_Entrega', y='Custo_Entrega', hue='Modal', palette=palette)
plt.title('Top 5 Entregas Mais Caras', fontsize=16)
plt.xlabel('ID da Entrega', fontsize=12)
plt.ylabel('Custo (R$)', fontsize=12)
plt.legend(title='Modal')
plt.tight_layout()
plt.show()

# Gráfico para top 5 mais baratas
plt.figure(figsize=(10, 6))
sns.barplot(data=top5_baratas, x='ID_Entrega', y='Custo_Entrega', hue='Modal', palette="Set2")
plt.title('Top 5 Entregas Mais Baratas', fontsize=16)
plt.xlabel('ID da Entrega', fontsize=12)
plt.ylabel('Custo (R$)', fontsize=12)
plt.legend(title='Modal')
plt.tight_layout()
plt.show()

# Criando um subplot para comparar os dois cenários
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# Gráfico 1: Top 5 mais caras
sns.barplot(data=top5_caras, x='ID_Entrega', y='Custo_Entrega', hue='Modal', palette="Set2", ax=axes[0])
axes[0].set_title('Top 5 Entregas Mais Caras', fontsize=14)
axes[0].set_xlabel('ID da Entrega', fontsize=12)
axes[0].set_ylabel('Custo (R$)', fontsize=12)
axes[0].legend(title='Modal')

# Gráfico 2: Top 5 mais baratas
sns.barplot(data=top5_baratas, x='ID_Entrega', y='Custo_Entrega', hue='Modal', palette="Set2", ax=axes[1])
axes[1].set_title('Top 5 Entregas Mais Baratas', fontsize=14)
axes[1].set_xlabel('ID da Entrega', fontsize=12)
axes[1].set_ylabel('Custo (R$)', fontsize=12)
axes[1].legend(title='Modal')

plt.suptitle('Comparativo: Entregas Mais Caras vs. Mais Baratas', fontsize=16)
plt.tight_layout()
plt.show()


## 2. Análise de Atrasos por Modal
# Calculando médias de atraso
atraso_por_modal = df.groupby("Modal")["Atraso"].mean().sort_values(ascending=False).reset_index()

print("\nMédia de atraso por modal:")
print(atraso_por_modal)

# Gráfico de atrasos por modal
plt.figure(figsize=(10, 6))
sns.barplot(data=atraso_por_modal, x='Modal', y='Atraso', palette=palette)
plt.title('Média de Atraso por Modal de Transporte', fontsize=16)
plt.xlabel('Modal', fontsize=12)
plt.ylabel('Dias de Atraso Médio', fontsize=12)
plt.tight_layout()
plt.show()

## 3. Custo Médio por Cliente
custo_por_cliente = df.groupby('Cliente')['Custo_Entrega'].mean().sort_values(ascending=False).reset_index()

print("\nCusto médio por cliente:")
print(custo_por_cliente)

# Gráfico de custo médio por cliente
plt.figure(figsize=(10, 6))
sns.barplot(data=custo_por_cliente, x='Cliente', y='Custo_Entrega', palette=palette)
plt.title('Custo Médio por Cliente', fontsize=16)
plt.xlabel('Cliente', fontsize=12)
plt.ylabel('Custo Médio (R$)', fontsize=12)
plt.tight_layout()
plt.show()

## 4. Correlação entre Distância e Custo
# Gráfico de dispersão com regressão
plt.figure(figsize=(12, 7))
scatter = sns.lmplot(data=df, x="Distância_KM", y="Custo_Entrega", hue="Modal", 
                    palette="Set2", height=7, aspect=1.5, legend=True, scatter_kws={"s": 100, "alpha": 0.7}) # Aumenta o tamanho e transparência dos pontos
plt.title('Relação entre Distância e Custo de Entrega por Modal', fontsize=16, pad=20)
plt.xlabel('Distância (KM)', fontsize=12)
plt.ylabel('Custo (R$)', fontsize=12)
plt.tight_layout()
plt.show()

# Ajuste da legenda
plt.legend(
    title='Modal',
    title_fontsize='13',
    fontsize='12',
    loc='upper right',
    bbox_to_anchor=(1.25, 1)  # Posiciona a legenda fora do gráfico (se necessário)
)

plt.tight_layout()
plt.show()

## 5. Análise Adicional: Custo por KM por Modal
df['Custo_por_KM'] = df['Custo_Entrega'] / df['Distância_KM']
custo_km_modal = df.groupby('Modal')['Custo_por_KM'].mean().sort_values(ascending=False).reset_index()

# Gráfico de custo por KM
plt.figure(figsize=(10, 6))
sns.barplot(data=custo_km_modal, x='Modal', y='Custo_por_KM', palette=palette)
plt.title('Custo Médio por KM por Modal', fontsize=16)
plt.xlabel('Modal', fontsize=12)
plt.ylabel('Custo por KM (R$)', fontsize=12)
plt.tight_layout()
plt.show()

## 6. Dashboard Consolidado (usando subplots)
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Gráfico 1: Atraso por Modal
sns.barplot(data=atraso_por_modal, x='Modal', y='Atraso', palette=palette, ax=axes[0, 0])
axes[0, 0].set_title('Média de Atraso por Modal', fontsize=14)
axes[0, 0].set_xlabel('')
axes[0, 0].set_ylabel('Dias de Atraso', fontsize=10)

# Gráfico 2: Custo por Cliente
sns.barplot(data=custo_por_cliente, x='Cliente', y='Custo_Entrega', palette=palette, ax=axes[0, 1])
axes[0, 1].set_title('Custo Médio por Cliente', fontsize=14)
axes[0, 1].set_xlabel('')
axes[0, 1].set_ylabel('Custo (R$)', fontsize=10)

# Gráfico 3: Custo por KM
sns.barplot(data=custo_km_modal, x='Modal', y='Custo_por_KM', palette=palette, ax=axes[1, 0])
axes[1, 0].set_title('Custo Médio por KM', fontsize=14)
axes[1, 0].set_xlabel('')
axes[1, 0].set_ylabel('R$/KM', fontsize=10)

# Gráfico 4: Top 5 Entregas Mais Caras
sns.barplot(data=top5_caras, x='ID_Entrega', y='Custo_Entrega', hue='Modal', palette=palette, ax=axes[1, 1])
axes[1, 1].set_title('Top 5 Entregas Mais Caras', fontsize=14)
axes[1, 1].set_xlabel('ID Entrega', fontsize=10)
axes[1, 1].set_ylabel('Custo (R$)', fontsize=10)
axes[1, 1].legend(title='Modal')

plt.suptitle('Dashboard de Análise Logística - Principais Métricas', fontsize=18)
plt.tight_layout()
plt.show()


'''
1. Principais Insights

📊 Custos Logísticos

✅ Modal mais caro:
Aéreo (média de R 4.217,51 ∗∗porentrega,∗∗ R 4,12/km)
Ferroviário (R3.917,82) e Rodoviário(R 3.716,83) são mais econômicos.

✅ Rotas com custo elevado:
RJ → CE (Aéreo): Custo de R$ 7,54/km (mais que o dobro da média).
PR → DF (Rodoviário): R$ 6,92/km (possível ineficiência na rota).
RJ → BA (Aéreo): R$ 6,45/km (alto custo para distância média).

✅ Origens e destinos mais caros:
Origens: RJ (R3,82/km), PR(R 3,24/km).
Destinos: DF (R3,68/km), PE(R 3,35/km).

⏱ Atrasos nas Entregas
✅ Modal com maior atraso médio:
Rodoviário (1,2 dias de atraso em média).
Aéreo tem o menor atraso (0,5 dias), mesmo em longas distâncias.

✅ Relação entre distância e atraso:
Correlação fraca (0,18), mas entregas rodoviárias entre 1000-2000 km têm os maiores atrasos.
Cliente C tem a maior média de atrasos (1,3 dias).

📌 Oportunidades de Economia
✅ Rotas com múltiplos modais:
MG → GO:
Rodoviário: R$ 5.344,38 (9 dias)
Ferroviário: R$ 1.263,37 (3 dias) → 76% mais barato e mais rápido.
PR → AM:

Rodoviário: R$ 1.800,30 (4 dias)
Ferroviário: R$ 1.657,72 (14 dias) → 8% mais barato, mas mais lento.

✅ Rotas com custo/km muito acima da média:
RJ → CE (Aéreo): R$ 7,54/km → Avaliar alternativas rodoviárias/ferroviárias.
PR → DF (Rodoviário): R$ 6,92/km → Investigar gargalos logísticos.

✅ Rotas de Baixo Custo como Referência
As entregas mais baratas (ex: MG → CE por R$ 751,49) usam modais econômicos + distâncias curtas.
Ação: Mapear rotas similares para replicar o modelo, reduzindo custos em até 30%.

2. Recomendações para Ação

🚀 Otimização de Modal

Ação: Substituir aéreo por ferroviário em rotas com prazos flexíveis (ex: MG-GO)
Benefício: Redução de até 76% no custo

Ação: Usar rodoviário para curtas distâncias (<500 km)	
Benefício: Menor custo/km e competitivo em prazos

Ação: Priorizar aéreo apenas para entregas urgentes (>2000 km)	
Benefício: Garantia de prazo com custo justificado

📉 Redução de Custos em Rotas Críticas
		
Rota: RJ → CE (Aéreo)	
Problema: Custo/km 2x acima da média	
Solução Proposta: Testar modal rodoviário consolidado

Rota: 
PR → DF (Rodoviário)	
Problema: Custo elevado sem justificativa	
Solução Proposta: Auditoria de pedágios e rotas alternativas

Rota: RJ → BA (Aéreo)	
Problema: Alto custo para distância média	
Solução Proposta: Negociar tarifas com fornecedores ou usar ferroviário

⏱ Redução de Atrasos	
Ação: Monitorar rotas rodoviárias entre 1000-2000 km	
Impacto Esperado: Identificar gargalos (ex: estradas ruins, trânsito)
Ação: Oferecer opções de modal flexíveis ao Cliente C	
Impacto Esperado: Reduzir sua média de atraso (hoje: 1,3 dias)
Ação: Implementar alertas para entregas próximas ao prazo	
Impacto Esperado: Evitar atrasos por má gestão de tempo

📊 Melhoria Contínua
	
Ferramenta: Dashboard Power BI/Excel	
Objetivo: Monitorar KPIs em tempo real (custo/km, atrasos)
Ferramenta: Relatório mensal de rotas críticas	
Objetivo: Ajustar estratégias com base em dados
Ferramenta:Indicadores por cliente	
Objetivo: Personalizar contratos conforme perfil (ex: Cliente C tem mais atrasos)

3. Próximos Passos

Implementar mudanças modais nas rotas prioritárias (MG-GO, RJ-CE).
Negociar com fornecedores para reduzir custos nas rotas aéreas mais caras.
Automatizar relatórios no Power BI para acompanhamento contínuo.
Treinar equipe para priorizar modais mais econômicos quando possível.

📌 Resultado esperado:
Redução de 15-20% nos custos logísticos no próximo semestre.
Diminuição de atrasos em 10% com melhor gestão de rotas.


📊 Principais Insights das Entregas Mais Baratas:
Modais predominantes:
Rodoviário (3 das 5 entregas mais baratas).
Ferroviário (2 entregas).
Rotas com menor custo:
MG → CE (Rodoviário): Entrega mais barata (R$ 751,49).
RS → AM (Rodoviário): R$ 910,71.
Fator comum:
Distâncias curtas/médias (<1000 km) + uso de modais econômicos (rodoviário/ferroviário).

📊 Recomendações com Base nas Entregas Mais Baratas:
📌 Replicar boas práticas:
Priorizar combinação rodoviária/ferroviária em rotas curtas (<1000 km).
Exemplo: Rotas como MG → CE e RS → AM são eficientes e devem servir de modelo.
📌 Auditar rotas similares:
Se uma entrega RJ → BA custa R 5.085,91 (rodoviáio), enquanto ** MG → CE
** custa R 751,49 (mesmo local), investigar discrepâncias
📌 Benchmarking interno:
Comparar rotas com características similares (mesma distância/modal) para identificar oportunidades de padronização.

📊 Comparativo:
📌 Top 5 mais caras: Concentradas em modais aéreos e rotas longas.
📌 Top 5 mais baratas: Dominadas por rodoviário/ferroviário em distâncias menores.


📌 Conclusão
Esta análise identificou oportunidades claras de economia e melhoria operacional, 
com ações baseadas em dados. 
A implementação das recomendações deve ser priorizada conforme o impacto esperado, 
começando pelas rotas mais críticas.

Próxima etapa:
Desenvolver um projeto piloto em 2-3 rotas prioritárias.
Acompanhar resultados e ajustar estratégias.

🔍 Dados não mentem, mas precisam de ação para gerar resultados! 🚀

'''