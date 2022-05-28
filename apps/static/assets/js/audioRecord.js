var recorders = document.querySelectorAll('[name="audioCapture"]');
var players = document.querySelectorAll('audio');

recorders.forEach((recorder, i) => {
  recorder.addEventListener('change', function(e) {
    var file = e.target.files[0];
    // Do something with the audio file.
    players[i].src =  URL.createObjectURL(file);
  });
})

// WebRTC
var recordButton = document.getElementById('recorder4');
recordButton.onclick = getOrCreateAudioContext;

function successCallback(stream) {
    // RecordRTC usage goes here
  var recordRTC = RecordRTC(stream);

  startAudioRecorder();

  function startAudioRecorder () {
    recordRTC.startRecording();
    recordButton.value = 'Stop Recording';
    recordButton.onclick = stopAudioRecorder;
  };

  function stopAudioRecorder (audio_recorder) {
      recordRTC.stopRecording(function(audioURL) {
          document.querySelector('#player4').src = audioURL;

          var recordedBlob = recordRTC.getBlob();
          //recordRTC.getDataURL(function(dataURL) { });
          recordButton.value = 'Record';
          recordButton.onclick = startAudioRecorder;
      });
  }
}

function errorCallback(error) {
    // maybe another application is using the device
  // alert('whoops, looks like you can\'t record audio using WebRTC')
  console.error('could not get device for webrtc')
}

function getOrCreateAudioContext () {
  var mediaConstraints = { video: false, audio: true };

  navigator.mediaDevices.getUserMedia(mediaConstraints).then(successCallback).catch(errorCallback);

}