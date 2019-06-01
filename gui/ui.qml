import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12
import QtQuick.Layouts 1.12
import QtQuick.Dialogs 1.0
import QtQuick.Window 2.2
import QtGraphicalEffects 1.0
import QtQuick.Shapes 1.0

Window {
    id: applicationWindow
    width: 640
    height: 480
    visible: true
    maximumWidth: 640
    maximumHeight: 480
    minimumWidth: 640
    minimumHeight: 480
    title: "NRIQA"

    property var init: false

    onAfterRendering: {

        if (!init) {

            console.log("init_models")
            signals.init_models()
            btn_openfile.enabled = true
            btn_openfolder.enabled = true
            btn_predict.enabled = true
            btn_predict_several.enabled = true
            init = true
            busyIndicator.running = false
            element4.visible = false
        }
    }

    Material.theme: Material.Light
    Material.accent: Material.color(Material.Teal)

    function showMessageBox(message,title) {
        var component = Qt.createComponent("MessageDialog.qml")
        if (component.status === Component.Ready) {
            var dialog = component.createObject(rectangle)

            dialog.title = qsTr(title)
            dialog.text = message
            dialog.anchors.centerIn = rectangle
            dialog.open()
        } else
            console.error(component.errorString())
    }

    function showImage(path,text){

        var component = Qt.createComponent("MessageDialogImage.qml")
        if (component.status === Component.Ready){

            var img = component.createObject(rectangle)
            img.source = path
            img.width = rectangle.width
            img.height = rectangle.height
            img.fillMode =Image.PreserveAspectFit
            img.prediction = text
            img.open()
        } else
            console.error(component.errorString())
    }

    function urlToPath(urlString) {
        var s
        if (urlString.startsWith("file:///")) {
            var k = urlString.charAt(9) === ':' ? 8 : 7
            s = urlString.substring(k)
        } else {
            s = urlString
        }
        return decodeURIComponent(s);
    }

    TabBar {
        id: bar
        width: parent.width

        TabButton {
            text: "Изображение"
            width: implicitWidth
            Material.background: Material.color(Material.Teal)
        }
        TabButton {
            text: "Коллекция изображений"
            width: implicitWidth
            Material.background: Material.color(Material.Teal)
        }
        TabButton {
            text: "Настройки"
            width: implicitWidth
        }
    }

    StackLayout {
        id: stack
        width: parent.width
        currentIndex: bar.currentIndex

        Item {
            id: single
            property string url_file: ""
    
            property string filename: "single_report_" + Qt.formatDateTime(new Date(), "H:m:s") + ".json"

            Button {
                id: btn_predict
                y: 325
                width: 95
                height: 52
                text: qsTr("Расчет")
                enabled: false
                anchors.verticalCenterOffset: 429
                anchors.horizontalCenterOffset: -257
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                onClicked: {

                   if (single.url_file.length == "") {
                       showMessageBox("Выберите изображение", "Ошибка!")
                   } else {

                       var temp = signals.prediction(single.url_file)
                       console.log(typeof temp[temp.indexOf("TotalPrediction") + 18])
                       console.log(temp[temp.indexOf("TotalPrediction") + 18])
                       console.log(temp)
                       if (temp[temp.indexOf("TotalPrediction") + 18] === '0') {

                           showMessageBox("Качественное изображение",
                                          "Результаты прогноза")

                       } else
                           showMessageBox("Некачественное изображение",
                                          "Результаты прогноза")

                   }
                }
                Material.background: Material.color(Material.Teal)
                Material.foreground: "white"
            }

            Button {
                id: btn_openfile
                y: 64
                width: 97
                height: 45
                text: qsTr("Открыть")
                enabled: false
                checked: false
                clip: false
                visible: true
                focusPolicy: Qt.NoFocus
                display: AbstractButton.TextBesideIcon
                anchors.verticalCenterOffset: 90
                anchors.horizontalCenterOffset: -263
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                onClicked: fileDialogOpenFile.open()

                FileDialog {
                    id: fileDialogOpenFile
//                    folder: "."
                    title: "Выберите файл для открытия"
                    selectMultiple: false
                    nameFilters: ["Image files (*.jpg *.png *.bmp *.tiff *.jpeg)"]
                    onAccepted: {
                        single.url_file = urlToPath(fileDialogOpenFile.fileUrl)
                        custbut.visible = false


                    }
                }

                Material.background: Material.color(Material.Teal)
                Material.foreground: "white"
            }

            Rectangle {
                id: rectangle
                x: 232
                y: 73
                width: 380
                height: 380

                CustButton {
                    id: custbut
                    x: 0
                    y: 0
                    width: rectangle.width
                    height: rectangle.height
                    normalSrc: "images/file_normal.png"
                    hoverSrc: "images/file_hovered.png"
                    clickedSrc: "images/file_hovered.png"
                    onClicked: fileDialog.open()

                    FileDialog {
                        id: fileDialog
                        folder: "."
                        title: "Выберите файл для открытия"
                        selectMultiple: false
                        nameFilters: ["Image files (*.jpg *.png *.bmp *.tiff *.jpeg)"]
                        onAccepted: {
                            single.url_file = urlToPath(fileDialog.fileUrl)
                            custbut.visible = false
                        }
                    }

                    DropArea {
                        id: drop
                        anchors.rightMargin: 413
                        anchors.bottomMargin: 0
                        anchors.fill: parent
                        onEntered: {
//                            if (drag.urls.length == 1) {
//                                single.url_file[0] = drag.urls[0].toString()
//                                single.url_file[0] = single.url_file.replace(
//                                            /^(file:\/{2})/, "")
//                                single.url_file[0] = decodeURIComponent(
//                                            single.url_file[0])
//                            }
                        }
                    }
                }
                Image {

                    width: parent.width
                    height: parent.height
                    fillMode: Image.PreserveAspectFit
                    source: single.url_file
                }
            }

            CheckBox {
                id: save_single
                x: 8
                y: 329
                text: qsTr("Сохранить отчет")
                checkState: Qt.Checked
            }

            Switch {
                id: element
                x: 12
                y: 131
                text: qsTr("Резкость")
                checked: true
            }

            Switch {
                id: element1
                x: 12
                y: 182
                text: qsTr("Шум")
                checked: true
            }

            Switch {
                id: element2
                x: 12
                y: 228
                text: qsTr("Яркость")
                checked: true
            }
        }

        Item {
            id: several
            property var paths_list: []
            property var predict_values: ({})

            Button {
                id: btn_predict_several
                y: 325
                width: 95
                height: 52
                text: qsTr("Расчет")
                enabled: false
                anchors.verticalCenterOffset: 429
                anchors.horizontalCenterOffset: -257
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                onClicked: {
                    busyIndicator.running = true
                    element4.visible = true
                    if (several.paths_list.length == 0) {
                        showMessageBox("Пустая коллекция", "Ошибка!")
                    } else {

                        for (var i = 0; i < several.paths_list.length; i++){
                            several.paths_list[i] = several.paths_list[i].toString()
                            var yolo = signals.prediction(urlToPath(several.paths_list[i]))
                            several.predict_values[several.paths_list[i]] = yolo




                        }
                        element4.visible = false
                        busyIndicator.running = false



                    }

                }
                onReleased: {
                    busyIndicator.running = true
                    element4.visible = true

                }

                Material.background: Material.color(Material.Teal)
                Material.foreground: "white"
            }
            CheckBox {
                id: save_several
                x: 8
                y: 329
                text: qsTr("Сохранить отчет")
                checkState: Qt.Checked
            }

            Switch {
                id: element_several
                x: 12
                y: 131
                text: qsTr("Резкость")
                checked: true
            }

            Switch {
                id: element1_sveral
                x: 12
                y: 182
                text: qsTr("Шум")
                checked: true
            }

            Switch {
                id: element2_several
                x: 12
                y: 228
                text: qsTr("Яркость")
                checked: true
            }

            GridView {
                id: gridView

                x: 272
                y: 83
                width: 330
                height: 330
                contentHeight: 330
                contentWidth: 330
                clip: true
                //                highlightRangeMode: GridView.ApplyRange
                //                clip: true

                //                flow: GridView.FlowLeftToRight

                //                boundsBehavior: Flickable.StopAtBounds
                //                flickableDirection: Flickable.VerticalFlick
                visible: true
                cellWidth: 110
                cellHeight: 110
                delegate: Column {

//                  anchors.horizontalCenter: parent.horizontalCenter

                    Image {
                        id: image
                        property bool prop: false
                        width: 80
                        height: 80
                        anchors.horizontalCenter: parent.horizontalCenter
//                        fillMode: Image.PreserveAspectFit

                        source: img
                        clip: true

                        scale:  mouseArea.containsMouse ? 1.1 : 1.0
                        smooth: mouseArea.containsMouse
                        MouseArea {
                            id: mouseArea
                            clip: true
                            anchors.fill: parent
                            anchors.margins: -10
                            hoverEnabled: true         //this line will enable mouseArea.containsMouse
                            onClicked: {

                            if (several.predict_values[image.source]== undefined){

                                showImage(image.source,"")
                            }
                            else {
                                var temp = several.predict_values[image.source]
                                if (temp[temp.indexOf("TotalPrediction") + 18] === '0') {

                                    showImage(image.source,"Качественное изображение")

                                }
                                else
                                    showImage(image.source,"Некачественное изображение")



                            }


                            }
                            // if (temp[temp.indexOf("TotalPrediction") + 18] == 0) {


                            // } else

                            // showImage(image.source,several.predict_values[image.source])

                            // }

                        }


                    }
//                    Image {
//                        id:quality
//                        visible: vision
//                        width: 40
//                        height: 40
//                        x: image.width
//                        y: image.height + quality.height
//                        source:  "images/yes.jpg"
//                        fillMode: Image.PreserveAspectFit
//                    }

//                    CheckBox{
//                        id: quality
//                        visible: true
//                        width: 20
//                        height: 20
//                        x: image.width
//                        y: image.height + quality.height
//                        checked: image.prop

//                        clip: true


//                    }

                }
                model: ListModel {
                    id: gallery
                }


            }

            Button {
                id: btn_openfolder
                y: 64
                width: 97
                height: 45
                text: qsTr("Открыть")
                enabled: false
                checked: false
                clip: false
                visible: true
                focusPolicy: Qt.NoFocus
                display: AbstractButton.TextBesideIcon
                anchors.verticalCenterOffset: 90
                anchors.horizontalCenterOffset: -263
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                onClicked: fileDialogOpenFolder.open()

                FileDialog {
                    id: fileDialogOpenFolder
                    folder: "."
                    title: "Выберите файл для открытия"
                    selectMultiple: true
                    nameFilters: ["Image files (*.jpg *.png *.bmp *.tiff *.jpeg)"]
                    onAccepted: {
                        several.paths_list = fileDialogOpenFolder.fileUrls
                        for (let item of several.paths_list){
                            item = decodeURIComponent(item)
                            gallery.append({"img":item})
                        }

                    }
                }

                Material.background: Material.color(Material.Teal)
                Material.foreground: "white"
            }
        }

        Item {
            id: settings

            TextField {
                id: save_report
                x: 46
                y: 89
                width: 422
                height: 40
                text: Qt.resolvedUrl(".").replace(/^(file:\/{2})/, "")
            }

            ComboBox {
                id: comboBox
                x: 166
                y: 145
                model: ["json", "html", "csv", "xml"]
            }

            Button {
                id: button_savefolder
                x: 490
                y: 89
                width: 94
                height: 40
                text: qsTr("Обзор...")
                onClicked: fileDialogSaveFolder.open()
                FileDialog {
                    id: fileDialogSaveFolder
                    selectMultiple: false

                    selectFolder: true
                    onAccepted: {
                        save_report.text = fileDialogSaveFolder.fileUrl.toString().replace(/^(file:\/{2})/, "")
                    }
                }
            }

            Text {
                id: element3
                x: 46
                y: 145
                width: 119
                height: 40
                text: qsTr("Формат отчета")
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignLeft
                font.pixelSize: 15
            }
        }
    }

    BusyIndicator {
        id: busyIndicator
        x: 143
        y: 405
        width: 50
        height: 46
        enabled: true
        wheelEnabled: false
        running: true
    }

    Text {
        id: element4
        x: 143
        y: 457
        text: qsTr("Загрузка...")
        textFormat: Text.PlainText
        font.pixelSize: 12
    }
}
