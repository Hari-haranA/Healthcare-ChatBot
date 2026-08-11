const sendButton = document.getElementById('send-button');
const userInput = document.getElementById('user-input');
const chatWindow = document.querySelector('.chat-window');

sendButton.addEventListener('click', function() {
    // Process user input here (e.g., using NLTK)
    const userText = userInput.value;
    userInput.value = '';

    // Create a new chat bubble for the user
    const userBubble = document.createElement('div');
    userBubble.classList.add('chat-bubble', 'user');
    userBubble.textContent = userText;
    chatWindow.appendChild(userBubble);

    // Simulate a response from the avatar (replace with actual logic)
    const avatarBubble = document.createElement('div');
    avatarBubble.classList.add('chat-bubble', 'avatar');