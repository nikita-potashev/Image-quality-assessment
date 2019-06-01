import QtQuick 2.7
import QtQuick.Controls 2.2

Dialog {
    id: dialog
    standardButtons: DialogButtonBox.Ok

    property alias source : image.source
    property alias fillMode: image.fillMode
    property alias prediction: element.text

    Image {
        id: image
        anchors.bottomMargin: 100

        anchors.fill: parent

        // horizontalAlignment: Qt.AlignLeft
        // verticalAlignment: Qt.AlignTop
    }

    Text {
        id: element
        verticalAlignment: Text.AlignBottom
        horizontalAlignment: Text.AlignLeft

        anchors.right: parent.right
        anchors.rightMargin: 640
        anchors.left: parent.left
        anchors.leftMargin: 0
        anchors.top: image.bottom
        anchors.topMargin: 0

        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        topPadding: 0
        // anchors.fill: parent
        visible: true

        font.pixelSize: 12
    }
}
















/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:2;anchors_height:100;anchors_width:0}
}
 ##^##*/
