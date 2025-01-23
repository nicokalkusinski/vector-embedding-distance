from openai import OpenAI
from modules import tools, math

client = OpenAI(api_key=tools.load_api_key())

def get_embedding(word, model="text-embedding-3-small"):
    """
    Get the embedding for a given word using the specified model.
    """
    response = client.embeddings.create(
        input=word,
        model=model
    )

    return response.data[0].embedding

def compare(content1, content2, method=3):
    """
    Compare two words using OpenAI embeddings and return their similarity score.
    """
    embedding1 = get_embedding(content1)
    embedding2 = get_embedding(content2)
    if method==1:
        print("Using Euclidean Distance.")
        similarity = math.euclidean_distance(embedding1, embedding2)
        print(f"Result: {similarity:.6f}")
        return similarity
    elif method==2:
        print("Using Cosine Similarity.")
        similarity = math.cosine_similarity(embedding1, embedding2)
        print(f"Result: {similarity:.6f}")
        return similarity
    else:
        print("Using Euclidean Distance and Cosine Similarity.")
        sim1, sim2 = math.euclidean_distance(embedding1, embedding2), math.cosine_similarity(embedding1, embedding2)
        print(f"Euclidean Distance: {sim1:.6f}")
        print(f"Cosine Similarity: {sim2:.6f}")
        return sim1, sim2

# Example usage
# load md files with tools.load_md_file("file_path")
all_content = """
#Servicios que ofrece Neotic

**Los servicios ofrecidos por el programa Kit Digital**
-Neotic actúa como agente digitalizador del programa Kit Digital, permitiendo que las empresas accedan a soluciones digitales mediante subvenciones gubernamentales. Neotic implementa diversas estrategias y soluciones digitales financiadas a través del programa Kit Digital.

**Los servicios ofrecidos por el programa Kit Consulting**
-Neotic actúa como agente consultor del programa Kit Consulting, que otorga subvenciones para ayudar a las empresas a realizar una consultoría. Las soluciones que ofrece este programa se pueden ver en su correspondiente catálogo.

**Servicios en la Nube**
-Proporciona servicios en la nube de Microsoft para mejorar la productividad, seguridad y confiabilidad organizacional.

**Soluciones CRM**
-Implementa la plataforma no-code de CRM llamada Creatio para gestionar y automatizar las operaciones empresariales, incluyendo consolidación y gestión de datos del cliente, automatización de flujos de trabajo, pronósticos de ventas, administración de contratos y análisis predictivos.

**Ciberseguridad**
Ofrece servicios integrales de ciberseguridad para proteger datos y operaciones empresariales contra amenazas cibernéticas, a través de medidas avanzadas y asociaciones con empresas tecnológicas líderes como Sophos.
Las soluciones integrales de ciberseguridad que incluyen son:
-Herramientas antimalware.
-Soluciones de Control de Acceso a la Red (NAC).
-Cifrado y protección de datos.
-Pentesting (Pruebas de Penetración).
-Seguridad Perimetral.
-Auditoría y monitorización de archivos.

**Soluciones de Respaldo**
-Brinda soluciones de respaldo y recuperación de datos utilizando el ecosistema híbrido en la nube de Syneto, que incluye protección contra ransomware de datos basada en IA.
-Soluciones de Veeam para respaldo, recuperación y gestión de datos.

**Marketing y Comercio Electrónico**
Estrategias de marketing digital que incluyen:
-Optimización SEO.
-Gestión de redes sociales.
-Campañas de email marketing.
-Diseño web y creación de plataformas de comercio electrónico.

**Servicios de TI e Infraestructura**
-Soporte de TI, mantenimiento de hardware y actualizaciones de sistemas mediante servicios de alquiler.
-Creación y mantenimiento de páginas web e infraestructura de TI.
-Mantenimiento de TI
-Implementación de infraestructura tecnológica mediante servicios de alquiler.

**Facturación Electrónica (E-Factura)**
Ayuda a las empresas a cumplir con los requisitos obligatorios de facturación electrónica.
Ofrece soluciones alineadas con la Ley Crea y Crece para facilitar las transacciones electrónicas.

**Soluciones de Oficina Flexible**
Proporciona soluciones de oficina virtual para el trabajo remoto, incluyendo comunicaciones seguras y gestión de datos.

**Recuperación de Datos**
Servicios de recuperación de datos para restaurar información perdida de diversos dispositivos.

**Soluciones para Presencia Social**
Mejora la visibilidad empresarial online mediante estrategias de redes sociales y participación pública."""

focused_content = """
#Servicios y productos de neotic, que neotic ofrece?
- **Los servicios ofrecidos por el programa Kit Digital**
- **Los servicios ofrecidos por el programa Kit Consulting**
- **Servicios en la Nube**
- **Soluciones CRM**
- **Ciberseguridad**
- **Soluciones de Respaldo**
- **Marketing y Comercio Electrónico**
- **Servicios de TI e Infraestructura**
- **Facturación Electrónica (E-Factura)**
- **Soluciones de Oficina Flexible**
- **Recuperación de Datos**
- **Soluciones para Presencia Social**
"""

