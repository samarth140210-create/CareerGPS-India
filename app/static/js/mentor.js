const textarea = document.getElementById("question");
const form = document.getElementById("mentorForm");
const chat = document.getElementById("chatContainer");
const scrollBtn = document.getElementById("scrollBottomBtn");

function scrollBottom(){

    chat.scrollTop = chat.scrollHeight;

}

scrollBottom();

textarea.addEventListener("input",function(){

    this.style.height="auto";
    this.style.height=this.scrollHeight+"px";

});

textarea.addEventListener("keydown",function(e){

    if(e.key==="Enter" && !e.shiftKey){

        e.preventDefault();
        form.requestSubmit();

    }

});

function copyText(button){

    const text=button.parentElement.firstElementChild.innerText;

    navigator.clipboard.writeText(text);

    button.innerHTML="✓ Copied";

    setTimeout(function(){

        button.innerHTML="📋 Copy";

    },1500);

}

function createUserBubble(text){

    const wrapper=document.createElement("div");

    wrapper.className="message user";

    wrapper.innerHTML=`
        <div class="bubble">
            ${text}
        </div>
    `;

    chat.appendChild(wrapper);

    scrollBottom();

}

function createTypingBubble(){

    const wrapper=document.createElement("div");

    wrapper.className="message ai";

    wrapper.innerHTML=`

        <div class="bubble">

            <div class="typing">

                <span></span>

                <span></span>

                <span></span>

            </div>

        </div>

    `;

    chat.appendChild(wrapper);

    scrollBottom();

    return wrapper;

}

async function typeWriter(element,text){

    element.innerHTML="";

    let i=0;

    return new Promise(resolve=>{

        const timer=setInterval(()=>{

            element.innerHTML+=text.charAt(i);

            i++;

            if(chat.scrollHeight-chat.scrollTop-chat.clientHeight<150){

                scrollBottom();

            }

            if(i>=text.length){

                clearInterval(timer);

                resolve();

            }

        },12);

    });

}

chat.addEventListener("scroll",function(){

    if(chat.scrollTop+chat.clientHeight<chat.scrollHeight-250){

        scrollBtn.style.display="block";

    }

    else{

        scrollBtn.style.display="none";

    }

});

scrollBtn.addEventListener("click",function(){

    scrollBottom();

});

form.addEventListener("submit",async function(e){

    e.preventDefault();

    const message=textarea.value.trim();

    if(message==="") return;

    createUserBubble(message);

    textarea.value="";
    textarea.style.height="28px";

    const aiBubble=createTypingBubble();

    try{

        const response=await fetch("/mentor-api",{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                question:message

            })

        });

        const data=await response.json();

        aiBubble.innerHTML=`

            <div class="bubble">

                <div class="answer"></div>

                <button
                    class="copy-btn"
                    onclick="copyText(this)">

                    📋 Copy

                </button>

            </div>

        `;

        const answerBox =

        aiBubble.querySelector(

        ".answer"

        );

        await typeWriter(

        answerBox,

        data.answer

        );

        if(window.marked){

        answerBox.innerHTML=

        marked.parse(

        answerBox.innerText

        );

        }

    }

    catch{

        aiBubble.innerHTML=`

            <div class="bubble">

                Something went wrong.

            </div>

        `;

    }

});