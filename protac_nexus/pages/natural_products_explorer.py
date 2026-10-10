import streamlit as st
import pandas as pd
from protac_nexus.integrations.providers import ProviderError, search_chembl, search_pubchem
from protac_nexus.integrations.chemistry import describe_smiles, rdkit_available
from protac_nexus.config.services import SERVICES
def render():
    page="Natural Products Explorer"; st.title(page); st.write(SERVICES[page])
    st.caption("PubChem provides compound identity/structure records; ChEMBL provides molecule records. These records alone do not establish anticancer efficacy.")
    query=st.text_input("Search compound name or identifier",placeholder="e.g. curcumin"); source=st.radio("Search source",["PubChem","ChEMBL","Both"],horizontal=True); limit=st.select_slider("Maximum records per source",options=[5,10,20],value=10)
    if st.button("Search public databases",type="primary",disabled=not query.strip()):
        with st.spinner("Searching selected public source(s)…"):
            if source in ("PubChem","Both"):
                try:
                    records=search_pubchem(query,limit)
                    if records: st.subheader("PubChem results"); st.dataframe(pd.DataFrame(records),use_container_width=True,hide_index=True,column_config={"source_url":st.column_config.LinkColumn("Source record")})
                    else: st.info("No matching PubChem compound records were returned.")
                except ProviderError as exc: st.warning(f"PubChem could not be reached: {exc}")
            if source in ("ChEMBL","Both"):
                try:
                    records=search_chembl(query,limit)
                    if records: st.subheader("ChEMBL molecule results"); st.dataframe(pd.DataFrame(records),use_container_width=True,hide_index=True,column_config={"source_url":st.column_config.LinkColumn("Source record")})
                    else: st.info("No matching ChEMBL molecule records were returned.")
                except ProviderError as exc: st.warning(f"ChEMBL could not be reached: {exc}")
    with st.expander("Check a SMILES structure with RDKit"):
        smiles=st.text_input("SMILES",key="rdkit_smiles",placeholder="Paste a SMILES string")
        if not rdkit_available(): st.info("RDKit is optional and is not installed in this deployment yet.")
        elif st.button("Validate structure and calculate descriptors"):
            try: st.json(describe_smiles(smiles))
            except (ValueError,RuntimeError) as exc: st.error(str(exc))
