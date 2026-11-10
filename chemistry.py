"""Optional RDKit-backed chemistry utilities; absence is reported explicitly."""
from __future__ import annotations


def rdkit_available() -> bool:
    try:
        import rdkit  # noqa: F401
        return True
    except ImportError:
        return False


def describe_smiles(smiles: str) -> dict[str, object]:
    """Calculate basic structure descriptors; never treats them as activity predictions."""
    try:
        from rdkit import Chem
        from rdkit.Chem import Descriptors, rdMolDescriptors
    except ImportError as exc:
        raise RuntimeError("RDKit is not installed in this environment.") from exc
    molecule = Chem.MolFromSmiles(smiles.strip())
    if molecule is None:
        raise ValueError("The SMILES string could not be parsed by RDKit.")
    return {
        "canonical_smiles": Chem.MolToSmiles(molecule),
        "molecular_weight": round(Descriptors.MolWt(molecule), 3),
        "logp_estimate": round(Descriptors.MolLogP(molecule), 3),
        "tpsa": round(rdMolDescriptors.CalcTPSA(molecule), 3),
        "h_bond_donors": rdMolDescriptors.CalcNumHBD(molecule),
        "h_bond_acceptors": rdMolDescriptors.CalcNumHBA(molecule),
        "rotatable_bonds": rdMolDescriptors.CalcNumRotatableBonds(molecule),
        "interpretation": "Calculated physicochemical descriptors; not a prediction of anticancer activity or PROTAC efficacy.",
    }
