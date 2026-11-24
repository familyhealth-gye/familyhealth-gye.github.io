# Sitio de Family Health (borrador)

Sitio estático para que Google y las IAs encuentren al centro por especialidad. Sin build ni dependencias: `python build.py` regenera todo.

## Cómo editar
Todo el contenido está en `build.py` (arriba: datos del centro, especialidades, preguntas frecuentes). Cambia el texto y vuelve a correr `python build.py`.

## Verificar antes de publicar (no inventé nada, pero no todo está confirmado)
- Servicios por especialidad: borra los que hoy no ofrezcan (Papanicolaou, control prenatal, ortodoncia, implantes, certificados, etc.).
- «Con cita previa»: confirmar que es así para todas las especialidades.
- Laboratorio clínico y Ecografía: texto genérico a propósito; ajustar a lo que de verdad hacen.
- Armonización orofacial y terapia física NO están en el sitio (publicidad estética sanitaria, revisar reglas antes).
- Sin número de permiso ACESS, sin precios, sin reseñas ni calificación en los datos estructurados (a propósito).
- El texto de cada especialidad lo debería revisar el abogado/DPO y un médico, como el resto de la app.

## Publicar gratis (GitHub Pages)
1. En la cuenta `familyhealth-gye` crear un repo público llamado `familyhealth-gye.github.io`.
2. Subir el contenido de esta carpeta (menos `build.py` y `README.md` si prefieres).
3. En Settings → Pages: rama `main`, carpeta raíz.
4. En Google Maps (Editar perfil → Contacto) poner `https://familyhealth-gye.github.io/` como Sitio web.
5. En Search Console agregar el sitio y enviar `sitemap.xml`.

Si algún día compran dominio: cambiar `BASE` en `build.py`, regenerar y apuntar el dominio en Settings → Pages.
