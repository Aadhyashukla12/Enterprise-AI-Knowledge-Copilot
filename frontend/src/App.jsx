import { useEffect, useState } from "react";
import "./App.css";
import Dashboard from "./pages/Dashboard";
const API_BASE = "http://127.0.0.1:8001";
function App() {

    const [documents, setDocuments] = useState([]);
    const [messages, setMessages] = useState([]);
    const [chatHistory, setChatHistory] = useState([]);
    const [input, setInput] = useState("");
    const [isTyping, setIsTyping] = useState(false);
    const [isUploading, setIsUploading] = useState(false);

    async function fetchDocuments() {

        try {

            const response = await fetch(`${API_BASE}/documents`);

            const data = await response.json();

            setDocuments(data.documents);

        } catch (error) {

            console.log(error);

        }

    }
    async function handleUpload(event) {

    const file = event.target.files[0];

    if (!file) return;
    setIsUploading(true);
    const formData = new FormData();

    formData.append("file", file);

    try {
          const response = await fetch(`${API_BASE}/upload`, 
       {
           method: "POST",
           body: formData
       }
       );
          console.log("Status:", response.status);
          console.log("OK:", response.ok);
        const data = await response.json();
        console.log("Response:", data);

        alert(data.message);

        // Refresh sidebar
        fetchDocuments();

    } catch (error) {

        console.error(error);

        alert("Upload failed.");

    }
    finally {

    setIsUploading(false);

}
    

}
async function handleDelete(filename) {

    const confirmDelete = window.confirm(
        `Delete "${filename}"?`
    );

    if (!confirmDelete) return;

    try {

        const response = await fetch(`${API_BASE}/delete`,
            {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    filename
                })
            }
        );

        const data = await response.json();

        alert(data.message);

        fetchDocuments();

    } catch (error) {

        console.log(error);

        alert("Delete failed.");

    }

}
    useEffect(() => {

        fetchDocuments();

    }, []);

  async function handleSend() {

    if (input.trim() === "") return;

    const userMessage = input;

    // Store question in chat history
    setChatHistory(prev => [
        ...prev,
        userMessage
    ]);

    // Show user message
    setMessages(prev => [
        ...prev,
        {
            sender: "user",
            text: userMessage,
            time: new Date().toLocaleTimeString([], {
                hour: "2-digit",
                minute: "2-digit"
            })
        }
    ]);

    setInput("");
    setIsTyping(true);

    try {

        const response = await fetch(`${API_BASE}/chat`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: userMessage
                })
            }
        );

        const data = await response.json();

        // Show AI response
        setMessages(prev => [
            ...prev,
            {
                sender: "ai",
                text: data.response,
                sources: data.sources || [],
                time: new Date().toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit"
                })
            }
        ]);

    } catch (error) {

        console.error(error);

        setMessages(prev => [
            ...prev,
            {
                sender: "ai",
                text: "Unable to connect to the backend.",
                time: new Date().toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit"
                })
            }
        ]);

    } finally {

        setIsTyping(false);

    }

}
    

    return (

  <Dashboard
    documents={documents}
    chatHistory={chatHistory}
    messages={messages}
    input={input}
    setInput={setInput}
    handleSend={handleSend}
    handleUpload={handleUpload}
    handleDelete={handleDelete}
    isTyping={isTyping}
    isUploading={isUploading}
/>

);
}

export default App;