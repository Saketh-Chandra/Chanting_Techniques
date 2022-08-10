from js import console
import dhandapatha
import dwajapatha
import ghanapatha
import jathapatha
import kramapatha
import malapatha
import rathapatha
import Rekhapatha
import sikhapatha


def call(line, type):
    if (type == "Ghanapatha"):
        return ghanapatha.ghanapatha(line)
    elif (type == "Jathapatha"):
        return jathapatha.jathapatha(line)
    elif (type == "Rekhapatha"):
        return Rekhapatha.rekhapatha(line)
    elif (type == "Kramapatha"):
        return kramapatha.kramapatha(line)
    elif (type == "Malapatha"):
        return malapatha.malapatha(line)
    elif (type == "Sikhapatha"):
        return sikhapatha.sikhapatha(line)
    elif (type == "Dwajapatha"):
        return dwajapatha.dwajapatha(line)
    elif (type == "Rathapatha"):
        return rathapatha.rathapatha(line)
    elif (type == "Dhandapatha"):
        return dhandapatha.dhandapatha(line)


output_element = Element("output")


def main(*args, **kwargs):
    from js import filedata
    output_element.element.innerText = ''
    try:
        option = Element("selecttpye").element.value
        if not filedata:
            raise Exception("Error: please Select File")
        if option == 'default':
            raise Exception("Error: please Select Chanting Type")

        output_data = "\n".join([" ".join(i) for i in call(filedata, option)])
    except Exception as e:
        output_data = str(e).title()
    finally:
        output_element.element.innerHTML = output_data
