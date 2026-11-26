import streamlit as st

import progression as prog
from contenu.brainteasers import BRAINTEASERS

st.title("🧠 Brainteasers")
st.caption("En entretien, on juge surtout le raisonnement : réfléchis à voix haute, pose tes hypothèses, "
           "vérifie l'ordre de grandeur. Essaie d'abord sans l'indice !")

data = prog.load()
niveaux = st.sidebar.multiselect("Niveau", ["Facile", "Moyen", "Difficile"], default=["Facile", "Moyen", "Difficile"])
resolus = sum(bool(data["brainteasers"].get(b["id"])) for b in BRAINTEASERS)
st.progress(resolus / len(BRAINTEASERS), text=f"Résolus : {resolus} / {len(BRAINTEASERS)}")


def save_solved(bid, key):
    data["brainteasers"][bid] = st.session_state[key]
    prog.save(data)


for b in BRAINTEASERS:
    if b["niveau"] not in niveaux:
        continue
    with st.container(border=True):
        done = bool(data["brainteasers"].get(b["id"]))
        st.markdown(f"#### {'✅' if done else '❓'} {b['titre']}  ·  *{b['niveau']}*")
        st.markdown(b["enonce"])
        c1, c2, c3 = st.columns(3)
        show_hint = c1.toggle("💡 Indice", key=f"hint_{b['id']}")
        show_sol = c2.toggle("📖 Solution", key=f"sol_{b['id']}")
        key = f"solved_{b['id']}"
        c3.checkbox("Je l'ai résolu seul", value=done, key=key, on_change=save_solved, args=(b["id"], key))
        if show_hint:
            st.info(b["indice"])
        if show_sol:
            st.success(f"**Réponse : {b['reponse']}**")
            st.markdown(b["solution"])
