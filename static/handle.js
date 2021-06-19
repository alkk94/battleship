function setFieldValue(id, isShip) {
    if (isShip === 1) {
        document.getElementById(id).classList.add('spot-on');
    } else {
        document.getElementById(id).innerHTML='miss';
    }
}