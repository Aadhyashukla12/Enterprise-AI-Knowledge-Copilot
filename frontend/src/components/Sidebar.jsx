function Sidebar({

    documents,

    chatHistory,

    handleUpload,

    handleDelete,

    isUploading

}) {

    return (

        <div className="sidebar">

            <h2>📚 Knowledge Base</h2>

            <label
    className={`upload-btn ${isUploading ? "uploading" : ""}`}
>

    {isUploading
        ? "⏳ Uploading..."
        : "📤 Upload PDF"}

    <input
        type="file"
        accept=".pdf"
        hidden
        onChange={handleUpload}
        disabled={isUploading}
    />

     </label>

            <br />

            {documents.length === 0 ? (

                <p className="no-documents">
                    No documents uploaded.
                </p>

            ) : (

                documents.map((doc, index) => (

                    <div
                        key={index}
                        className="document-card"
                    >

                        <div className="document-info">

                            <span className="pdf-icon">
                                📄
                            </span>

                            <span
                                className="doc-name"
                                title={doc}
                            >
                                {doc}
                            </span>

                        </div>

                        <button
                            className="delete-btn"
                            onClick={() => handleDelete(doc)}
                            title="Delete Document"
                        >
                            🗑️
                        </button>

                    </div>

                ))

            )}

            <hr />

<h3 className="history-title">
    💬 Chat History
</h3>

{chatHistory.length === 0 ? (

    <p className="no-documents">
        No chats yet.
    </p>

) : (

    chatHistory.map((chat, index) => (

        <div
            key={index}
            className="history-card"
        >

            {chat.length > 35
                ? chat.substring(0, 35) + "..."
                : chat}

        </div>

    ))

)}

<hr />

<div className="sidebar-menu">

    <div className="menu-item">
        ⚙️ Settings
    </div>

</div>

</div>

);

}

export default Sidebar;