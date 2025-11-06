# Projeto: Simulação Ransomware & Keylogger (SAFE MODE)

> **Aviso:** Projeto educacional. **Execute apenas em uma máquina isolada (VM) e com backups/snapshots.**

## Objetivos
- Conceitos de impacto de ransomware e keyloggers em ambiente controlado.
- Praticar técnicas defensivas: monitoramento de integridade, identificação de anomalias e recuperação.
- Documentar aprendizados e gerar material para portfólio.

## Estrutura do repositório
- `create_test_files.py` — cria arquivos de teste no sandbox.
- `simulate_ransom_safe.py` — **simulação segura**: renomeia arquivos (marca como "ENCRYPTED_SIM") e gera manifesto JSON para restauração.
- `simulate_keylogger_generator.py` — gera um arquivo de log de teclas sintético (sem capturar teclas reais).
- `checksum_monitor.py` — monitora integridade via checksums e detecta alterações.
- `images/` — capturas de tela de experimentos.

## Como executar (passos seguros)
1. Crie uma VM isolada e faça snapshot.
2. Clone este repo na VM.
3. Defina um diretório de sandbox (ex.: `/home/user/sandbox`) e abra um terminal nessa VM.
4. Rode:
   ```bash
   python3 create_test_files.py /caminho/para/sandbox
   python3 checksum_monitor.py init /caminho/para/sandbox       # cria baseline
   python3 simulate_ransom_safe.py /caminho/para/sandbox       # simulação segura
   python3 checksum_monitor.py check /caminho/para/sandbox     # detecta alterações
   python3 simulate_ransom_safe.py --restore /caminho/para/sandbox # restaura usando manifesto
   python3 simulate_keylogger_generator.py /caminho/para/sandbox # gera log sintético
