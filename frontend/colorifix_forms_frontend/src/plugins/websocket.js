const socket = new WebSocket("ws://localhost:8000/ws");
console.log('Socket initialized')

function socketCheck(callback){
    if(socket.readyState === 1){
    callback()
  }
  else{
    socket.onopen = () => {
    callback()
  };
  }
}
export {socket, socketCheck};