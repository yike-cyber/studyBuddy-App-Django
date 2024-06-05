function showReplyTo(messageId, InputField) {
  let elementstyle = document.getElementById(InputField).style;
  if (elementstyle.display == "none") {
    elementstyle.display = "block";
  } else {
    elementstyle.display = "block";
  }
}

function showParticipants() {
  let elementStyle = document.getElementById("Participants_id").style;

  if (elementStyle.display == "none") {
    elementStyle.display = "block";
  } else {
    elementStyle.display = "none";
  }
}

// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("reply-form-{{message.id}}");
//   const statusMessage = document.getElementById(
//     "status-message-{{message.id}}"
//   );
//   console.log(`{{message.id}}`);
//   form.addEventListener("submit", async function (event) {
//     event.preventDefault();

//     const url = form.action;
//     const formData = new FormData(form);
//     const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;

//     try {
//       const response = await fetch(url, {
//         method: "POST",
//         headers: {
//           "X-CSRFToken": csrfToken,
//         },
//         body: formData,
//       });

//       if (response.obk) {
//         const data = await response.json();
//         document.getElementById("message_body_{{message.id}}").value = "";
//         statusMessage.innerText = "Reply submitted successfully";
//       } else {
//         const errorData = await response.json();
//         console.error("Error submitting reply:");
//       }
//     } catch (error) {
//       console.error("Error submitting reply:", error);
//     }
//   });
// });
