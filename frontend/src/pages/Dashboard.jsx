import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import ChatArea from "../components/ChatArea";
import MessageInput from "../components/MessageInput";

function Dashboard({

    documents,

    chatHistory,

    messages,

    input,

    setInput,

    handleSend,

    handleUpload,

    handleDelete,

    isTyping,

    isUploading,
    

}) {

    return (

        <div>

            <Navbar />

            <div className="main-container">

              <Sidebar
                 documents={documents}
                 chatHistory={chatHistory}
                 handleUpload={handleUpload}
                 handleDelete={handleDelete}
                 isUploading={isUploading}

/>
                <div className="chat-container">

                    <ChatArea
                        messages={messages}
                        isTyping={isTyping}
                    />

                    <MessageInput
                        input={input}
                        setInput={setInput}
                        handleSend={handleSend}
                    />

                </div>

            </div>

        </div>

    );

}

export default Dashboard;