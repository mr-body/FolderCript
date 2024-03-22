eel.expose(pythonSay)
eel.expose(updateProgress);
eel.expose(updateName);
eel.expose(verificAdd);

const MAX = 100

const cp = new CircleProgress('.progress', {
	max: MAX,
	value: 0,
	animationDuration: 400,
	textFormat: (val) => val + '%',
});


function pythonSay(info) {
	console.log(info)
}

eel.javascriptSay("Cliente javascript escutando")

listHistory("")

let caminho

async function selectFolder() {
    let folder = await eel.SelectFolder()()
    folder_info = folder
    this.caminho = folder_info[1]
    $("#nomePasa").html(folder_info[0])
    $("#postCaminho").html(folder_info[1])
    $("#tamanhoTotal").html("<b>"+folder_info[2]+folder_info[3]+"</b>")
    $("#nPastas").html("Pastas: <b>"+folder_info[4]+"</b>")
    $("#nitens").html("Itens: <b>"+folder_info[5]+"</b>")

    $("#btn_titulo").html("Pasta <b>'"+folder_info[0]+"'</b>")
}

function updateProgress(progress) {
  // Update progress bar width and text
  $(".viewStatus").addClass("show")

  const val = progress;
	cp.value = val;
	cp.el.style.setProperty('--progress-value', val / MAX);
  
  if (progress == 100) {
    $("#increment").text(`0%`);
    $("#progress").val(0);
    $("#filename").text("");
    
    eel.save($("#postCaminho").text(), $("#chave").val(), "teste feito com sucesso");
    
    $(".viewStatus").removeClass("show")

    $("#nomePasa").text("")
    $("#postCaminho").text("")
    $("#tamanhoTotal").text("")
    $("#nPastas").text("")
    $("#nitens").text("")
    $("#chave").val("");

    $("#chave").val("")
    caminho = ""
    ocument.getElementById('postCaminho').textContent = 'Nenhuma pasta selecionada'
    document.querySelector('.concluido').classList.add('showSucess');
    document.querySelector('.rotulo').classList.add('showSucess');

    document.querySelector('button').classList.remove('HideBigBtn');
		document.querySelector('.progress').classList.remove('showprogress');
    document.getElementById('btn_titulo').textContent = 'Selecionar Pasta'
    listHistory(value)
  }
}


function updateName(name) {
    // Atualizar a nome do ficheiro
    $("#filename").text(`Crit: ${name}`)
}


function verificAdd(info) {
    $("#info").text(info)
}

async function criptografar() {
    document.querySelector('.modal').classList.remove('showModal');
    if($(".option").val() == 1)
    {
      if(document.getElementById('postCaminho').textContent != 'Nenhuma pasta selecionada')
      {
        await eel.Criptografar(this.caminho,$("#chave").val())
        document.querySelector('.modal').classList.remove('showMonal')
        document.querySelector('.btnCripto').style='transform: scale(0%)'
      }
      else{
        alert("selecina uma pasta e define uma senha")
        window.location.reload()
      }
    }
    else
    {
     if(document.getElementById('postCaminho').textContent != 'Nenhuma pasta selecionada')
      {
        await eel.decrypt(this.caminho,$("#chave").val())
        document.querySelector('.modal').classList.remove('showMonal')
        document.querySelector('.btnCripto').style='transform: scale(0%)'
      }
      else{
        alert("selecina uma pasta e define uma senha")
        window.location.reload()
      }
    }
    
}


function buscaHist(value)
{
  listHistory(value)
}