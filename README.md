# 🐸 JFrog Connect – Hello World

Aplicación "Hola Mundo" containerizada y lista para desplegarse en **JFrog Container Registry**.

---

## 📂 Estructura del proyecto

```
.
├── app/
│   └── main.py                 # Aplicación Python (servidor HTTP)
├── .github/
│   └── workflows/
│       └── jfrog-deploy.yml    # CI/CD – build & push a JFrog
├── Dockerfile                  # Imagen del contenedor
├── .dockerignore
├── docker-compose.yml          # Ejecución local
└── README.md
```

---

## 🚀 Desarrollo local

### Opción 1 – Python directo

```bash
python app/main.py
# → http://localhost:8080
```

### Opción 2 – Docker

```bash
docker build -t hello-world-app .
docker run -p 8080:8080 hello-world-app
# → http://localhost:8080
```

### Opción 3 – Docker Compose

```bash
docker compose up --build
# → http://localhost:8080
```

---

## ⚙️ Configuración DevOps – Despliegue a JFrog

### 1. Prerrequisitos en JFrog

1. Tener una instancia de JFrog (SaaS o self-hosted).
2. Crear un **Docker Repository** (ej: `docker-local`) en:
   `Administration → Repositories → Local → Docker`.
3. Crear un usuario o API Key con permisos de push al repo.

### 2. Secrets de GitHub

Ir a **GitHub → Repo → Settings → Secrets and variables → Actions** y crear:

| Secret           | Ejemplo                         | Descripción                              |
|------------------|---------------------------------|------------------------------------------|
| `JFROG_URL`      | `https://miempresa.jfrog.io`    | URL base de tu instancia JFrog           |
| `JFROG_USER`     | `deployer`                      | Usuario con permisos de push             |
| `JFROG_PASSWORD`  | `AKCp8...`                      | Contraseña o API Key                     |
| `JFROG_REPO`     | `docker-local`                  | Nombre del Docker repository en JFrog    |

### 3. Flujo CI/CD

```
push a main → GitHub Actions → Build imagen → Push a JFrog Container Registry
```

El workflow (`.github/workflows/jfrog-deploy.yml`) hace:

1. **Test**: Verifica que la app importa correctamente.
2. **Build**: Construye la imagen Docker con dos tags (`latest` + SHA del commit).
3. **Push**: Sube la imagen al registry de JFrog.
4. **Build Info**: Publica metadatos del build en JFrog para trazabilidad.

### 4. Verificar en JFrog

Después del primer push exitoso:

1. Ir a **Application → Artifactory → Artifacts**.
2. Navegar al repo `docker-local` → `hello-world-app`.
3. Verás los tags `latest` y el SHA del commit.

### 5. Pull de la imagen desde JFrog

```bash
docker login miempresa.jfrog.io
docker pull miempresa.jfrog.io/docker-local/hello-world-app:latest
docker run -p 8080:8080 miempresa.jfrog.io/docker-local/hello-world-app:latest
```

---

## 🔗 Diagrama de flujo

```
┌──────────┐     push      ┌──────────────┐    docker push    ┌─────────────────┐
│  Dev      │──────────────▶│ GitHub       │──────────────────▶│ JFrog           │
│  (código) │               │ Actions      │                   │ Container       │
└──────────┘               │ (build img)  │                   │ Registry        │
                           └──────────────┘                   └────────┬────────┘
                                                                       │ docker pull
                                                                       ▼
                                                              ┌─────────────────┐
                                                              │ Cualquier host  │
                                                              │ (run container) │
                                                              └─────────────────┘
```

---

## 📝 Notas

- La app usa **solo la stdlib de Python** — cero dependencias externas.
- El Dockerfile crea un **usuario no-root** por seguridad.
- Incluye **HEALTHCHECK** para orquestadores como Kubernetes.
- El tag `latest` se actualiza en cada push a `main`; el tag SHA permite rollback.