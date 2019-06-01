import QtQuick 2.0
import QtQuick.Layouts 1.3

Item {
    id: button
    implicitWidth: backgroundImage.width*window.width/1280
    implicitHeight: backgroundImage.height*window.height/720
    width: backgroundImage.width*window.width/1280
    height: backgroundImage.height*window.height/720


    signal clicked
    property string normalSrc: ""
    property string hoverSrc: ""
    property string clickedSrc: ""
    property string b_icon: ""
    property string caption: ""
    property bool dis: true
    property string textcolor: "#525f70"
    property int posx: 78
    property int posy: 24


    function clip(){
        backgroundImage.source = clickedSrc
        cap.color = "#ffffff"
        dis = false
    }

    function unclip(){
        dis= true
        backgroundImage.source = normalSrc
        cap.color = textcolor
    }

    Image {
        id: backgroundImage
        anchors.fill: button
        source: (button.enabled ? normalSrc : clickedSrc)
    }

    Image {
        x: 31
        y: 23
        source: b_icon
    }

    MouseArea {
        hoverEnabled: true
        anchors.fill: button
        onClicked: { if (dis) button.clicked() }
        onEntered: { if (dis) backgroundImage.source = hoverSrc; }
        onExited: { if (dis) { backgroundImage.source = normalSrc; cap.color = textcolor } }
        onPressed: { if (dis) { backgroundImage.source = clickedSrc; cap.color = "#ffffff"} }
        onReleased: { if (dis) { backgroundImage.source = (button.enabled ? hoverSrc : clickedSrc); cap.color = textcolor } }
    }

    Text{
        id: cap
        x: posx
        y: posy
        font.pixelSize: 20
        //font.letterSpacing: -1
        text: caption
        font.family: "Roboto Regular"
        color: textcolor
    }
}
