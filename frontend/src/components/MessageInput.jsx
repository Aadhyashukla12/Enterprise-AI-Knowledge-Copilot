function MessageInput({

  input,
  setInput,
  handleSend

}) {

  return (

    <div className="message-input">

      <input
        type="text"
        value={input}
        placeholder="Type your message..."
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => {

          if (e.key === "Enter") {
            handleSend();
          }

        }}
      />

      <button onClick={handleSend}>
        Send
      </button>

    </div>

  );

}

export default MessageInput;