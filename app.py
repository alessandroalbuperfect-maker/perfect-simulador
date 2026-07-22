import streamlit as st

# Configuração visual do aplicativo
st.set_page_config(page_title="Checklist & Simulador - Perfect Energia Solar", page_icon="☀️", layout="wide")

st.title("📋 Checklist Técnico & Simulador Comercial — Perfect Energia Solar")
st.caption("Ferramenta de campo alinhada ao padrão oficial de vistoria técnica e vendas.")

# Divisão por Abas do Checklist
tab1, tab2, tab3, tab4 = st.tabs([
    "1. Padrão & Entrada Elétrica", 
    "2. Inversor & Telhado", 
    "3. Dimensionamento (Gokin + Sungrow)", 
    "4. Estudo Financeiro & Resumo"
])

# ==========================================
# ABA 1: PADRÃO E CONEXÃO ELÉTRICA
# ==========================================
with tab1:
    st.header("1. Entrada — Padrão e Conexão Elétrica")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        cliente = st.text_input("Cliente:", value="Sr. Rafael")
        endereco = st.text_input("Endereço:", value="Rua das Palmeiras, 123")
    with col2:
        closer = st.text_input("Closer / Vendedor:", value="Alessandro")
        concessionaria = st.selectbox("Concessionária:", ["Copel", "Celesc", "Outra"])
    with col3:
        ambiente = st.radio("Ambiente:", ["Urbano", "Rural"], horizontal=True)
        tipo_ligacao = st.selectbox("Tipo de Ligação:", ["Monofásico", "Bifásico", "Trifásico"])

    st.markdown("---")
    st.subheader("Verificações de Campo (Checklist)")
    
    col4, col5, col6 = st.columns(3)
    with col4:
        bitola_cabos = st.selectbox("Bitola dos Cabos de Entrada (mm²):", [4.0, 6.0, 10.0, 16.0, 25.0, 35.0, 50.0, 70.0, 95.0], index=2)
        disjuntor_geral = st.selectbox("Disjuntor Geral (A):", [32, 40, 50, 63, 80, 100, 125, 150, 200], index=2)
    with col5:
        tensao_rede = st.selectbox("Tensão da Rede Elétrica:", ["220V Monofásico/Bifásico", "220V Trifásico", "380V Trifásico"])
        distancia_cc_ca = st.number_input("Rota de Cabeamento (Distância CC/CA até o inversor em metros):", min_value=1, value=20, step=5)
    with col6:
        estado_caixa = st.selectbox("Estado Físico da Caixa do Medidor:", ["Ótimo / Novo", "Bom", "Ferrugem / Avaria Leve", "Danificada / Troca Necessária"])
        estado_poste = st.selectbox("Estado Físico do Poste Padrão:", ["Ótimo / Novo", "Bom", "Rachaduras / Trincas", "Danificado / Troca Necessária"])

    st.markdown("---")
    col7, col8 = st.columns(2)
    with col7:
        espaco_dps = st.checkbox("Possui espaço para instalação do DPS no Quadro de Distribuição (QD)?", value=True)
        espaco_disjuntor_ca = st.checkbox("Possui espaço para instalação do Disjuntor CA no Quadro (QD)?", value=True)
        fatura_em_maos = st.checkbox("Fatura Atualizada em Mãos (PDF / Digital)?", value=True)
    with col8:
        pendencias = st.text_area("Pendências e Recomendações (Itens a corrigir/reforço/troca):", "Nenhuma pendência aparente no padrão.")

# ==========================================
# ABA 2: LOCAL DO INVERSOR, TELHADO E RISCOS
# ==========================================
with tab2:
    st.header("2. Local de Instalação, Telhado e Riscos")
    
    col9, col10 = st.columns(2)
    with col9:
        st.subheader("2. Local do Inversor")
        ventilacao_ok = st.checkbox("Ambiente ventilado e protegido contra sol/chuva direta", value=True)
        proximidade_qd = st.checkbox("String Box e Inversor próximos ao Quadro Principal", value=True)
        distancia_inversor_padrao = st.number_input("Distância entre Inversor e Padrão de Entrada (m):", min_value=1, value=15)
        
    with col10:
        st.subheader("4. Riscos & Sombreamento")
        sombreamento = st.selectbox("Sombreamento (Chaminés, árvores, prédios vizinhos):", ["Sem sombreamento", "Sombreamento Parcial (Manhã/Tarde)", "Sombreamento Severo"])
        infra_extra = st.text_input("Necessidade de Infraestrutura Extra:", "Nenhuma (Utilizar eletrodutos existentes)")

    st.markdown("---")
    st.subheader("3. Estrutura e Telhado")
    
    col11, col12, col13 = st.columns(3)
    with col11:
        tipo_telha = st.selectbox("Tipo de Telha / Estrutura:", ["Cerâmica (Colonial)", "Fibrocimento", "Metálica", "Zinco", "Laje", "Solo"])
        orientacao = st.selectbox("Orientação Solar Principal:", ["Norte", "Nordeste", "Noroeste", "Leste", "Oeste", "Sul"])
    with col12:
        inclinacao = st.number_input("Inclinação Aproximada (graus °):", min_value=0, max_value=90, value=15)
        area_disponivel = st.number_input("Área Disponível no Telhado (m²):", min_value=5, value=60)
    with col13:
        avaliacao_estrutura = st.selectbox("Avaliação Estrutural do Telhado:", ["Estrutura em ótimo estado", "Estrutura necessita reforço pontual", "Necessita Laudo Técnico de Engenharia"])

