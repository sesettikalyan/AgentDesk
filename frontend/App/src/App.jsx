import { useState } from 'react'
import Sidebar from './Components/Sidebar'
import ChatWindow from './Components/ChatWindow'
import InputBar from './Components/Inputbar'
import './App.css'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState("")
  const [loading, setLoading] = useState(false)

  async function sendMessage() {
    if (input.trim() === "") return

    const newMessages = [...messages, { id: Date.now(), sender: "user", text: input }]
    setMessages(newMessages)
    setInput("")
    setLoading(true)

    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input })
    })

    const data = await response.json()

    setMessages([...newMessages, { id: Date.now() + 1, sender: "bot", text: data.reply }])
    setLoading(false)
  }

  return (
    <div className="app">
      <Sidebar />
      <div className="main">
        <ChatWindow messages={messages} loading={loading} />
        <InputBar input={input} setInput={setInput} sendMessage={sendMessage} />
      </div>
    </div>
  )
}

export default App