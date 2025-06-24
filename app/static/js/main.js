const storyForm = document.getElementById('story-form');
const photoInput = document.getElementById('photo');
const fileNameSpan = document.getElementById('file-name');

const loadingSpinner = document.getElementById('loading-spinner');
const storyOutput = document.getElementById('story-output');
const storyText = document.getElementById('story-text');
const copyButton = document.getElementById('copy-button');

photoInput.addEventListener('change', () => {
    if (photoInput.files.length > 0) {
        fileNameSpan.textContent = photoInput.files[0].name;
        fileNameSpan.classList.remove('text-gray-300');
        fileNameSpan.classList.add('text-white', 'font-semibold');
    } else {
        fileNameSpan.textContent = 'Click to choose a file...';
        fileNameSpan.classList.add('text-gray-300');
        fileNameSpan.classList.remove('text-white', 'font-semibold');
    }
});

storyForm.addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(storyForm);

    loadingSpinner.classList.remove('hidden');
    storyOutput.classList.add('hidden');
    copyButton.classList.add('hidden');

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Something went wrong on the server.');
        }

        storyText.textContent = data.story;
        copyButton.classList.remove('hidden');

    } catch (error) {
        storyText.textContent = `Error: ${error.message}`;
    } finally {
        loadingSpinner.classList.add('hidden');
        storyOutput.classList.remove('hidden');
        storyOutput.scrollTop = 0;
    }
});

copyButton.addEventListener('click', () => {
    const textToCopy = storyText.textContent;

    const textArea = document.createElement('textarea');
    textArea.value = textToCopy;
    textArea.style.position = 'fixed';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();

    try {
        document.execCommand('copy');
        copyButton.textContent = 'Copied!';
        setTimeout(() => {
            copyButton.textContent = 'Copy';
        }, 2000);
    } catch (err) {
        console.error('Gagal menyalin teks: ', err);
        copyButton.textContent = 'Failed!';
        setTimeout(() => {
            copyButton.textContent = 'Copy';
        }, 2000);
    }

    document.body.removeChild(textArea);
});