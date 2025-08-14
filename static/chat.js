function sendMessage() {
    let input = document.getElementById('userInput').value;
    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('chatbox').innerHTML +=
          `<p>You: ${input}</p><p>Bot: ${data.reply}</p>`;
        document.getElementById('userInput').value = '';
    });
}
