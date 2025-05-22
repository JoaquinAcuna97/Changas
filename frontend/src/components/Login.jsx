import React from "react";
import AuthForm from "./AuthForm";

export default function Login({ onSwitch }) {
  const fields = [
    { label: "Usuario (email)", name: "username", type: "email", autoComplete: "username" },
    { label: "Contraseña", name: "password", type: "password", autoComplete: "current-password" },
  ];

  const handleLogin = (form, setMessage) => {
    setMessage(`Iniciando sesión con ${form.username}...`);
    setTimeout(() => setMessage("Login exitoso! (simulado)"), 1000);
  };

  return (
    <AuthForm
      title="Iniciar Sesión"
      fields={fields}
      onSubmit={handleLogin}
      toggleText="¿No tienes cuenta?"
      onToggle={onSwitch}
    />
  );
}
