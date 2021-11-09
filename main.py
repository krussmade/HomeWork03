import sys
import time
import container
from container import Container


if __name__ == '__main__':

    container = Container()
    file = open('inputTests/input3', 'r')
    # print(file.readlines())
    container.RandomFill(111)
    container.Print()

    # start = time.time()
    # # Проверка на корректность введенных данных
    # if len(sys.argv) == 5:
    #     if sys.argv[1] == "-f":
    #         inputFileName = sys.argv[2]
    #         outputFileName = sys.argv[3]
    #         outputSortedName = sys.argv[4]
    #     elif sys.argv[1] == "-n":
    #         number = int(sys.argv[2])
    #         outputFileName = sys.argv[3]
    #         outputSortedName = sys.argv[4]
    # else:
    #     print("Incorrect command line!\n"
    #           "    Waited:\n"
    #           "python main.py -f inputFileName outputFileName outputSortedFileName\n"
    #           "    Or:\n"
    #           "python main.py -n number outputFileName outputSortedFileName\n")
    #     exit()
    #
    # print('==> Start')
    # container = Container()
    # # Заполняем контейнер фигурами
    # if sys.argv[1] == "-f":
    #     ifile = open(inputFileName, 'r')
    #     figNum = container.FileFill(ifile)
    #     if figNum == -1:
    #         print("Unknown animals")
    #         exit()
    #     container.Print()
    #     ifile.close()
    # else:
    #     container.RandomFill(number)
    #
    # # Записываем данные контейнера в файл
    # ofile = open(outputFileName, 'w')
    # ofile.write("Container stores {} animals:\n".format(len(container.store)))
    # container.Write(ofile)
    # ofile.close()
    #
    # # Сортируем контейнер
    # container.heapSort()
    #
    # # Записываем данные отсортированного контейнера в файл
    # osfile = open(outputSortedName, 'w')
    # osfile.write("Sorted container stores {} animals:\n".format(len(container.store)))
    # container.Write(osfile)
    # osfile.close()
    #
    # print('==> Finish')
    # end = time.time()
    # print("Run-time = ", end - start, " sec")
