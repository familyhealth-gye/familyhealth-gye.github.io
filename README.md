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
- **Blog** (`BLOG` en `build.py`, 3 artículos): información general escrita sin revisión médica. Un médico del centro debe leer cada artículo antes de publicar.
- **Horario**: confirmado por el dueño 2026-11-25: L–V 8:30–19:00 (Maps), sáb. 9:00–16:00. Si Maps dice otra hora el sábado, corregir Maps.
- **Fotos** (`fotos/`): las que la clínica subió a su ficha de Maps, sin pacientes reales (la de consulta es con un creador de contenido que trabaja para el centro). Nunca agregar fotos donde se vea un paciente sin su consentimiento escrito.
- **Reseñas**: «4,9 · 81 opiniones» está escrito a mano (`RESENAS`); el chip enlaza a Google, donde siempre está el número real. Actualizarlo de vez en cuando.

## Publicar gratis (GitHub Pages)
1. En la cuenta `familyhealth-gye` crear un repo público llamado `familyhealth-gye.github.io`.
2. Subir el contenido de esta carpeta (menos `build.py` y `README.md` si prefieres).
3. En Settings → Pages: rama `main`, carpeta raíz.
4. En Google Maps (Editar perfil → Contacto) poner `https://familyhealth-gye.github.io/` como Sitio web.
5. En Search Console agregar el sitio y enviar `sitemap.xml`.

Si algún día compran dominio: cambiar `BASE` en `build.py`, regenerar y apuntar el dominio en Settings → Pages.
