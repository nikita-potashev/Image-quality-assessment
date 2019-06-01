import QtQuick 2.7
import QtQuick.Controls 2.2

Dialog {
    standardButtons: DialogButtonBox.Ok

    property alias text : textContainer.text

    Text {
        id: textContainer

        anchors.fill: parent

        horizontalAlignment: Qt.AlignLeft
        verticalAlignment: Qt.AlignTop
    }
}