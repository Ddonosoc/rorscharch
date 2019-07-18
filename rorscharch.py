import datetime
import csv

Laminas = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
determinantes = ["F", "M", "FM", "m", "Fm", "mF", "FC", "CF", "C", "FK", "KF", "K", "FC\'", "C\'F", "C\'", "Fc", "cF",
                 "c", "Fk", "kF", "k"]
determinantes_con_cal = ["F", "FM", "Fm", "FC", "FK", "FC\'", "Fc", "Fk", "M"]
LOCs = ["G", "G+", "Go", "Gv", "G-", "G/", "(G)", "DG", "GS", "DG", "Do", "DS", "Dd", "Ddi", "Dde", "Ddd"]
calidad_formal = ["+", "-", "W+", "W-", "O", "V", "S"]

contenidos = ["H", "(H)", "Hd", "(Hd)", "A", "(A)", "Ad", "(Ad)", "Obj A", "Ab", "An", "(At)", "Antr", "San", "Veg",
              "Rp", "Nb", "Ex", "Fg", "Com", "Geo", "Hg", "Psj", "Na", "Sx", "Rx", "(Vo)", "Obj"]

categorias = {"grupo a": {"0": "Frase 1", "1": "Frase 2", "2": "Frase 3"},
              "grupo b": {"0": "Frase 4", "1": "Frase 5", "2": "Frase 6"}}


def test_r():
    print("------------------------------------------------------------")
    print("                 TEST DE RORSCHARCH")
    print("------------------------------------------------------------")
    Info = []
    nombre = input("Ingresa nombre de persona, si tiene espacios, reemplazalos por un _:\n")

    for lamina in Laminas:
        print("------------------------------------------------------------")
        print("Lámina: " + lamina)
        print("------------------------------------------------------------")
        respuestas = try_a_number("Ingresa numero de respuestas:\n")
        info_lamina = []

        if respuestas == 0:
            continue
        for k in range(respuestas):
            print("------------------------------------------------------------")
            print("Respuesta n°: " + str(k + 1))
            print("------------------------------------------------------------")
            LOC = do_loop("Ingresa LOC, tus opciones son: \n", LOCs)
            determinante = do_loop(
                "Ingresa determinante, si lleva \', antes de la comilla poner un backslash (\\), tus "
                "opciones son: \n", determinantes)
            # Comprobar determinante
            calidad_formal_input = ""
            if determinante in determinantes_con_cal:
                calidad_formal_input = do_loop(
                    "Ingresa calidad formal, tus opciones son: \n", calidad_formal)
            contenido = do_loop("Ingresa contenido, tus opciones son: \n", contenidos)
            n_fenomenos = try_a_number("Ingresa número de fenómenos:\n")
            fenomenos_list = []
            for l in range(int(n_fenomenos)):
                print("Fenómeno n°: " + str(l + 1))
                fenomeno = parte_fenomenos()
                fenomenos_list.append(fenomeno)
            info_lamina.append([LOC, determinante, calidad_formal_input, contenido, fenomenos_list])
        Info.append(info_lamina)

    fecha = datetime.date.today()

    with open(nombre + str(fecha) + '.csv', 'w', encoding='ISO-8859-1', newline='') as tsvfile1:
        writer = csv.writer(tsvfile1, delimiter=';')
        writer.writerow(['Lamina', 'N° resp', 'Loc', 'DET', 'C. F.', 'Cont', 'N° F.', 'F. especial'])
        # Por cada lamina
        for i in range(len(Info)):
            # Por cada respuesta
            for j in range(len(Info[i])):
                loc = Info[i][j][0]
                det = Info[i][j][1]
                cal = Info[i][j][2]
                cont = Info[i][j][3]
                if len(Info[i][j][4]) == 0:
                    writer.writerow([Laminas[i], j + 1, loc, det, cal, cont])
                for r in range(len(Info[i][j][4])):
                    fen = Info[i][j][4][r]
                    writer.writerow([Laminas[i], j + 1, loc, det, cal, cont, r + 1, fen])
    print("------------------------------------------------------------")
    print("Se ha guardado el archivo " + nombre + str(fecha))
    print("------------------------------------------------------------")


def parte_fenomenos():
    print("Tipea help para obtener ayuda completa")
    flag = True
    final = ""
    while flag:
        value = input("Ingresa un comando: \n")
        value_list = value.split()
        if value_list[0] == "help" and len(value_list) == 1:
            print("En esta sección debes ingresar un comando que sea del tipo \'help\', \'help grupo\', \'agregar"
                  "\' [grupo] [fenomeno]\', \'[grupo] [fenomeno]")
            print(categorias)
        elif value_list[0] == "help" and len(value_list) > 1:
            print("A continuación se imprimirán los valores del grupo " + value_list[2])
            print(categorias[value_list[1] + " " + value_list[2]])
        elif value_list[0] == "agregar":
            key = value_list[1] + value_list[2]
            string_value = value_list[3:]
            if key not in categorias:
                categorias[key]["0"] = string_value
            else:
                length = len(categorias[key])
                categorias[key][str(length)] = string_value
        elif value_list[0] == "grupo":
            try:
                dict_vals = categorias[value_list[0] + " " + value_list[1]]
                print(dict_vals)
                val_cat = value_list[2]
                final = dict_vals[val_cat]
                flag = False
            except:
                print("Error, opción ingresada no es válida, intenta nuevamente")
                continue
        else:
            print("Error, opción ingresada no es válida, intenta nuevamente")
    return final


def get_options(option):
    final = ""
    for val in option:
        final += val + " "
    final += "\n"
    return final


def try_a_number(msg):
    flag = True
    final = -1
    while flag:
        numb = input(msg)
        try:
            int(numb)
        except:
            print("Error, opción ingresada no es válida, intenta nuevamente")
            continue
        flag = False
        final = int(numb)
    return final


def do_loop(msg, options):
    flag = True
    final = ""
    while flag:
        option = input(msg + get_options(options))
        if not check(option, options):
            print("Error, opción ingresada no es válida, intenta nuevamente")
        else:
            flag = False
            final = option
    return final


def check(option, options):
    if option in options:
        return True
    else:
        return False


if __name__ == '__main__':
    test_r()
