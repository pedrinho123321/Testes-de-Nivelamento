const { Client } = require("pg");
require("dotenv").config();

async function connectToDatabase() {
  const client = new Client({
    connectionString: process.env.DATABASE_URL,
  });

  try {
    await client.connect();
    console.log("Connected to database successfully");

    // Execute queries
    const lastQuarterQuery = `
      WITH last_quarter AS (
        SELECT MAX(data_trimestre) as max_date
        FROM demonstracoes_contabeis
      )
      SELECT 
        o.razao_social,
        dc.valor_conta as despesa_total
      FROM demonstracoes_contabeis dc
      JOIN operadoras o ON dc.registro_ans = o.registro_ans
      JOIN last_quarter lq ON dc.data_trimestre = lq.max_date
      WHERE dc.codigo_conta = '411X1'
      ORDER BY dc.valor_conta DESC
      LIMIT 10;
    `;

    const lastYearQuery = `
      WITH last_year AS (
        SELECT 
          registro_ans,
          SUM(valor_conta) as total_anual
        FROM demonstracoes_contabeis
        WHERE data_trimestre >= (SELECT MAX(data_trimestre) - INTERVAL '1 year' 
                               FROM demonstracoes_contabeis)
        AND codigo_conta = '411X1'
        GROUP BY registro_ans
      )
      SELECT 
        o.razao_social,
        ly.total_anual as despesa_total_anual
      FROM last_year ly
      JOIN operadoras o ON ly.registro_ans = o.registro_ans
      ORDER BY ly.total_anual DESC
      LIMIT 10;
    `;

    console.log(
      "\nTop 10 operadoras com maiores despesas no último trimestre:"
    );
    const quarterResult = await client.query(lastQuarterQuery);
    console.table(quarterResult.rows);

    console.log("\nTop 10 operadoras com maiores despesas no último ano:");
    const yearResult = await client.query(lastYearQuery);
    console.table(yearResult.rows);
  } catch (err) {
    console.error("Database connection error:", err);
  } finally {
    await client.end();
  }
}

connectToDatabase();
