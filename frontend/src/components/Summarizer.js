import React, {useState} from "react";
import {summarizeText, uploadPDF} from "../api";

export default function Summarizer(){
  const [input, setInput] = useState("");
  const [summary, setSummary] = useState("");
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleSummarize(){
    setLoading(true);
    try{
      const d = await summarizeText(input);
      setSummary(d.summary || "");
    }catch(e){ setSummary("Error: " + (e?.response?.data?.error || e.message)); }
    setLoading(false);
  }

  async function handleUpload(e){
    e.preventDefault();
    if(!file) return alert("Choose PDF");
    setLoading(true);
    const form = new FormData(); form.append("file", file);
    try{
      const r = await uploadPDF(form);
      setSummary(r.summary || "");
    }catch(err){ setSummary("Upload error: " + (err?.response?.data?.error || err.message)); }
    setLoading(false);
  }

  return (
    <div>
      <h2>Summarizer</h2>
      <textarea value={input} onChange={(e)=>setInput(e.target.value)} placeholder="Paste lecture text..." />
      <div style={{marginTop:8}}>
        <button className="primary" onClick={handleSummarize} disabled={loading}>{loading ? "Working..." : "Summarize"}</button>
      </div>
      <hr/>
      <h3>Or upload PDF</h3>
      <input type="file" accept="application/pdf" onChange={(e)=>setFile(e.target.files[0])} />
      <button className="primary" onClick={handleUpload} disabled={loading}>Upload & Summarize</button>
      <div className="result"><h4>Summary</h4><div>{summary}</div></div>
    </div>
  );
}
