const form = document.getElementById("analyzeForm");
const output = document.getElementById("output");
const textResult = document.getElementById("textResult");
const cyContainer = document.getElementById("cy");

form.onsubmit = async (e) => {
  e.preventDefault();
  output.classList.add("d-none");
  textResult.innerHTML = "Processando...";

  const formData = new FormData(form);
  try {
    const response = await fetch("http://localhost:8001/analisar_ameacas/", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    let texto = data.choices?.[0]?.message?.content || JSON.stringify(data);
    textResult.innerText = texto.trim();

    const cy = cytoscape({
      container: cyContainer,
      style: [
        {
          selector: "node",
          style: {
            "background-color": "#0078D4",
            label: "data(label)",
            color: "#fff",
            "text-valign": "center",
            "text-halign": "center",
            "font-size": "10px",
            width: "label",
            height: "label",
            padding: "10px",
          },
        },
        {
          selector: "edge",
          style: {
            width: 2,
            "line-color": "#999",
            "target-arrow-color": "#999",
            "target-arrow-shape": "triangle",
            "curve-style": "bezier",
            label: "data(label)",
            "font-size": "8px",
            "text-rotation": "autorotate",
            color: "#555",
          },
        },
      ],
      elements: {
        nodes: [
          { data: { id: "Usuario", label: "Usuário" } },
          { data: { id: "EasyAuth", label: "Easy Auth" } },
          { data: { id: "AppService", label: "App Service" } },
          { data: { id: "SQL", label: "Azure SQL" } },
          { data: { id: "EntraID", label: "Entra ID" } },
          { data: { id: "Monitor", label: "Monitoramento" } },

          { data: { id: "Spoofing1", label: "Spoofing: Token roubado" } },
          { data: { id: "Spoofing2", label: "Spoofing: Conta falsa" } },
          {
            data: {
              id: "Tampering1",
              label: "Tampering: Req. modificada",
            },
          },
          {
            data: {
              id: "Tampering2",
              label: "Tampering: Banco alterado",
            },
          },
          {
            data: {
              id: "Repudiation1",
              label: "Repudiation: Ação negada",
            },
          },
          { data: { id: "Info1", label: "Disclosure: Vazamento" } },
          { data: { id: "DoS1", label: "DoS: Sobrecarga" } },
          { data: { id: "Privilege1", label: "EoP: Acesso admin" } },
        ],
        edges: [
          {
            data: {
              source: "Usuario",
              target: "EasyAuth",
              label: "acessa",
            },
          },
          {
            data: {
              source: "EasyAuth",
              target: "AppService",
              label: "autoriza",
            },
          },
          {
            data: {
              source: "AppService",
              target: "SQL",
              label: "consulta",
            },
          },
          {
            data: {
              source: "AppService",
              target: "Monitor",
              label: "log",
            },
          },
          {
            data: {
              source: "EasyAuth",
              target: "EntraID",
              label: "identidade",
            },
          },

          { data: { source: "Spoofing1", target: "EasyAuth" } },
          { data: { source: "Spoofing2", target: "AppService" } },
          { data: { source: "Tampering1", target: "AppService" } },
          { data: { source: "Tampering2", target: "SQL" } },
          { data: { source: "Repudiation1", target: "AppService" } },
          { data: { source: "Info1", target: "SQL" } },
          { data: { source: "DoS1", target: "AppService" } },
          { data: { source: "Privilege1", target: "AppService" } },
        ],
      },
      layout: {
        name: "cose",
        padding: 20,
      },
    });

    output.classList.remove("d-none");
  } catch (err) {
    textResult.innerText = "Erro ao processar: " + err;
    output.classList.remove("d-none");
  }
};

// Adiciona funcionalidade ao botão de impressão do grafo
const printBtn = document.getElementById("printGraph");
if (printBtn) {
  printBtn.onclick = function () {
    const cyElement = document.getElementById("cy");
    const printWindow = window.open("", "", "width=900,height=700");
    printWindow.document.write(
      "<html><head><title>Imprimir Grafo STRIDE</title>"
    );
    printWindow.document.write(
      "<style>body{margin:0;}#cy{width:100vw;height:90vh;}</style>"
    );
    printWindow.document.write("</head><body>");

    // Clona o grafo como imagem
    const cyCanvas = cyElement.querySelector("canvas");
    if (cyCanvas) {
      const imgData = cyCanvas.toDataURL("image/png");
      printWindow.document.write(
        '<img src="' + imgData + '" style="width:100%;height:auto;"/>'
      );
    } else {
      printWindow.document.write(
        "<div>Não foi possível capturar o grafo.</div>"
      );
    }
    printWindow.document.write("</body></html>");
    printWindow.document.close();
    printWindow.focus();
    printWindow.print();
  };
}