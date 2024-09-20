document.querySelectorAll(".copy").forEach(copyButton => {
    copyButton.addEventListener("click", () => {
        const textToCopy = document.getElementById("initial_text");
        textToCopy.setSelectionRange(0, 99999);

        navigator.clipboard.writeText(textToCopy.value).then(() => {
            const buttonIcon = document.getElementById("copyIcon");

            copyButton.active = true;
            buttonIcon.textContent = "check";
            document.getElementById("copyButton").innerHTML = '<span class="material-symbols-outlined" id="checkIcon">check</span>'

            setTimeout(() => {
                buttonIcon.textContent = "content_copy"
                document.getElementById("copyButton").innerHTML = '<span class="material-symbols-outlined" id="copyIcon">content_copy</span>'
            }, 1500);
        });
    });
});


document.querySelectorAll(".delete").forEach(clearButton => {
    clearButton.addEventListener("click", () => {
        const textArea = document.getElementById("initial_text");
        textArea.value = "";
    });
});