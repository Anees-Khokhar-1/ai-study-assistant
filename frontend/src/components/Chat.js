import React,{useState} from "react";
import {chatWithAI} from "../api";
export default function Chat(){
  const [msg,setMsg]=useState(""); const [reply,setReply]=useState(""); const [loading,setLoading]=useState(false);
  async function send(){ setLoading(true); try{ const r = await chatWithAI(msg); setReply(r.reply||JSON.stringify(r)); }catch(e){ setReply("Error: " + (e?.response?.data?.error || e.message)); } setLoading(false); }
  return (<div><h2>Chat</h2><input style={{width:"80%",padding:8}} value={msg} onChange={e=>setMsg(e.target.value)} placeholder="Ask..."/><button className="primary" onClick={send} disabled={loading} style={{marginLeft:8}}>{loading?"...":"Send"}</button><div className="result"><h4>Reply</h4><div>{reply}</div></div></div>);
}
