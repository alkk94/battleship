function setFieldValue(id, row, col) {
    if (gameBoard[row][col] === 0 || gameBoard[row][col] === 1) {
        if (gameBoard[row][col] === 0) {
            document.getElementById(id).classList.add('miss');
            document.getElementById('trial-shoot').innerHTML = "Miss"
        } else if (gameBoard[row][col] === 1) {
            document.getElementById(id).classList.add('spot-on');
            document.getElementById('trial-shoot').innerHTML = "Down"
        }
        gameBoard[row][col] = 2;
        trialCounter++;
        document.getElementById('trial-counter').innerHTML = "Number of tries " + trialCounter;
    }
}