const express = require("express");
const multer = require("multer");
const cors = require("cors");
const path = require("path");
const fs = require("fs");

const app = express();
const port = 3000;

app.use(cors());

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "../spreadsheets");
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  },
});

const upload = multer({
  storage: storage,
  fileFilter: (req, file, cb) => {
    const allowedFileTypes = [".xlsx", ".xls"];
    const fileType = path.extname(file.originalname).toLowerCase();
    if (allowedFileTypes.includes(fileType)) {
      cb(null, true);
    } else {
      cb(new Error("Error: Only excel files are allowed!"));
    }
  },
  limits: {
    fileSize: 1024 * 1024 * 10, // Limitar o tamanho do arquivo para 10 MB
  },
});

app.post("/upload", upload.single("excelFile"), (req, res) => {
  // lógica para apagar se houver um arquivo existente
  console.log("sucess");
  res.json({ msg: "sucess" }).status(200);
});

// rota de delete para o arquivo

app.listen(port, () => console.log(`Server running on port ${port}`));
