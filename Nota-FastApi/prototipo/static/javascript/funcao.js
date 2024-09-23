function mostrar_esconder(el){
    var display = document.getElementById(el).style.display;
    if(display == "block"){
        document.getElementById(el).style.display = 'none';
    }
    else{
        document.getElementById(el).style.display = 'block';
    }
}

function esconder_mostrar(el){
    var display = document.getElementById(el).style.display;
    if(display == "none"){
        document.getElementById(el).style.display = 'block';
    }
    else{
        document.getElementById(el).style.display = 'none';
    }
}


document.addEventListener('DOMContentLoaded', () =>{
    const salvar = document.getElementById('salvar');
    const menssagem = document.getElementById('menssagem');
    salvar.addEventListener('click', () => {
        menssagem.classList.remove('msg-alerta');
        menssagem.classList.add('show');

        setTimeout(() => {
            menssagem.classList.remove('show');
            menssagem.classList.add('msg-alerta');
        }, 900000000);
    });
});

///MOSTRAR SENHA

function mostrarSenha(){
    var inputpass = document.getElementById('password')
    var btnShowPass = document.getElementById('btn-valor')

    if (inputpass.type === 'text'){
        inputpass.setAttribute('type','password')
        btnShowPass.classList.replace('bi-eye-fill','bi-eye-slash-fill')
    }else{
        inputpass.setAttribute('type','text')
        btnShowPass.classList.replace('bi-eye-slash-fill','bi-eye-fill')
    }
}