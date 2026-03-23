# importar biblioteca
from flask import Flask, jsonify, render_template
# importe para documentacao
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# [flask routes] para listar rotas da api

# criar variavel para receber a classe Flask
app = Flask(__name__)

#   documentacao OpenAPI
spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)

@app.route('/validade/<data_informada/<int:quantidade>/<prazo-*>')
def validado(quantidade, prazo):
    """
        **API para calcular cashback**

        ##ENdpoint:
        GET/validade

        ## Parámetros
        {
            "produto": "Arroz",
            "prazo": "26/07/2026","

        }

        ## Resposta (JSON)
        {
                "validade: "26/07/2026 12:43:41",
                "data_transacao_iso": "2026-07-26T12:43:41",
                "produto": "Arroz",
            }

        """
    prazo = int(prazo)
    quantidade = int(quantidade)
    meses = datetime.today()+relativedelta(months=prazo)
    # years=
    anos = datetime.today()+relativedelta(years=prazo)
    # weeks=
    semanas = datetime.today()+relativedelta(weeks=prazo)
    # days=
    dias = datetime.today()+relativedelta(days=prazo)

    dias = (prazo - dias).days
    semanas = (prazo - semanas).weeks
    meses = (prazo - meses).months
    anos = (prazo - anos).years
    print(f'{dias}')
    print(f'{semanas}')
    print(f'{meses}')
    print(f'{anos}')


    return (f'"antes" - {datetime.today().strftime("%d-%m-%Y")}, '
            f'"dias"- {dias}, '
            f'"semanas"- {semanas}, '
            f'"meses"- {meses},'
            f'"anos"- {anos}')


# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)