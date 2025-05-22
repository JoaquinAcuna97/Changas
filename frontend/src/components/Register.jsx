import React from "react";
import AuthForm from "./AuthForm";

export default function Register({ onSwitch }) {
  const fields = [
    { label: "Usuario (email)", name: "username", type: "email", autoComplete: "username" },
    { label: "Contraseña", name: "password", type: "password", autoComplete: "new-password" },
    { label: "Teléfono", name: "phone", type: "tel", autoComplete: "tel" },
  ];

  const handleRegister = (form, setMessage) => {
    setMessage(`Registrando usuario ${form.username} con teléfono ${form.phone}...`);
    setTimeout(() => setMessage("Registro exitoso! (simulado)"), 1000);
  };

  return (
    <AuthForm
      title="Registrarse"
      fields={fields}
      onSubmit={handleRegister}
      toggleText="¿Ya tienes cuenta?"
      onToggle={onSwitch}
    />
  );
}
