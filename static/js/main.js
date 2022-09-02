var filedata = ""


function readfile(input) {
    let textfile = input.files[0];
    let reader = new FileReader();
    reader.readAsText(textfile);
    reader.onload = function () {
        filedata = reader.result;
    };
    reader.onerror = function () {
        console.log(reader.error);
    };

}

if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
        navigator.serviceWorker
            .register("/Chanting_Techniques/serviceWorker.js", {scope: '/Chanting_Techniques/'})
            .then(res => console.log("service worker registered"))
            .catch(err => console.log("service worker not registered", err));
    });
}