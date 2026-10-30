import '../styles/ChatWindow.css'
import MessageBubble from './MessageBubble'

function ChatWindow({ messages, loading }) {
  return (
    <>
      <div className="chat-header-bar">
        <div className="header-bot-info">
          <div className="header-avatar">
            AI
            <div className="header-online-dot"></div>
          </div>
          <div>
            <div className="header-name">Support Agent</div>
            <div className="header-active">● Active now</div>
          </div>
        </div>
      </div>

      <div className="chat-window">
        <div className="date-divider">
          | <hr /><span>Today</span><hr />
        </div>

        {messages.map(({ id, sender, text }) => (
          <MessageBubble key={id} sender={sender} text={text} />
        ))}

        {loading && <MessageBubble sender="bot" text="Thinking..." />}
      </div>
    </>
  )
}

export default ChatWindow