tagged_content = """
#Servicios y productos de neotic, que neotic ofrece?
- **Los servicios ofrecidos por el programa Kit Digital**
- **Los servicios ofrecidos por el programa Kit Consulting**
- **Servicios en la Nube**
- **Soluciones CRM**
- **Ciberseguridad**
- **Soluciones de Respaldo**
- **Marketing y Comercio Electrónico**
- **Servicios de TI e Infraestructura**
- **Facturación Electrónica (E-Factura)**
- **Soluciones de Oficina Flexible**
- **Recuperación de Datos**
- **Soluciones para Presencia Social**

Servicios digitales, Kit Digital, Kit Consulting, servicios en la nube, soluciones CRM, ciberseguridad, soluciones de respaldo, marketing digital, comercio electrónico, servicios de TI, infraestructura tecnológica, facturación electrónica, oficina virtual, recuperación de datos, presencia online
"""
query = "Que servicios neotic ofrece?"

split_content = [
    "**Los servicios ofrecidos por el programa Kit Digital**\n-Neotic actúa como agente digitalizador del programa Kit Digital, permitiendo que las empresas accedan a soluciones digitales mediante subvenciones gubernamentales. Neotic implementa diversas estrategias y soluciones digitales financiadas a través del programa Kit Digital.",
    
    "**Los servicios ofrecidos por el programa Kit Consulting**\n-Neotic actúa como agente consultor del programa Kit Consulting, que otorga subvenciones para ayudar a las empresas a realizar una consultoría. Las soluciones que ofrece este programa se pueden ver en su correspondiente catálogo.",
    
    "**Servicios en la Nube**\n-Proporciona servicios en la nube de Microsoft para mejorar la productividad, seguridad y confiabilidad organizacional.",
    
    "**Soluciones CRM**\n-Implementa la plataforma no-code de CRM llamada Creatio para gestionar y automatizar las operaciones empresariales, incluyendo consolidación y gestión de datos del cliente, automatización de flujos de trabajo, pronósticos de ventas, administración de contratos y análisis predictivos.",
    
    "**Ciberseguridad**\nOfrece servicios integrales de ciberseguridad para proteger datos y operaciones empresariales contra amenazas cibernéticas, a través de medidas avanzadas y asociaciones con empresas tecnológicas líderes como Sophos.\nLas soluciones integrales de ciberseguridad que incluyen son:\n-Herramientas antimalware.\n-Soluciones de Control de Acceso a la Red (NAC).\n-Cifrado y protección de datos.\n-Pentesting (Pruebas de Penetración).\n-Seguridad Perimetral.\n-Auditoría y monitorización de archivos.",
    
    "**Soluciones de Respaldo**\n-Brinda soluciones de respaldo y recuperación de datos utilizando el ecosistema híbrido en la nube de Syneto, que incluye protección contra ransomware de datos basada en IA.\n-Soluciones de Veeam para respaldo, recuperación y gestión de datos.",
    
    "**Marketing y Comercio Electrónico**\nEstrategias de marketing digital que incluyen:\n-Optimización SEO.\n-Gestión de redes sociales.\n-Campañas de email marketing.\n-Diseño web y creación de plataformas de comercio electrónico.",
    
    "**Servicios de TI e Infraestructura**\n-Soporte de TI, mantenimiento de hardware y actualizaciones de sistemas mediante servicios de alquiler.\n-Creación y mantenimiento de páginas web e infraestructura de TI.\n-Mantenimiento de TI.\n-Implementación de infraestructura tecnológica mediante servicios de alquiler.",
    
    "**Facturación Electrónica (E-Factura)**\nAyuda a las empresas a cumplir con los requisitos obligatorios de facturación electrónica.\nOfrece soluciones alineadas con la Ley Crea y Crece para facilitar las transacciones electrónicas.",
    
    "**Soluciones de Oficina Flexible**\nProporciona soluciones de oficina virtual para el trabajo remoto, incluyendo comunicaciones seguras y gestión de datos.",
    
    "**Recuperación de Datos**\nServicios de recuperación de datos para restaurar información perdida de diversos dispositivos.",
    
    "**Soluciones para Presencia Social**\nMejora la visibilidad empresarial online mediante estrategias de redes sociales y participación pública."
]


print("=== all vs. query ===")
res1 = compare(all_content, query)

print("=== focused vs. query ===")
res2 = compare(focused_content, query)

print("=== tagged vs. query ===")
res3 = compare(focused_content, query)

print("=== Summary ===")

percent = ((res2[1]-res1[1])/res1[1])*100
print(f"Focused is {percent:.2f}% better than all content.")

percent = ((res3[1]-res1[1])/res1[1])*100
print(f"Tagged is {percent:.2f}% better than all content.")

percent = ((res3[1]-res2[1])/res1[1])*100
print(f"Tagged is {percent:.2f}% better than Focused.")

print("=== Split content ===")
query = "necesito servicios de ciberseguridad para mi empresa"
for content in split_content:
    print(f"=== query vs. {content[:30]} ===")
    compare(content, query)