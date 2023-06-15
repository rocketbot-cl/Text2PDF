# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import traceback
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Text2PDF" + os.sep + "libs" + os.sep
sys.path.append(cur_path)
from txt_to_pdf_service import TxtToPdfService

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")
global txt_to_pdf_service

try:
    if module == "openTxt":
        path_txt = GetParams("path")
        if not path_txt:
            raise Exception("No se cargo el archivo TXT")
        try:
            txt_to_pdf_service = TxtToPdfService()
            txt_to_pdf_service.open_txt(path_txt)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e

    if module == "setFont":
        font_family = GetParams("font_family") if GetParams("font_family") else 'Arial'
        font_style = GetParams("font_style") if GetParams("font_style") else ''
        font_size = int(GetParams("font_size")) if GetParams("font_size") else 12

        try:
            data_font = {
                "family": font_family,
                "style": font_style,
                "size": font_size
            }
            txt_to_pdf_service.set_font(data_font)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e

    if module == "savePdf":
        path_pdf = GetParams("path_pdf")
        line_height = GetParams("line_height") if GetParams("line_height") else 10

        if not path_pdf:
            raise Exception("No se eligio destino del PDF")

        try:
            txt_to_pdf_service.write_into_pdf(path_pdf, line_height)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e
            
except Exception as e:
    PrintException()
    traceback.print_exc()
    raise e