# -*- encoding:utf-8 -*-
"""
    author:lgh
"""

from win32com.client import Dispatch, constants

def doc2pdf(input, output):
    w = Dispatch('Word.Application')
    try:
        # 打开文件
        doc = w.Documents.Open(input, ReadOnly=1)
        # 转换文件
        doc.ExportAsFixedFormat(output, constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup, CreateBookmarks = constants.wdExportCreateHeadingBookmarks)
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        w.Quit(constants.wdDoNotSaveChanges)

def doc2html(input, output):
    w = Dispatch('Word.Application')
    try:
        doc = w.Documents.Open(input, ReadOnly=1)
        doc.SaveAs(output, 8)
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        w.Quit(constants.wdDoNotSaveChanges)

def main():
    input = r'F:\shezhi\需求.docx'
    output = r'F:\shezhi\test.html'
    # rc = doc2pdf(input, output)
    rc = doc2html(input, output)
    if rc:
        print('转换成功')
    else:
        print('转换失败')

if __name__ == '__main__':
    main()