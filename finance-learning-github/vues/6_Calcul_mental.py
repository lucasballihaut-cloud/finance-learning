import random
import time

import pandas as pd
import streamlit as st

import calcul
import progression as prog
import quiz_engine as qe

st.title("⏱️ Calcul mental")
st.caption("Les tests en ligne des banques (et les traders en entretien) demandent des calculs rapides "
           "et justes, sans calculatrice. Vise la précision d'abord, la vitesse ensuite.")

data = prog.load()
session = st.session_state.get("calc")

if session is None:
    c1, c2 = st.columns(2)
    kind = c1.selectbox("Type d'exercice", list(calcul.TYPES), format_func=calcul.TYPES.get)
    n = c2.select_slider("Nombre de calculs", [5, 10, 20, 30], value=10)
    if st.button("▶️ Démarrer", type="primary"):
        st.session_state["calc"] = {"kind": kind, "items": calcul.series(kind, n, seed=random.random()),
                                    "i": 0, "good": 0, "start": time.time(), "log": [], "saved": False}
        st.rerun()
else:
    items, i = session["items"], session["i"]
    if i < len(items):
        enonce, reponse, tol = items[i]
        st.progress(i / len(items), text=f"Calcul {i + 1} / {len(items)} · bonnes réponses : {session['good']}")
        with st.form(f"calc_{i}", clear_on_submit=True):
            st.markdown(f"## {enonce} = ?")
            ans = st.text_input("Réponse", key=f"calc_ans_{i}")
            if st.form_submit_button("Valider (Entrée)", type="primary"):
                ok = qe.is_correct({"type": "nombre", "reponse": reponse, "tolerance": tol}, ans)
                session["good"] += ok
                session["log"].append({"Calcul": enonce, "Ta réponse": ans,
                                       "Bonne réponse": round(reponse, 4), "": "✅" if ok else "❌"})
                session["i"] += 1
                st.rerun()
        if st.button("⏹️ Abandonner"):
            del st.session_state["calc"]
            st.rerun()
    else:
        if not session["saved"]:
            session["elapsed"] = time.time() - session["start"]
            prog.record_calcul(data, session["kind"], session["good"], len(items), session["elapsed"])
            prog.save(data)
            session["saved"] = True
        c1, c2, c3 = st.columns(3)
        c1.metric("Score", f"{session['good']} / {len(items)}")
        c2.metric("Temps total", f"{session['elapsed']:.0f} s")
        c3.metric("Temps moyen", f"{session['elapsed'] / len(items):.1f} s / calcul")
        st.dataframe(pd.DataFrame(session["log"]), hide_index=True, width="stretch")
        if st.button("🔁 Nouvelle série", type="primary"):
            del st.session_state["calc"]
            st.rerun()

if data["calcul"]:
    st.subheader("Mes séries")
    hist = pd.DataFrame(data["calcul"])
    hist["Type"] = hist["type"].map(calcul.TYPES)
    hist["Score"] = hist["score"].astype(str) + " / " + hist["total"].astype(str)
    hist["s / calcul"] = (hist["secondes"] / hist["total"]).round(1)
    hist["Date"] = hist["date"].str.replace("T", " ")
    st.dataframe(hist[["Date", "Type", "Score", "s / calcul"]].iloc[::-1], hide_index=True, width="stretch")
