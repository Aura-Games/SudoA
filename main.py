import dash
import shell


dash_shell = shell.ShellEnvironment("dash", dash.dash_commands)

dash_shell.main_loop()
