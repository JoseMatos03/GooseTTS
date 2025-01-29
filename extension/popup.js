document.getElementById("play-btn").addEventListener("click", async () => {
  const text = document.getElementById("text-input").value.trim();
  if (!text) {
    alert("Please enter some text!");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:5000/tts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    if (!response.ok) {
      const errorMessage = await response.json();
      console.error("Error:", errorMessage);
      throw new Error(errorMessage.error || "Failed to fetch audio.");
    }

    const blob = await response.blob();
    const audioUrl = URL.createObjectURL(blob);

    // Play the audio
    const audio = new Audio(audioUrl);
    audio.play();
  } catch (error) {
    console.error(error);
    alert("An error occurred: " + error.message);
  }
});
