// Builds one transparent PNG per technology: the official wordmark where one exists, otherwise the
// official symbol locked up with the brand name. No version numbers or years.
import fs from "fs";
import { createRequire } from "module";
const require = createRequire(import.meta.url);
const L = require("@iconify-json/logos/icons.json");
const SI = "node_modules/simple-icons/icons/";
const SIDATA = JSON.parse(fs.readFileSync("node_modules/simple-icons/_data/simple-icons.json","utf8"));
const siColor = slug => { const all = SIDATA.icons || SIDATA; const e = all.find(i => (i.slug || i.title.toLowerCase().replace(/[^a-z0-9]/g,"")) === slug); return e ? "#" + e.hex : "#111111"; };
const DV = "node_modules/devicon/icons/";
const logos = (id) => { const ic = L.icons[id] || L.icons[(L.aliases[id]||{}).parent]; const w = ic.width || L.width || 256, h = ic.height || L.height || 256;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${ic.left||0} ${ic.top||0} ${w} ${h}" width="${w}" height="${h}">${ic.body}</svg>`; };
const devicon = (p) => fs.readFileSync(DV + p, "utf8");
const lockup = (slug, name, color) => { const svg = fs.readFileSync(SI + slug + ".svg", "utf8"); const path = svg.match(/<path d="([^"]+)"/)[1]; const c = color || siColor(slug);
  const tw = Math.round(name.length * 10.6 + 8);
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${34 + tw} 26" width="${(34 + tw)*4}" height="104"><g transform="translate(0,1)"><path fill="${c}" d="${path}"/></g><text x="32" y="18.4" font-family="Inter" font-weight="500" font-size="15.5" fill="#1d2433" letter-spacing="-0.2">${name}</text></svg>`; };
const ext = (f) => fs.readFileSync("ext/" + f, "utf8");
// Lock up any full icon SVG (nested) with the brand name, for brands whose official mark is a symbol only.
const lockSvg = (iconSvg, name) => { const tw = Math.round(name.length * 10.6 + 8);
  const inner = iconSvg.replace(/<\?xml[^>]*>/, "").replace(/<!DOCTYPE[^>]*>/, "").replace(/<svg([^>]*)>/, (m, a) => '<svg x="0" y="0" width="26" height="26"' + (/viewBox/.test(a) ? "" : ` viewBox="0 0 ${(a.match(/width="(\d+)/)||[0,200])[1]} ${(a.match(/height="(\d+)/)||[0,200])[1]}"`) + a.replace(/\s(width|height|x|y)="[^"]*"/g, "") + '>');
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${34 + tw} 26" width="${(34 + tw)*4}" height="104">${inner}<text x="32" y="18.4" font-family="Inter" font-weight="500" font-size="15.5" fill="#1d2433" letter-spacing="-0.2">${name}</text></svg>`; };
export const ROWS = {
  platforms: [
    ["aws", "AWS", () => logos("aws")], ["azure", "Microsoft Azure", () => lockSvg(logos("microsoft-azure"), "Microsoft Azure")], ["gcp", "Google Cloud", () => lockSvg(logos("google-cloud"), "Google Cloud")],
    ["snowflake", "Snowflake", () => logos("snowflake")], ["databricks", "Databricks", () => lockup("databricks", "Databricks")],
    ["fabric", "Microsoft Fabric", () => lockSvg(ext("fabric_icon.svg").replace(/fill="currentColor"/, ""), "Microsoft Fabric")], ["powerbi", "Power BI", () => lockSvg(logos("microsoft-power-bi"), "Power BI")],
    ["bigquery", "BigQuery", () => lockup("googlebigquery", "BigQuery", "#669DF6")], ["redshift", "Amazon Redshift", () => lockup("amazonredshift", "Amazon Redshift")],
    ["tableau", "Tableau", () => logos("tableau")], ["looker", "Looker", () => logos("looker")], ["qlik", "Qlik", () => logos("qlik")],
    ["grafana", "Grafana", () => lockSvg(logos("grafana"), "Grafana")], ["superset", "Apache Superset", () => lockup("apachesuperset", "Superset")], ["metabase", "Metabase", () => lockup("metabase", "Metabase")],
    ["sap", "SAP", () => logos("sap")], ["siemens", "Siemens", () => { const d = fs.readFileSync(SI + "siemens.svg", "utf8").match(/<path d="([^"]+)"/)[1]; return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 9 24 6.2"><path fill="#009999" d="${d}"/></svg>`; }], ["rockwell", "Rockwell Automation", () => lockup("rockwellautomation", "Rockwell Automation")],
    ["honeywell", "Honeywell", () => ext("honeywell.svg")], ["mqtt", "MQTT", () => lockup("mqtt", "MQTT")], ["nodered", "Node-RED", () => lockup("nodered", "Node-RED")],
    ["whatsapp", "WhatsApp", () => lockSvg(logos("whatsapp-icon"), "WhatsApp")],
  ],
  data: [
    ["spark", "Apache Spark", () => logos("apache-spark")], ["kafka", "Apache Kafka", () => logos("kafka")], ["confluent", "Confluent", () => lockSvg(ext("confluent.svg"), "Confluent")],
    ["flink", "Apache Flink", () => lockSvg(logos("apache-flink-icon"), "Apache Flink")], ["airflow", "Apache Airflow", () => logos("airflow")], ["dbt", "dbt", () => logos("dbt")],
    ["deltalake", "Delta Lake", () => lockSvg(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 35 35"><path fill="#00ADD4" d="${ext("delta_glyph.path").trim()}"/></svg>`, "Delta Lake")], ["iceberg", "Apache Iceberg", () => lockSvg(ext("apache-iceberg.svg"), "Apache Iceberg")], ["trino", "Trino", () => lockup("trino", "Trino")],
    ["clickhouse", "ClickHouse", () => lockup("clickhouse", "ClickHouse", "#FAFF69")], ["duckdb", "DuckDB", () => lockup("duckdb", "DuckDB")], ["nifi", "Apache NiFi", () => lockup("apachenifi", "Apache NiFi")],
    ["hadoop", "Apache Hadoop", () => lockup("apachehadoop", "Hadoop")], ["fivetran", "Fivetran", () => ext("fivetran.svg")], ["airbyte", "Airbyte", () => lockup("airbyte", "Airbyte")],
    ["matillion", "Matillion", () => lockup("matillion", "Matillion")], ["informatica", "Informatica", () => lockup("informatica", "Informatica")], ["talend", "Talend", () => lockup("talend", "Talend")],
    ["postgresql", "PostgreSQL", () => lockSvg(logos("postgresql"), "PostgreSQL")], ["oracle", "Oracle", () => logos("oracle")], ["sqlserver", "SQL Server", () => lockSvg(devicon("microsoftsqlserver/microsoftsqlserver-plain.svg"), "SQL Server")],
    ["mongodb", "MongoDB", () => logos("mongodb")], ["redis", "Redis", () => lockSvg(logos("redis"), "Redis")], ["elasticsearch", "Elasticsearch", () => lockSvg(logos("elasticsearch"), "Elasticsearch")],
    ["neo4j", "Neo4j", () => logos("neo4j")], ["influxdb", "InfluxDB", () => logos("influxdb")],
  ],
  ai: [
    ["python", "Python", () => lockSvg(logos("python"), "Python")], ["pytorch", "PyTorch", () => logos("pytorch")], ["tensorflow", "TensorFlow", () => lockSvg(logos("tensorflow"), "TensorFlow")],
    ["sklearn", "scikit-learn", () => devicon("scikitlearn/scikitlearn-original.svg")], ["pandas", "pandas", () => logos("pandas")], ["numpy", "NumPy", () => lockSvg(logos("numpy"), "NumPy")],
    ["opencv", "OpenCV", () => lockSvg(devicon("opencv/opencv-original.svg"), "OpenCV")], ["nvidia", "NVIDIA", () => logos("nvidia")], ["huggingface", "Hugging Face", () => lockup("huggingface", "Hugging Face")],
    ["openai", "OpenAI", () => logos("openai")], ["anthropic", "Anthropic", () => logos("anthropic")], ["gemini", "Google Gemini", () => logos("google-gemini")],
    ["langchain", "LangChain", () => lockup("langchain", "LangChain")], ["ollama", "Ollama", () => lockup("ollama", "Ollama")], ["mlflow", "MLflow", () => lockup("mlflow", "MLflow")],
    ["kubeflow", "Kubeflow", () => lockSvg(ext("kubeflow_icon.svg"), "Kubeflow")], ["ray", "Ray", () => lockup("ray", "Ray")], ["onnx", "ONNX", () => lockup("onnx", "ONNX")],
    ["pinecone", "Pinecone", () => logos("pinecone")], ["qdrant", "Qdrant", () => logos("qdrant")], ["jupyter", "Jupyter", () => lockSvg(devicon("jupyter/jupyter-original.svg"), "Jupyter")],
    ["docker", "Docker", () => logos("docker")], ["kubernetes", "Kubernetes", () => lockSvg(logos("kubernetes"), "Kubernetes")], ["terraform", "Terraform", () => logos("terraform")],
    ["githubactions", "GitHub Actions", () => lockSvg(logos("github-actions"), "GitHub Actions")], ["prometheus", "Prometheus", () => lockSvg(logos("prometheus"), "Prometheus")], ["fastapi", "FastAPI", () => logos("fastapi")],
    ["django", "Django", () => logos("django")], ["nodejs", "Node.js", () => logos("nodejs")], ["react", "React", () => lockup("react", "React")],
  ],
};
if (process.argv[2] === "write") {
  fs.mkdirSync("svg", { recursive: true }); const miss = [];
  for (const [row, items] of Object.entries(ROWS)) for (const [id, name, fn] of items) {
    try { fs.writeFileSync(`svg/${id}.svg`, fn()); } catch (e) { miss.push(id + " (" + e.message.slice(0, 40) + ")"); }
  }
  fs.writeFileSync("rows.json", JSON.stringify(Object.fromEntries(Object.entries(ROWS).map(([r, it]) => [r, it.map(([id, name]) => ({ id, name }))])), null, 1));
  console.log("missing:", miss.join(", "));
}
