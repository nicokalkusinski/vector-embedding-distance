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

def list2md(content: list[str]):
    for item in content:
        split_item = item.split("**")
        title = split_item[1]
        description = split_item[2]
        # save to md file
        with open(f"md_files/[Servicios] {title}.md", "w", encoding="utf-8") as file:
            file.write(f"# {title}\n{description}")

list2md(split_content)