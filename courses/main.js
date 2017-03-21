window.onload=main;

function main()
{
    var splink=document.querySelector(".splink");
    var spfield=document.querySelector(".spfield");

    splink.addEventListener("click",function(e){
        e.preventDefault();
        spfield.classList.toggle("hidden");
    });
}