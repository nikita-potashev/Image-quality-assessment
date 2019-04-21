import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12
import QtQuick.Layouts 1.12
import QtQuick.Dialogs 1.0

ApplicationWindow {
    id: applicationWindow
    width: 640
    height: 480
    visible: true
    title: "NRIQA"

    Material.theme: Material.Dark

    TabBar {
        id: bar
        width: parent.width
        TabButton {
            text: "Single"
            width: implicitWidth
        }
        TabButton {
            text: "Several"
            width: implicitWidth
        }

    }

    StackLayout {
        id:stack
        width: parent.width
        currentIndex: bar.currentIndex
        Item {
            id: single
            property string url_file: ""
            Button {
                id: btn_predict
                y: 325
                text: qsTr("Predict")
                anchors.verticalCenterOffset: 430
                anchors.horizontalCenterOffset: -257
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                onClicked: {

                    signals.prediction(single.url_file)
                    busyIndicator.running = true
                }
            }

            Button {
                id: btn_openfile
                y: 64
                text: qsTr("Open file")
                anchors.verticalCenterOffset: 92
                anchors.horizontalCenterOffset: -257
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                onClicked: {
                    fileDialog.title = "Open file"
                    fileDialog.nameFilters = [ "All files (*)" ]
                    fileDialog.selectExisting = true
                    fileDialog.open()
                }

            }

            Image {
                id: predict_image
                x: 198
                y: 34
                width: 414
                height: 316
                transformOrigin: Item.BottomRight
                anchors.bottom: parent.bottom
                anchors.bottomMargin: -404
                anchors.right: parent.right
                anchors.rightMargin: 25
                anchors.horizontalCenterOffset: 88
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenterOffset: 246
                anchors.verticalCenter: parent.verticalCenter
                fillMode: Image.PreserveAspectFit
                source: single.url_file
            }

            Text {
                id: predict_out
                x: 201
                y: 410
                width: 414
                height: 40
                text: qsTr("")
                font.pixelSize: 12
                Material.accent:Material.color(Material.DeepOrange)
            }

            FileDialog {
                id: fileDialog
                width: 300
                height: 300
                folder: shortcuts.home
                selectMultiple: false
                selectFolder: false
                onAccepted: {
                    if(fileDialog.selectExisting == true) {
                        console.log(fileDialog.fileUrl)
                        single.url_file = fileDialog.fileUrl
                    }
                    else {
                        console.log(fileDialog.fileUrl)
                    }
                }
            }




        }

        Item {
            id: several
        }
    }

    BusyIndicator {
        id: busyIndicator
        x: 128
        y: 411
        width: 48
        height: 40
        running: false
    }

//    Connections {

//        target: signals

//        // Обработчик сигнала сложения
//        prediction_result: {
//            // sum было задано через arguments=['sum']
//            predict_out.text = prediction
//        }

//    }
}


























