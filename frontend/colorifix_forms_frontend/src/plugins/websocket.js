import {protocol, url, port, channel} from '../config.yml'
const socket = new WebSocket(`${protocol}://${url}:${port}/${channel}`);

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