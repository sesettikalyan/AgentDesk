import '../styles/InputBar.css'

function InputBar({ input, setInput, sendMessage }) {
  return (
    <div className="input-area">
      <div className="input-wrapper">
        <input
          type="text"
          placeholder="Type a message..."
          className="message-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button className="send-btn" onClick={sendMessage}>➤</button>
      </div>
    </div>
  )
}

export default InputBar