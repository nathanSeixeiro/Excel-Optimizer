const fs = require("fs");
const path = require("path");

const pasta = "../../../spreadsheets";
const nomeArquivo = "JOACIR ROCHA JANEIRO 24.xlsx";
const caminhoArquivo = path.join(pasta, nomeArquivo);

// Verificar se o arquivo existe
fs.access(caminhoArquivo, fs.constants.F_OK, (err) => {
  if (!err) {
    // Se o arquivo existe, apagá-lo
    fs.unlink(caminhoArquivo, (err) => {
      if (err) {
        console.error("Erro ao apagar o arquivo:", err);
      } else {
        console.log("Arquivo apagado com sucesso.");
      }
    });
  } else {
    console.log("O arquivo não existe.");
  }
});
