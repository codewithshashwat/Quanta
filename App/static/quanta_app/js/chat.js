document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (!message) return;

        // Display user message in the chat box
        appendMessage(message, 'user');

        // Clear the input field
        userInput.value = '';

        try {
            // Send the message to the Django backend
            const response = await fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            // Display bot's response
            appendMessage(data.reply, 'bot');

        } catch (error) {
            console.error("Error:", error);
            appendMessage("Sorry, I'm having trouble connecting right now. Please try again later.", 'bot');
        }
    });

    function appendMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);
        messageDiv.textContent = text;
        chatBox.appendChild(messageDiv);
        
        // Scroll to the latest message
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});