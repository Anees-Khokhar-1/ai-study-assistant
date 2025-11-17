import React,{useState} from "react";
import {generateMCQs} from "../api";
export default function MCQGenerator(){
  const [text,setText]=useState(""); const [mcqs,setMcqs]=useState([]); const [loading,setLoading]=useState(false);
  async function generate(){ setLoading(true); try{ const r = await generateMCQs(text); setMcqs(r.mcq||[]); }catch(e){ setMcqs([{question:"Error: " + (e?.response?.data?.error || e.message)}]); } setLoading(false); }
  return (<div><h2>MCQ Generator</h2><textarea value={text} onChange={e=>setText(e.target.value)} placeholder="Paste lecture text..." /><button className="primary" onClick={generate} disabled={loading}>{loading?"...":"Generate MCQs"}</button><div className="result"><h4>MCQs</h4><ul>{mcqs.map((m,i)=>(<li key={i}><strong>{m.question}</strong><div>Options: {Array.isArray(m.options)?m.options.join(", "):m.options}</div></li>))}</ul></div></div>);
} 