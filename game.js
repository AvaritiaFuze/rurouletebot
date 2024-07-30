document.getElementById('spinButton').addEventListener('click', function() {
    let revolver = document.getElementById('revolver');
    revolver.style.animation = 'spin 1s ease-out';
    setTimeout(() => {
        revolver.style.animation = '';
        let result = Math.random() < 1 / 6 ? 'BANG! You are banned!' : 'Click! You survived!';
        document.getElementById('result').textContent = result;
        if (result.includes('BANG')) {
            fetch('/ban', { method: 'POST' });
        }
    }, 1000);
});