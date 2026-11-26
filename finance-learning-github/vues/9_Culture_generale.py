import random

import pandas as pd
import streamlit as st

import progression as prog
from contenu import culture as c

st.title("🌍 Culture générale")
st.caption(f"Données vérifiées le **{c.DATE_MAJ}**. Capitalisations et dirigeants changent : revérifie avant un entretien.")

tabs = st.tabs(["🏢 Capitalisations", "🏦 Banques centrales", "📈 Indices", "🏛️ Institutions et devises", "✅ Quiz"])

with tabs[0]:
    st.subheader("Les 15 plus grandes capitalisations mondiales")
    st.dataframe(pd.DataFrame(c.MONDE, columns=["Rang", "Entreprise", "Pays", "Capitalisation (Md$)", "Secteur"]),
                 hide_index=True, width="stretch")
    st.subheader("Par continent et par pays (top 5)")
    zone = st.pills("Continent", list(c.PAR_ZONE), default="Europe")
    for pays, top in c.PAR_ZONE.get(zone or "Europe", []):
        st.markdown(f"**{pays}**")
        st.dataframe(pd.DataFrame([(i + 1, n, v) for i, (n, v) in enumerate(top)],
                                  columns=["Rang", "Entreprise", "Capitalisation (Md$)"]), hide_index=True, width="stretch")

with tabs[1]:
    cont = st.pills("Continent ", sorted({b[0] for b in c.BANQUES_CENTRALES}), default="Europe")
    for b in c.BANQUES_CENTRALES:
        if b[0] == cont:
            with st.container(border=True):
                st.markdown(f"**{b[2]}** — {b[1]}  \n👤 {b[4]} : **{b[3]}** (depuis {b[5]})  \n🎯 Cible d'inflation : {b[6]}")
                if b[7]:
                    st.caption(b[7])

with tabs[2]:
    st.dataframe(pd.DataFrame(c.INDICES, columns=["Pays", "Indice", "Composition"]), hide_index=True, width="stretch")

with tabs[3]:
    st.subheader("Institutions internationales")
    st.dataframe(pd.DataFrame(c.INSTITUTIONS, columns=["Institution", "Siège", "Dirigeant", "Rôle"]),
                 hide_index=True, width="stretch")
    st.subheader("Devises et codes ISO")
    st.dataframe(pd.DataFrame(c.DEVISES, columns=["Pays", "Devise", "Code"]), hide_index=True, width="stretch")
    st.subheader("Sources")
    for label, url in c.SOURCES:
        st.markdown(f"- [{label}]({url})")


def make_questions(rng, n=10):
    qs = []
    banks = c.BANQUES_CENTRALES
    for b in rng.sample(banks, 4):
        wrong = rng.sample([x[3] for x in banks if x[3] != b[3]], 3)
        qs.append((f"Qui dirige la **{b[2]}** ({b[1]}) ?", b[3], wrong))
    countries = [(p, top) for zone in c.PAR_ZONE.values() for p, top in zone if p != "Union européenne"]
    for p, top in rng.sample(countries, 3):
        others = rng.sample([t[0][0] for q, t in countries if q != p], 3)
        qs.append((f"Quelle est la plus grande capitalisation boursière de **{p}** ?", top[0][0], others))
    for code_q in rng.sample(c.DEVISES, 2):
        wrong = rng.sample([d[2] for d in c.DEVISES if d != code_q], 3)
        qs.append((f"Quel est le code ISO de la devise **{code_q[1]}** ?", code_q[2], wrong))
    first = c.MONDE[0][1]
    qs.append(("Quelle est la première capitalisation boursière mondiale ?", first,
               rng.sample([m[1] for m in c.MONDE[1:8]], 3)))
    rng.shuffle(qs)
    return [(q, good, rng.sample([good] + wrong, 4)) for q, good, wrong in qs[:n]]


with tabs[4]:
    if st.button("🎲 Nouveau quiz de culture générale", type="primary") or "culture_quiz" not in st.session_state:
        st.session_state["culture_quiz"] = {"qs": make_questions(random.Random()), "done": None,
                                            "nonce": random.randint(0, 10 ** 9)}
    quiz = st.session_state["culture_quiz"]
    with st.form(f"culture_{quiz['nonce']}"):
        answers = [st.radio(q, options, index=None, key=f"cq_{quiz['nonce']}_{i}")
                   for i, (q, good, options) in enumerate(quiz["qs"])]
        if st.form_submit_button("📝 Valider") and quiz["done"] is None:
            details = {f"culture-{i}": a == q[1] for i, (q, a) in enumerate(zip(quiz["qs"], answers))}
            data = prog.load()
            prog.record_quiz(data, "culture", sum(details.values()), len(details), details)
            prog.save(data)
            quiz["done"] = (sum(details.values()), answers)
    if quiz["done"]:
        score, answers = quiz["done"]
        st.subheader(f"Score : {score} / {len(quiz['qs'])}")
        for (q, good, _), a in zip(quiz["qs"], answers):
            st.markdown(f"{'✅' if a == good else '❌'} {q} → **{good}**")
