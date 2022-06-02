// Метод для получения куки с scrf токеном
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

// Проскролить до самого низа сообщений
function scrollDown() {
	var chat = document.getElementById('chat-history');
	chat.scrollTop = chat.scrollHeight;	
}

// Поиск элемента для сообщений
function getElem() {
    let elem = document.getElementById("message-in-chat"); //находим элемент с сообщениями
    while (elem.firstChild) { //очищаем его
	    elem.removeChild(elem.firstChild);
    }
	return elem;
}

// Вносит в элемент новое сообщение
function addChat(item) {
  	let li = document.createElement("li");
  	let div1 = document.createElement("div");
  	let div2 = document.createElement("div");
  	let span = document.createElement("div");
  	li.className = "clearfix";

  	div1.className = "message-data text-right";

  	if (item.is_user === false) {
  		div2.className = "message my-message";
  		span.className = "message-data-time";
  	} else {
  		div2.className = "message other-message float-right";
  		span.className = "message-data-time";
  	}
  	div2.textContent = item.text;

  	let time = new Date(item.date)
    timeformat = [time.getMonth()+1,
               time.getDate()].join('/')+' - '+
              [time.getHours(),
               time.getMinutes()].join(':');
  	span.textContent = timeformat;

  	div2.append(span);
  	li.append(div1);
  	li.append(div2);
  	return li
}

// Метод для отправки сообщения в тг
function sendMessage() {
	var str = document.getElementById("message-input").value;
	let elem = document.getElementById("message-in-chat");

	$.ajax({
		type: 'POST',
		beforeSend: function(request) {
		  request.setRequestHeader("Content-Type", "application/json");
		  request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		},
	    url: '/chat/send_message/',
	    data: `{ 
		  "message": "${str}",
		  "user_id": "${window.location.pathname.split("/")[2]}"
	    }`,
	    success: (result) => {
	    	elem.append(addChat(result.response));
			scrollDown();
	    }
	});
}

let first_response = true

// Метод проверки новых сообщений(не совсем проверки новых, скорее обновление старых)
// Делает запрос, получает все мэсседжи в чате, выводит их в элемент
function check() { 
	  $.ajax({
	    type: 'POST',
		beforeSend: function(request) {
		  request.setRequestHeader("Content-Type", "application/json");
		  request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		},
	    url: '/user/get_messages/',
	    data: `{ 
	    	"user_id" : "${window.location.pathname.split("/")[2]}"
	    }`,
	    success: (result) => {

	      elem = getElem();

	      result.response.forEach(function(item, i, arr) { // Наполняем чат сообщениями
	      	elem.append(addChat(item)); // Вносим сообщения в чат
	      });

	      if (first_response == true) { // Если мы первый раз загрузили страницу, то скролим вниз
		      scrollDown();
		      first_response = false;
	      }

	      setTimeout(check, 5000); // Через 5 секунд вызываем функцию вновь
	    }
	  });
};

(function() {
  inp = document.getElementById('message-input');
  if (typeof inp !== "undefind") {
	  inp.addEventListener('keydown', function(e) {
	    if (e.keyCode === 13) { // При нажатии enter делаем запрос
	      sendMessage();
	      inp.value = null;
	    }
	  });
  }
})();

check();