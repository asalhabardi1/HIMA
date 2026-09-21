
import streamlit as st

st.set_page_config(
    page_title="ECO-SENTINEL",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --bg: #071216;
    --panel: #0d1b20;
    --panel2: #10242a;
    --line: #1d363b;
    --green: #72b446;
    --turquoise: #24b3ba;
    --sand: #c8aa72;
    --text: #edf5f1;
    --muted: #819399;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 80% 0%, rgba(36,179,186,.08), transparent 28%),
        radial-gradient(circle at 0% 30%, rgba(114,180,70,.06), transparent 25%),
        var(--bg);
    color: var(--text);
}

.block-container {
    padding: 1.5rem 3rem 3rem 3rem;
    max-width: 1550px;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #08171b;
    border-right: 1px solid var(--line);
}

section[data-testid="stSidebar"] .block-container {
    padding: 2rem 1.2rem;
}

/* HEADER */

.topline {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--line);
    padding-bottom: 18px;
    margin-bottom: 30px;
}

.brand {
    font-family: 'Space Grotesk';
    font-size: 15px;
    letter-spacing: 2px;
    font-weight: 700;
}

.brand span {
    color: var(--green);
}

.reserve {
    color: var(--muted);
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.logo-box {
    display: flex;
    gap: 12px;
    align-items: center;
}

.logo-placeholder {
    width: 46px;
    height: 46px;
    border: 1px solid #38545a;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--turquoise);
    font-family: 'Space Grotesk';
    font-size: 12px;
}

/* HERO */

.hero {
    padding: 18px 0 30px;
}

.eyebrow {
    color: var(--turquoise);
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 600;
}

.hero h1 {
    font-family: 'Space Grotesk';
    font-size: 58px;
    letter-spacing: -3px;
    margin: 8px 0 5px;
}

.hero h1 span {
    color: var(--green);
}

.hero p {
    color: var(--muted);
    font-size: 15px;
}

/* METRICS */

.metric-card {
    background: linear-gradient(145deg, #102126, #0b181c);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 22px;
    min-height: 142px;
    position: relative;
    overflow: hidden;
}

.metric-card:before {
    content: "";
    position: absolute;
    width: 100px;
    height: 100px;
    right: -45px;
    top: -45px;
    border-radius: 50%;
    background: rgba(36,179,186,.08);
}

.metric-label {
    color: var(--muted);
    font-size: 10px;
    letter-spacing: 1.8px;
    text-transform: uppercase;
}

.metric-value {
    font-family: 'Space Grotesk';
    font-size: 31px;
    font-weight: 600;
    margin-top: 12px;
}

.metric-detail {
    color: #60757b;
    font-size: 11px;
    margin-top: 6px;
}

/* MAP */

.map {
    height: 450px;
    margin-top: 25px;
    border-radius: 20px;
    border: 1px solid #294249;
    position: relative;
    overflow: hidden;

    background:
        radial-gradient(circle at 25% 65%, rgba(114,180,70,.18), transparent 22%),
        radial-gradient(circle at 72% 35%, rgba(36,179,186,.16), transparent 23%),
        linear-gradient(135deg, #0b191d, #071114);
}

.map-grid {
    position: absolute;
    inset: 0;
    opacity: .13;

    background-image:
        linear-gradient(#6e9390 1px, transparent 1px),
        linear-gradient(90deg, #6e9390 1px, transparent 1px);

    background-size: 55px 55px;
}

.map-header {
    position: absolute;
    top: 22px;
    left: 25px;
    z-index: 5;
}

.map-header small {
    color: var(--turquoise);
    letter-spacing: 2px;
    font-size: 9px;
}

.map-header h3 {
    font-family: 'Space Grotesk';
    margin-top: 5px;
}

/* ABSTRACT RESERVE */

.reserve-shape {
    position: absolute;
    left: 50%;
[09/04/48 09:10 م] S Al: top: 53%;
    transform: translate(-50%, -50%) rotate(-8deg);
    width: 390px;
    height: 215px;

    border: 2px solid rgba(114,180,70,.72);
    border-radius: 45% 55% 48% 52%;

    box-shadow:
        0 0 45px rgba(114,180,70,.10),
        inset 0 0 45px rgba(114,180,70,.04);
}

.zone {
    position: absolute;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--turquoise);
    box-shadow: 0 0 18px rgba(36,179,186,.7);
}

.zone.one {
    left: 42%;
    top: 43%;
}

.zone.two {
    left: 65%;
    top: 58%;
    background: var(--sand);
    box-shadow: 0 0 18px rgba(200,170,114,.7);
}

.map-label {
    position: absolute;
    bottom: 22px;
    left: 25px;
    color: #6f858a;
    font-size: 10px;
}

/* WARNING */

.warning {
    margin-top: 25px;
    min-height: 450px;
    background: linear-gradient(145deg, #101f23, #0b171a);
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 28px;
}

.warning-label {
    color: var(--sand);
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.signal {
    margin-top: 30px;
    padding: 20px;
    border-left: 3px solid var(--sand);
    background: rgba(200,170,114,.055);
    border-radius: 8px;
}

.signal-title {
    font-family: 'Space Grotesk';
    font-size: 18px;
}

.signal-text {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.7;
    margin-top: 10px;
}

/* PIPELINE */

.pipeline-title {
    margin-top: 40px;
    margin-bottom: 15px;
    font-family: 'Space Grotesk';
    font-size: 20px;
}

.pipeline {
    display: flex;
    gap: 10px;
    align-items: stretch;
}

.step {
    flex: 1;
    background: #0d1a1e;
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 19px 14px;
    text-align: center;
}

.step-number {
    color: var(--turquoise);
    font-size: 10px;
    letter-spacing: 1px;
}

.step-name {
    margin-top: 10px;
    font-size: 12px;
    color: #cbd8d4;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #53676c;
    font-size: 10px;
    letter-spacing: 1px;
    margin-top: 50px;
}

/* STREAMLIT */

div[data-testid="stMetric"] {
    background: transparent;
}

button[kind="secondary"] {
    border-color: var(--line);
}

</style>
""", unsafe_allow_html=True)


# SIDEBAR

with st.sidebar:

    st.markdown("""
    <div style="
        font-family:Space Grotesk;
        font-size:18px;
        font-weight:700;
        letter-spacing:2px;
        margin-bottom:35px;">
        ECO<span style="color:#72b446;">·</span>SENTINEL
    </div>
    """, unsafe_allow_html=True)

    st.caption("ENVIRONMENTAL INTELLIGENCE")

    st.radio(
        "SYSTEM",
        [
            "Overview",
            "Vegetation Intelligence",
            "AI Forecast",
            "Spatial Risk",
            "Early Warning"
        ],
        label_visibility="visible"
    )

    st.markdown("---")

    st.caption("CASE STUDY")

    st.markdown("""
    <div style="font-size:13px;line-height:1.7;color:#91a1a5;">
    Imam Turki bin Abdullah<br>
    Royal Reserve
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        margin-top:25px;
        padding:14px;
        border:1px solid #20363b;
        border-radius:10px;
        color:#6f858a;
        font-size:10px;
        line-height:1.6;">
        PROOF OF CONCEPT<br>
        Sentinel-2 · GIS · AI
    </div>
    """, unsafe_allow_html=True)


# TOP BAR

st.markdown("""
<div class="topline">

    <div>
        <div class="brand">
            ECO<span>·</span>SENTINEL
        </div>
        <div class="reserve">
            Environmental Intelligence System
        </div>
    </div>

    <div class="logo-box">

        <div style="
            text-align:right;
            color:#71858a;
            font-size:9px;
            line-height:1.5;">
            CASE STUDY<br>
            IMAM TURKI BIN ABDULLAH
        </div>

        <div class="logo-placeholder">
            ITBA
        </div>

        <div class="logo-placeholder">
            2030
        </div>

    </div>

</div>
[09/04/48 09:10 م] S Al: """, unsafe_allow_html=True)


# HERO

st.markdown("""
<div class="hero">

    <div class="eyebrow">
        Predictive Protected-Area Intelligence
    </div>

    <h1>
        ECO<span>-SENTINEL</span>
    </h1>

    <p>
        AI-powered environmental early warning and predictive monitoring
        for protected areas.
    </p>

</div>
""", unsafe_allow_html=True)


# METRICS

a, b, c, d = st.columns(4)

with a:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Vegetation Health</div>
        <div class="metric-value">0.12</div>
        <div class="metric-detail">Latest NDVI observation</div>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">AI Forecast Horizon</div>
        <div class="metric-value">2026–2030</div>
        <div class="metric-detail">LSTM-based prediction</div>
    </div>
    """, unsafe_allow_html=True)

with c:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Priority Zones</div>
        <div class="metric-value">02</div>
        <div class="metric-detail">Prototype monitoring layer</div>
    </div>
    """, unsafe_allow_html=True)

with d:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Observation Period</div>
        <div class="metric-value">2015–25</div>
        <div class="metric-detail">Sentinel-2 time series</div>
    </div>
    """, unsafe_allow_html=True)


# MAIN VISUAL

left, right = st.columns([2.15, 1])

with left:

    st.markdown("""
    <div class="map">

        <div class="map-grid"></div>

        <div class="map-header">
            <small>SPATIAL INTELLIGENCE</small>
            <h3>Imam Turki bin Abdullah Royal Reserve</h3>
        </div>

        <div class="reserve-shape">

            <div class="zone one"></div>
            <div class="zone two"></div>

        </div>

        <div class="map-label">
            PROTECTED AREA · 91,500 KM² · PROTOTYPE VIEW
        </div>

    </div>
    """, unsafe_allow_html=True)


with right:

    st.markdown("""
    <div class="warning">

        <div class="warning-label">
            Early Warning Layer
        </div>

        <h2 style="
            font-family:Space Grotesk;
            margin-top:12px;">
            Environmental Signal
        </h2>

        <p style="
            color:#819399;
            font-size:12px;
            line-height:1.8;">
            ECO-SENTINEL combines observed vegetation conditions
            with predicted trends to identify areas requiring
            priority environmental assessment.
        </p>

        <div class="signal">

            <div class="signal-title">
                Priority monitoring zone
            </div>

            <div class="signal-text">
                Predicted vegetation change detected.
                Further spatial assessment is recommended.
            </div>

        </div>

        <div style="
            margin-top:28px;
            color:#61767b;
            font-size:10px;
            letter-spacing:1px;">
            STATUS
        </div>

        <div style="
            margin-top:8px;
            color:#72b446;
            font-family:Space Grotesk;
            font-size:18px;">
            PREDICTIVE MONITORING ACTIVE
        </div>

    </div>
    """, unsafe_allow_html=True)


# PIPELINE

st.markdown("""
<div class="pipeline-title">
    Intelligence Pipeline
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="pipeline">

    <div class="step">
        <div class="step-number">01</div>
        <div class="step-name">Satellite Data</div>
    </div>

    <div class="step">
        <div class="step-number">02</div>
        <div class="step-name">Environmental Indicators</div>
    </div>

    <div class="step">
        <div class="step-number">03</div>
        <div class="step-name">AI Forecasting</div>
    </div>

    <div class="step">
        <div class="step-number">04</div>
        <div class="step-name">Spatial Risk</div>
    </div>
[09/04/48 09:10 م] S Al: <div class="step">
        <div class="step-number">05</div>
        <div class="step-name">Early Warning</div>
    </div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="footer">
ECO-SENTINEL · PROOF OF CONCEPT · IMAM TURKI BIN ABDULLAH ROYAL RESERVE
</div>
""", unsafe_allow_html=True)
