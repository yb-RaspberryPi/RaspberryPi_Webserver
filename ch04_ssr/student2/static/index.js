var n = 0;
var num = document.querySelector("#num");
var increase = document.querySelector("#increase");
var submit = document.querySelector("#submit");

increase.addEventListener("click", function() {
    n = n + 1;
    num.innerHTML = n;
})

submit.addEventListener("click", function() {
    fetch("/save", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            num: n
        })
    })
    .then(function(response) {
        location.href = "/";
    });

    num.innerHTML = n;
})
