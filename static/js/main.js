var filedata = ""


async function button() {
    let [fileHandle] = await window.showOpenFilePicker();
    let fileData = await fileHandle.getFile();
    filedata = await fileData.text();
    document.getElementById("FileName").value = fileData.name;
    //console.log(fileData.name, typeof (fileData.name))
}

if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
        navigator.serviceWorker
            .register("/Chanting_Techniques/serviceWorker.js", {scope: '/Chanting_Techniques/'})
            .then(res => console.log("service worker registered"))
            .catch(err => console.log("service worker not registered", err));
    });
}