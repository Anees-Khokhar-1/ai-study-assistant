import React,{useState} from "react";
import {generateNotes} from "../api";
export default function NotesGenerator(){
  const [text,setText]=useState(""); const [notes,setNotes]=useState([]); const [loading,setLoading]=useState(false);
  async function gen(){ setLoading(true); try{ const r = await generateNotes(text); setNotes(r.notes||[]); }catch(e){ setNotes(["Error: " + (e?.response?.data?.error || e.message)]); } setLoading(false); }
  return (<div><h2>Notes Generator</h2><textarea value={text} onChange={e=>setText(e.target.value)} placeholder="Paste lecture text..." /><button className="primary" onClick={gen} disabled={loading}>{loading ? "..." : "Generate Notes"}</button><div className="result"><h4>Notes</h4><ul>{Array.isArray(notes)?notes.map((n,i)=>(<li key={i}>{n}</li>)) : <li>{notes}</li>}</ul></div></div>);
} 