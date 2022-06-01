function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function request() {
	let xhr = new XMLHttpRequest();
	xhr.open("POST", "/tg_chat/send_message/");

	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));

	xhr.onload = () => console.log(xhr.responseText);

	var str = document.getElementById("message-input").value;

	let data = `{
	  "message": "${str}"
	}`;

	xhr.send(data);
}

(function() {
  document.getElementById('message-input').addEventListener('keydown', function(e) {
    if (e.keyCode === 13) {
      request();
    }
  });
})();