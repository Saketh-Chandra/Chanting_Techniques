//let text = ''
var filedata = ""


async function button() {
    let [fileHandle] = await window.showOpenFilePicker();
    let fileData = await fileHandle.getFile();
    filedata = await fileData.text();
    document.getElementById("FileName").value = fileData.name;
    //console.log(fileData.name, typeof (fileData.name))
}