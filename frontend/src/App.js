import axios from "axios";
export async function summarizeText(text){ const res = await axios.post("/summarize", {text}); return res.data; }
export async function chatWithAI(message){ const res = await axios.post("/chat", {message}); return res.data; }
export async function generateMCQs(text){ const res = await axios.post("/mcq", {text}); return res.data; }
export async function generateNotes(text){ const res = await axios.post("/notes", {text}); return res.data; }
export async function uploadPDF(formData){ const res = await axios.post("/api/upload", formData, { headers: { "Content-Type": "multipart/form-data" } }); return res.data; }
