import streamlit as st
from protac_nexus.config.services import SERVICES

def render():
    st.markdown('''<div class="hero"><div style="color:#8CEBE7;text-transform:uppercase;letter-spacing:.12em;font-size:.75rem">Natural products • Targeted protein degradation • Cancer research</div><h1>PROTAC Nexus</h1><p><b>Natural Products–Based PROTACs for Cancer Therapy</b></p><p>A research platform to explore natural compounds and derivatives as potential PROTAC building blocks, assess computational design hypotheses, and connect findings with published experimental evidence.</p></div>''', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Your research workspace</div>', unsafe_allow_html=True)
    a,b,c,d=st.columns(4); a.metric("Scientific services","10"); b.metric("Research services","2"); c.metric("Portal areas","3"); d.metric("Live scientific engines","0",help="Integrations will be enabled after the interface and workflows are ready.")
    st.subheader("Start exploring")
    names=["Natural Products Explorer","PROTAC Explorer","Experimental Data Explorer","Molecular Docking","Linker Optimization","Research Consultation"]
    icons={"Natural Products Explorer":"🌿","PROTAC Explorer":"🧬","Experimental Data Explorer":"📊","Molecular Docking":"⚛️","Linker Optimization":"🔗","Research Consultation":"🧪"}
    for start in range(0,len(names),3):
        cols=st.columns(3)
        for col,name in zip(cols,names[start:start+3]):
            with col:
                st.markdown(f'<div class="card"><h3>{icons[name]} {name}</h3><p>{SERVICES[name]}</p></div>',unsafe_allow_html=True)
                st.caption("Choose this page from the sidebar to open the service.")
    st.subheader("Platform areas")
    x,y,z=st.columns(3)
    x.markdown('<div class="card"><h4>🔬 Scientific workspace</h4><p>Explore compounds, experimental evidence, structures, and computational workflows.</p></div>',unsafe_allow_html=True)
    y.markdown('<div class="card"><h4>🤝 Research services</h4><p>Submit a consultation or propose a research collaboration.</p></div>',unsafe_allow_html=True)
    z.markdown('<div class="card"><h4>🗂️ Request management</h4><p>Planned user and admin portals for requests, progress, deliverables, and payments.</p></div>',unsafe_allow_html=True)
    st.subheader("Scientific safeguards")
    x,y,z=st.columns(3); x.info("Natural origin does not by itself prove anticancer activity or therapeutic efficacy."); y.info("Docking scores are computational outputs, not proof of binding or degradation."); z.info("IC50, Ki, Kd, DC50, and Dmax are distinct measurements and must not be conflated.")
