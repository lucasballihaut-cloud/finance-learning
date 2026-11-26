import random

import pandas as pd
import streamlit as st

import progression as prog
import quiz_engine as qe
from ui import module_picker, score_color

module = module_picker()
data = prog.load()
questions = {q["id"]: q for q in module["quiz"]}

st.title(f"✅ Quiz — {module['titre']}")

missed = prog.missed_questions(data, module["id"])
best = prog.best_score(data, module["id"])
c1, c2, c3 = st.columns(3)
c1.metric("Questions dans le module", len(questions))
c2.metric("Meilleur score", f"{best:.0%}" if best is not None else "—")
c3.metric("Questions à revoir", len(missed))

# ---------- Lancer un quiz ----------
with st.sidebar:
    st.subheader("Nouveau quiz")
    mode = st.radio("Questions", ["Tout le module", "Seulement mes erreurs"],
                    disabled=not missed, help="« Mes erreurs » = questions ratées lors de ta dernière tentative.")
    n = st.slider("Nombre de questions", 3, len(questions), min(10, len(questions)))
    start = st.button("🎲 Lancer un nouveau quiz", type="primary", width="stretch")

quiz = st.session_state.get("quiz")
if start or quiz is None or quiz["module"] != module["id"]:
    ids = [q["id"] for q in qe.pick_questions(
        module["quiz"], n, missed if mode == "Seulement mes erreurs" and missed else None)]
    quiz = {"module": module["id"], "ids": ids, "nonce": random.randint(0, 10 ** 9), "result": None}
    st.session_state["quiz"] = quiz

st.caption("Pour les réponses numériques, tu peux écrire « 7,88 » ou « 7.88 ». "
           "Les pourcentages s'écrivent sans le signe % (ex. −2,5 pour −2,5 %).")

# ---------- Formulaire ----------
if quiz["result"] is None:
    with st.form(f"quiz_form_{quiz['nonce']}"):
        answers = {}
        for i, qid in enumerate(quiz["ids"], 1):
            q = questions[qid]
            st.markdown(f"**Question {i}.** {q['question']}")
            if q["type"] == "qcm":
                answers[qid] = st.radio("Ta réponse", range(len(q["choix"])), index=None,
                                        format_func=lambda k, q=q: q["choix"][k],
                                        key=f"{quiz['nonce']}_{qid}", label_visibility="collapsed")
            else:
                answers[qid] = st.text_input("Ta réponse", key=f"{quiz['nonce']}_{qid}",
                                             placeholder="Ta réponse (nombre)", label_visibility="collapsed")
            st.divider()
        submitted = st.form_submit_button("📝 Valider mes réponses", type="primary")
    if submitted:
        score, details = qe.grade([questions[i] for i in quiz["ids"]], answers)
        prog.record_quiz(data, module["id"], score, len(quiz["ids"]), details)
        prog.save(data)
        quiz["result"] = {"score": score, "details": details, "answers": answers}
        st.rerun()

# ---------- Correction ----------
else:
    res = quiz["result"]
    total = len(quiz["ids"])
    pct = res["score"] / total
    st.subheader(f"{score_color(pct)} Score : {res['score']} / {total} ({pct:.0%})")
    if pct == 1:
        st.balloons()
    st.caption("Ton score est enregistré dans ta progression.")
    for i, qid in enumerate(quiz["ids"], 1):
        q, ok, ans = questions[qid], res["details"][qid], res["answers"].get(qid)
        with st.container(border=True):
            st.markdown(f"{'✅' if ok else '❌'} **Question {i}.** {q['question']}")
            if q["type"] == "qcm":
                given = q["choix"][ans] if ans is not None else "(pas de réponse)"
                good = q["choix"][q["reponse"]]
            else:
                given = ans if ans else "(pas de réponse)"
                good = f"{q['reponse']:g}".replace(".", ",")
            st.markdown(f"Ta réponse : {given}  \nBonne réponse : **{good}**")
            st.markdown(f"💡 {q['explication']}")
    if st.button("🔁 Recommencer avec de nouvelles questions", type="primary"):
        del st.session_state["quiz"]
        st.rerun()

# ---------- Historique ----------
attempts = [a for a in data["quiz"] if a["module"] == module["id"]]
if attempts:
    st.subheader("Historique de ce module")
    hist = pd.DataFrame([{"Date": a["date"].replace("T", " "), "Score (%)": round(100 * a["score"] / a["total"]),
                          "Bonnes réponses": f"{a['score']} / {a['total']}"} for a in attempts])
    st.line_chart(hist.set_index("Date")["Score (%)"])
    st.dataframe(hist.iloc[::-1], hide_index=True, width="stretch")
