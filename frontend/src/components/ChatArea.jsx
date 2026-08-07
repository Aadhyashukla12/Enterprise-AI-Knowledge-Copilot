import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
function ChatArea({ messages, isTyping }) {

  return (

    <div className="chat-area">

      {messages.length === 0 ? (

        <>
          <h2>Welcome 👋</h2>
          <p>Ask me anything about your uploaded documents.</p>
        </>

      ) : (

        <>

          {messages.map((msg, index) => (

            <div
              key={index}
              className={
                msg.sender === "user"
                  ? "user-message"
                  : "ai-message"
              }
            >

              {msg.sender === "ai" ? (

    <ReactMarkdown remarkPlugins={[remarkGfm]}>
        {msg.text}
    </ReactMarkdown>

) : (

     <p>{msg.text}</p>

)}

              {/* Show Sources */}

              {msg.sender === "ai" &&
                msg.sources &&
                msg.sources.length > 0 && (

                  <div className="source-box">

                    <strong>📄 Sources</strong>

                    {msg.sources.map((source, i) => (

                      <div key={i} className="source-item">

                        <p>
                          <strong>Document:</strong> {source.source}
                        </p>

                        <p>
                          <strong>Chunk:</strong> {source.chunk}
                        </p>

                      </div>

                    ))}

                  </div>

              )}

              <small>{msg.time}</small>

            </div>

          ))}

          {isTyping && (

            <div className="typing">
              🤖 AI is typing...
            </div>

          )}

        </>

      )}

    </div>

  );

}

export default ChatArea;