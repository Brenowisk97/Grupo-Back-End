# Grupo 1 - Projeto Back-End
Este é o repositório do grupo 1 de __Projeto Back-End__.


Ao longo do semestre, o grupo teve o objetivo de cumprir as atividades de __segmentação de imagens__ e também __anonimização de dados__ para a Dosimagem, empresa especializada em tratamento oncológico. A Dosimagem oferece contato com seus clientes 100% online, desde o envio das imagens médicas dos clientes até a emissão do relatório digital, agilizando todo o processo envolvido na medicina nuclear.


Para esse projeto, foi escolhida a linguagem _Python_, além de outras ferramentas como Pydicom, Insomnia e Flask:
 - Pydicom: Biblioteca em Python que permite manipular arquivos no formato DICOM
 - Insomnia: Framework web em Python que permite a criação de aplicação rapidamente e otimizada
 - Flask: Ferramenta para teste/validação de API e usado para requisições HTTP (GET, POST, DELETE)

Concluindo a AP1, foi possível anonomizar as imagens com sucesso com a integração, inclusiva, via API com o envio das imagens com o método POST e o código feito retornando uma nova imagem num diretório à parte com os principais metadadados pessoais e identificáveis dos pacientes sendo anonomizados.

Nesse sentido, para organização do projeto, o Trello foi escolhida como gerenciador de atividades e tarefas da disciplina. A ferramenta permite a criação de quadros e cartões que indicam o status de cada atividade, no contexto de seu responsável e etapa em que está inserida.

Para o Trello, criamos colunas específicas que ajudaram a agendar e definir, principalmente, as tarefas prioritárias, em estudo e futuras, presentes no link: https://trello.com/b/jedVnv7E/gerenciamento-projeto-back-end
 - Apresentação - AP2
 - Informações gerais
 - AP1
 - AP2
 - Em andamento
 - Concluído
 - Estudo
 - Encontros Virtuais

 Em relação a AP2, a projeto foi de segmentar as imagens para agilizar o processo da Dosimagem. Com o uso de Python, novamente, foi utilizada a biblioteca TotalSegmentator com o intuito de cumprir essas tarefas com a mesma ferramenta presente no 3DSlicer. Nesse sentido, é importante ressaltar que não foi possível criar API, uma vez que houve um problema com as imagens disponibilizadas causando atrasos no projeto da turma. 

 No entanto, foi possível concluir essas segmentações com sucesso, permitindo a particionar as imagens numa nova pasta.
