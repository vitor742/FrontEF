import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.18.0/firebase-app.js';
import { getFirestore, collection, query, where, getDocs } from 'https://www.gstatic.com/firebasejs/9.18.0/firebase-firestore.js';
import { getAuth} from 'https://www.gstatic.com/firebasejs/9.18.0/firebase-auth.js';

const firebaseConfig = {
    apiKey: "AIzaSyB-gb6WNxu7_stWtEmKPEcO17jr_h3C1cM",
    authDomain: "estoquefacil-7b03b.firebaseapp.com",
    projectId: "estoquefacil-7b03b",
    storageBucket: "estoquefacil-7b03b.firebasestorage.app",
    messagingSenderId: "201462826581",
    appId: "1:201462826581:web:d10a08a1380073fdcfb6dc"
  };

// Inicializa o Firebase NÃO MEXE PELO AMOR DE DEUS
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);


// Isso aqui é a lógica de login, se vc nao sabe oque tá fazendo (tipo eu), NÃO MEXE, ah e eu acho que tipo
// uma sessão nao tá sendo criada, depois eu olho isso

document.getElementById('loginForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const cpf = document.getElementById('access_key').value;

    try {
        const usersRef = collection(db, 'funcionarios');
        const q = query(usersRef, where('nome_funcionario', '==', username), where('cpf_funcionario', '==', cpf));
        const querySnapshot = await getDocs(q);

        if (!querySnapshot.empty) {
            console.log("Login bem-sucedido!");
            window.location.href = "/dashboard";
        } else {
            console.log("Credenciais inválidas.");
            let divMessage = document.querySelector(".loginMessage");
            divMessage.style.display = "flex";

            setTimeout(() => {
                divMessage.style.display = "none";
            }, 10000);
                    
            }
    } catch (error) {
        console.log("Erro ao tentar autenticar:", error);
    }
});