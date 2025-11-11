// === TEMAS, PALAVRAS E DICAS ===
const temas = {
    capitais: {
        1: { 
            palavras: ["recife", "fortaleza", "salvador", "joaopessoa", "maceio"],
            dica: "🏙️ Capitais do Nordeste do Brasil"
        },
        2: { 
            palavras: ["brasilia", "florianopolis", "curitiba", "belo horizonte"],
            dica: "🌎 Capitais de todos os estados brasileiros"
        },
        3: { 
            palavras: ["paris", "londres", "toquio", "berlim", "roma"],
            dica: "🗺️ Capitais famosas ao redor do mundo"
        }
    },
    animais: {
        1: { 
            palavras: ["gato", "cachorro", "vaca", "pato", "peixe"],
            dica: "🐾 Animais domésticos e comuns"
        },
        2: { 
            palavras: ["elefante", "girafa", "zebra", "jacare"],
            dica: "🦓 Animais selvagens e de zoológico"
        },
        3: { 
            palavras: ["ornitorrinco", "camaleao", "canguru", "chimpanze"],
            dica: "🐉 Animais exóticos e raros"
        }
    },
    frutas: {
        1: { 
            palavras: ["maca", "pera", "uva", "manga", "banana"],
            dica: "🍌 Frutas populares do dia a dia"
        },
        2: { 
            palavras: ["abacaxi", "cereja", "pitanga", "melancia"],
            dica: "🍒 Frutas tropicais e regionais"
        },
        3: { 
            palavras: ["carambola", "tamarindo", "framboesa", "maracuja"],
            dica: "🥭 Frutas raras e de nomes incomuns"
        }
    }
};

// === VARIÁVEIS ===
let palavraSecreta = "";
let letrasUsadas = [];
let chances = 7;

// === ELEMENTOS ===
const menu = document.getElementById("menu");
const jogo = document.getElementById("jogo");
const palavraDiv = document.getElementById("palavra");
const chancesSpan = document.getElementById("chances");
const usadasSpan = document.getElementById("usadas");
const mensagem = document.getElementById("mensagem");
const letraInput = document.getElementById("letra");
const dicasDiv = document.getElementById("dicas");

// === EVENTOS ===
document.getElementById("iniciar").addEventListener("click", iniciarJogo);
document.getElementById("tentar").addEventListener("click", tentarLetra);
document.getElementById("reiniciar").addEventListener("click", () => location.reload());
letraInput.addEventListener("keypress", e => e.key === "Enter" && tentarLetra());

document.getElementById("tema").addEventListener("change", atualizarDica);
document.getElementById("nivel").addEventListener("change", atualizarDica);

// === FUNÇÕES ===
function atualizarDica() {
    const tema = document.getElementById("tema").value;
    const nivel = document.getElementById("nivel").value;
    if (tema && nivel) {
        dicasDiv.textContent = temas[tema][nivel].dica;
    } else {
        dicasDiv.textContent = "💡 Escolha um tema e um nível para ver as dicas aqui!";
    }
}

function iniciarJogo() {
    const tema = document.getElementById("tema").value;
    const nivel = document.getElementById("nivel").value;

    if (!tema || !nivel) {
        alert("⚠️ Escolha um tema e um nível antes de jogar!");
        return;
    }

    const lista = temas[tema][nivel].palavras;
    palavraSecreta = lista[Math.floor(Math.random() * lista.length)].toLowerCase();

    menu.classList.add("hidden");
    jogo.classList.remove("hidden");

    atualizarTela();
}

function atualizarTela() {
    palavraDiv.textContent = palavraSecreta
        .split("")
        .map(l => (letrasUsadas.includes(l) ? l : "_"))
        .join(" ");
    chancesSpan.textContent = chances;
    usadasSpan.textContent = letrasUsadas.join(", ");
}

function tentarLetra() {
    const letra = letraInput.value.toLowerCase().trim();
    letraInput.value = "";

    if (!letra || letra.length !== 1) {
        alert("Digite apenas uma letra!");
        return;
    }
    if (letrasUsadas.includes(letra)) {
        alert("Você já tentou essa letra!");
        return;
    }

    letrasUsadas.push(letra);

    if (palavraSecreta.includes(letra)) {
        mensagem.textContent = "✅ Letra correta!";
    } else {
        chances--;
        mensagem.textContent = "❌ Letra incorreta!";
    }

    atualizarTela();
    verificarFimDeJogo();
}

function verificarFimDeJogo() {
    if (chances <= 0) {
        mensagem.textContent = `😢 Você perdeu! A palavra era "${palavraSecreta}".`;
        letraInput.disabled = true;
        return;
    }

    const venceu = palavraSecreta.split("").every(l => letrasUsadas.includes(l));
    if (venceu) {
        mensagem.textContent = `🎉 Parabéns! Você acertou "${palavraSecreta}"!`;
        letraInput.disabled = true;
    }
}
