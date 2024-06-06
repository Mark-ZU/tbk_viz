import QtQuick

Rectangle{
    id: root
    width: 100
    height: 100
    color: "red"
    MouseArea{
        anchors.fill: parent
        onClicked: {
            console.log("clicked")
        }
    }
}