# ==========================================
# ABA 3: DIMENSIONAMENTO DO KIT (GOKIN + SUNGROW)
# ==========================================
with tab3:
    st.header("3. Dimensionamento Técnico da Solução Perfect")
    
    col14, col15 = st.columns(2)
    with col14:
        valor_conta = st.number_input("Valor Médio da Conta Atual (R$):", min_value=100.0, value=1000.0, step=50.0)
        tarifa_kwh = st.number_input("Tarifa da Concessionária (R$/kWh):", min_value=0.5, value=0.95, step=0.05)
    with col15:
        st.subheader("Previsão de Aumento de Consumo Futuro")
        add_ar = st.checkbox("Ar-condicionado Novo (+150 kWh/mês)")
        add_ev = st.checkbox("Carregador de Veículo Elétrico (+300 kWh/mês)")
        add_piscina = st.checkbox("Aquecimento de Piscina (+400 kWh/mês)")
        add_ampliacao = st.checkbox("Ampliação da Casa / Comércio (+200 kWh/mês)")

    # Cálculos
    consumo_atual = valor_conta / tarifa_kwh
    consumo_extra = (150 if add_ar else 0) + (300 if add_ev else 0) + (400 if add_piscina else 0) + (200 if add_ampliacao else 0)
    consumo_total_alvo = consumo_atual + consumo_extra
    
    # Placas Gokin (550W N-Type Bifacial, média de 68 kWh/mês por módulo)
    potencia_módulo = 550
    qtd_placas = int(-(-consumo_total_alvo // 68.0))
    potencia_kwp = (qtd_placas * potencia_módulo) / 1000.0

    # Escolha Automática do Inversor Sungrow
    inversor_sungrow = ""
    if tensao_rede == "220V Monofásico/Bifásico":
        if potencia_kwp <= 3.5:
            inversor_sungrow = "Sungrow SG3.0RS (Monofásico)"
        elif potencia_kwp <= 6.0:
            inversor_sungrow = "Sungrow SG5.0RS (Monofásico)"
        elif potencia_kwp <= 8.5:
            inversor_sungrow = "Sungrow SG7.5RS-L (Mono/Bifásico - 3 MPPTs)"
        else:
            inversor_sungrow = "Sungrow SG10RS (Monofásico)"
    elif tensao_rede == "220V Trifásico":
        if potencia_kwp <= 18:
            inversor_sungrow = "Sungrow SG15CX-LV (Trifásico 220V)"
        else:
            inversor_sungrow = "Sungrow SG25CX-LV / SG75CX-LV (Trifásico 220V)"
    else: # 380V Trifásico
        if potencia_kwp <= 12:
            inversor_sungrow = "Sungrow SG10RT (Trifásico 380V)"
        elif potencia_kwp <= 22:
            inversor_sungrow = "Sungrow SG20RT (Trifásico 380V)"
        else:
            inversor_sungrow = "Sungrow SG50CX / SG110CX-P2 (Comercial 380V)"

    st.markdown("---")
    st.subheader("Resultado do Dimensionamento")
    
    col16, col17 = st.columns(2)
    with col16:
        st.info(f"⚡ **Consumo Atual:** {consumo_atual:.0f} kWh/mês\n\n➕ **Consumo Futuro Extra:** {consumo_extra} kWh/mês\n\n🎯 **CONSUMO TOTAL ALVO:** {consumo_total_alvo:.0f} kWh/mês")
        st.success(f"☀️ **Módulos Solares:** {qtd_placas} x Painéis Gokin 550W N-Type Bifacial\n\n🔌 **Inversor Recomendado:** {inversor_sungrow}\n\n📐 **Potência Instalada:** {potencia_kwp:.2f} kWp")
    
    with col17:
        # Validação da Corrente Elétrica x Disjuntor Geral
        corrente_estimada = (potencia_kwp * 1000) / (220 if "220V" in tensao_rede else 380)
        st.subheader("Validação de Engenharia Automática")
        
        if corrente_estimada > (disjuntor_geral * 0.85):
            st.warning(f"⚠️ **Atenção:** A corrente gerada ({corrente_estimada:.1f}A) atinge mais de 85% do disjuntor geral ({disjuntor_geral}A). **Recomendada adequação/troca do disjuntor ou padrão.**")
        else:
            st.success(f"✅ **Padrão Elétrico Aprovado:** Disjuntor de {disjuntor_geral}A e cabos de {bitola_cabos}mm² suportam a corrente de {corrente_estimada:.1f}A com total segurança.")

# ==========================================
# ABA 4: ESTUDO FINANCEIRO & RELATÓRIO CONSOLIDADO
# ==========================================
with tab4:
    st.header("4. Estudo Financeiro e Relatório de Campo")
    
    economia_mensal = (consumo_total_alvo * tarifa_kwh) * 0.82 # 82% de economia média
    economia_anual = economia_mensal * 12
    economia_25anos = economia_anual * 25
    
    col18, col19, col20 = st.columns(3)
    col18.metric("Economia Mensal Estimada", f"R$ {economia_mensal:.2f}")
    col19.metric("Economia Anual", f"R$ {economia_anual:.2f}")
    col20.metric("Economia em 25 Anos", f"R$ {economia_25anos:,.2f}")

    st.markdown("---")
    st.subheader("Simulador 'Troca de Boleto' (Financiamento)")
    
    prazo = st.radio("Prazo do Financiamento:", ["36x", "48x", "60x"], horizontal=True)
    fatores = {"36x": 0.037, "48x": 0.030, "60x": 0.026}
    investimento_estimado = potencia_kwp * 3750.0
    parcela_estimada = investimento_estimado * fatores[prazo]

    col21, col22 = st.columns(2)
    with col21:
        st.write(f"🔴 **Gasto Atual na Conta de Luz:** R$ {valor_conta:.2f} / mês")
    with col22:
        st.write(f"🟢 **Parcela Estimada ({prazo}):** R$ {parcela_estimada:.2f} / mês")

    if parcela_estimada <= valor_conta:
        st.success("🎉 **PROPOSTA PERFEITA:** A parcela do financiamento fica menor ou igual ao valor atual pago para a concessionária!")
    else:
        st.info("💡 A parcela fica equivalente ao valor atual, já garantindo a cobertura dos aumentos futuros de consumo!")

    st.markdown("---")
    st.subheader("📄 Resumo do Checklist Técnico para Envio")
    
    relatorio_texto = f"""
    ===================================================
    CHECKLIST TÉCNICO DE VISITA — PERFECT ENERGIA SOLAR
    ===================================================
    CLIENTE: {cliente} | CLOSER: {closer}
    ENDEREÇO: {endereco}
    CONCESSIONÁRIA: {concessionaria} ({ambiente})
    
    1. PADRÃO E CONEXÃO ELÉTRICA:
    - Ligação: {tipo_ligacao} ({tensao_rede})
    - Cabos Entrada: {bitola_cabos} mm² | Disjuntor Geral: {disjuntor_geral} A
    - Estado Caixa Medidor: {estado_caixa} | Estado Poste: {estado_poste}
    - Rota CC/CA: {distancia_cc_ca} metros
    - Espaço DPS/Disjuntor CA: {'Sim' if espaco_dps and espaco_disjuntor_ca else 'Não (Necessita caixa auxiliar)'}
    - Fatura em Mãos: {'Sim' if fatura_em_maos else 'Não'}
    - Pendências: {pendencias}
    
    2. LOCAL INVERSOR & TELHADO:
    - Ventilação/Proteção: {'Ok' if ventilacao_ok else 'Ajustar local'}
    - Telhado: {tipo_telha} | Orientação: {orientacao} ({inclinacao}°)
    - Área Disponível: {area_disponivel} m²
    - Avaliação Estrutural: {avaliacao_estrutura}
    - Sombreamento: {sombreamento} | Infra Extra: {infra_extra}
    
    3. DIMENSIONAMENTO DO SISTEMA PERFECT:
    - Consumo Alvo: {consumo_total_alvo:.0f} kWh/mês
    - Placas: {qtd_placas} x Painéis Gokin 550W N-Type Bifacial ({potencia_kwp:.2f} kWp)
    - Inversor: {inversor_sungrow}
    
    4. ANÁLISE FINANCEIRA:
    - Economia Mensal Estimada: R$ {economia_mensal:.2f}
    - Parcela Estimada ({prazo}): R$ {parcela_estimada:.2f}
    ===================================================
    """
    
    st.code(relatorio_texto, language="text")
