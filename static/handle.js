function setFieldValue(id, isShip) {
    if (isShip === 1) {
        document.getElementById(id).classList.add('spot-on');
    } else {
        document.getElementById(id).innerHTML='miss';
    }
    trial_counter++;
    document.getElementById('trial-counter').innerHTML = "Number of tries " + trial_counter;
}