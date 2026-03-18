import os
import time

class SistemaExpertoMetodologias:
    def __init__(self):
        self.hechos = {}
        self.conclusiones = {}
        self.traza = []
        self.reglas = self.definir_reglas()

    def limpiar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def definir_reglas(self):
        return [
            # SCRUM (metodología ágil más popular)
            {'id': 1, 'premisas': [('tamano', 'mediano'), ('requisitos', 'cambiantes')], 
             'conclusion': 'Scrum', 'certeza': 0.85},
            {'id': 2, 'premisas': [('tamano', 'grande'), ('requisitos', 'cambiantes'), ('experiencia_agil', 'si')], 
             'conclusion': 'Scrum', 'certeza': 0.80},
            
            # WATERFALL (tradicional)
            {'id': 3, 'premisas': [('requisitos', 'estables'), ('contrato', 'fijo')], 
             'conclusion': 'Waterfall', 'certeza': 0.90},
            {'id': 4, 'premisas': [('tamano', 'grande'), ('documentacion', 'importante')], 
             'conclusion': 'Waterfall', 'certeza': 0.75},
            
            # KANBAN (flujo continuo)
            {'id': 5, 'premisas': [('tipo', 'soporte'), ('prioridades', 'cambian')], 
             'conclusion': 'Kanban', 'certeza': 0.88},
            {'id': 6, 'premisas': [('equipo', 'pequeno'), ('entregas', 'continuas')], 
             'conclusion': 'Kanban', 'certeza': 0.82},
            
            # XP (prácticas técnicas)
            {'id': 7, 'premisas': [('requisitos', 'muy_cambiantes'), ('calidad', 'critica')], 
             'conclusion': 'XP', 'certeza': 0.87},
            {'id': 8, 'premisas': [('equipo', 'pequeno'), ('requisitos', 'muy_cambiantes')], 
             'conclusion': 'XP', 'certeza': 0.85},
            
            # Metodología híbrida (por defecto para casos no cubiertos)
            {'id': 9, 'premisas': [('tamano', 'pequeno'), ('requisitos', 'estables')], 
             'conclusion': 'Híbrida (Scrum + Kanban)', 'certeza': 0.70},
            {'id': 10, 'premisas': [('tamano', 'mediano'), ('requisitos', 'estables')], 
             'conclusion': 'Híbrida (Waterfall + Ágil)', 'certeza': 0.65},
        ]

    def mostrar_titulo(self, texto):
        print(f"\n{'='*60}")
        print(f" {texto}")
        print(f"{'='*60}")

    def mostrar_info(self, texto):
        print(f"📌 {texto}")

    def preguntar_con_info(self, pregunta, info, opciones):
        print(f"\n❓ {pregunta}")
        self.mostrar_info(info)
        for key, (texto, _) in opciones.items():
            print(f"   {key}. {texto}")
        
        while True:
            resp = input("👉 Selecciona una opción: ").strip()
            if resp in opciones:
                return opciones[resp][1]
            print("⚠️ Opción inválida, intenta de nuevo")

    def preguntar_si_no(self, pregunta, info):
        print(f"\n❓ {pregunta}")
        self.mostrar_info(info)
        while True:
            resp = input("👉 (s/n): ").strip().lower()
            if resp in ['s', 'n']:
                return resp == 's'
            print("⚠️ Ingresa 's' o 'n'")

    def recolectar_datos(self):
        self.limpiar()
        self.mostrar_titulo("📋 CUESTIONARIO SOBRE TU PROYECTO")
        print("\nResponde las siguientes preguntas para recomendarte")
        print("la metodología de desarrollo más adecuada.\n")
        time.sleep(1)

        # Tamaño del proyecto
        opciones = {
            '1': ("Pequeño (1-3 meses, equipo de 1-3 personas)", "pequeno"),
            '2': ("Mediano (3-12 meses, equipo de 4-10 personas)", "mediano"),
            '3': ("Grande (más de 12 meses, más de 10 personas)", "grande")
        }
        self.hechos['tamano'] = self.preguntar_con_info(
            "¿Qué tamaño tiene tu proyecto?",
            "Esto ayuda a determinar la complejidad de gestión necesaria",
            opciones
        )

        # Estabilidad de requisitos
        opciones = {
            '1': ("Estables (los requisitos están claros desde el inicio)", "estables"),
            '2': ("Cambiantes (los requisitos evolucionan durante el proyecto)", "cambiantes"),
            '3': ("Muy cambiantes (no sabemos exactamente qué construir)", "muy_cambiantes")
        }
        self.hechos['requisitos'] = self.preguntar_con_info(
            "¿Cómo son los requisitos de tu proyecto?",
            "Esto determina qué tan flexible debe ser la metodología",
            opciones
        )

        # Tipo de contrato
        opciones = {
            '1': ("Precio fijo (presupuesto cerrado, alcance definido)", "fijo"),
            '2': ("Tiempo y materiales (presupuesto flexible)", "variable"),
            '3': ("No aplica / No lo sé", "no_aplica")
        }
        self.hechos['contrato'] = self.preguntar_con_info(
            "¿Qué tipo de contrato tienes con el cliente?",
            "Los contratos de precio fijo funcionan mejor con metodologías tradicionales",
            opciones
        )

        # Experiencia ágil
        self.hechos['experiencia_agil'] = self.preguntar_si_no(
            "¿El equipo tiene experiencia en metodologías ágiles?",
            "Scrum, Kanban, XP son metodologías ágiles. Si no tienen experiencia, mejor empezar con algo simple"
        )
        self.hechos['experiencia_agil'] = 'si' if self.hechos['experiencia_agil'] else 'no'

        # Calidad
        self.hechos['calidad'] = self.preguntar_si_no(
            "¿La calidad del código es un factor crítico?",
            "Proyectos críticos (bancos, salud, etc.) necesitan prácticas como TDD y revisiones de código"
        )
        self.hechos['calidad'] = 'critica' if self.hechos['calidad'] else 'normal'

        # Documentación
        self.hechos['documentacion'] = self.preguntar_si_no(
            "¿El proyecto requiere documentación extensa?",
            "Proyectos que necesitan certificaciones o tienen muchos stakeholders necesitan más documentación"
        )
        self.hechos['documentacion'] = 'importante' if self.hechos['documentacion'] else 'basica'

        # Tipo de proyecto
        self.hechos['tipo'] = 'soporte' if self.preguntar_si_no(
            "¿Es un proyecto de soporte/mantenimiento?",
            "Proyectos de soporte donde entran solicitudes constantes"
        ) else 'desarrollo'

        # Prioridades
        self.hechos['prioridades'] = 'cambian' if self.preguntar_si_no(
            "¿Las prioridades del negocio cambian frecuentemente?",
            "Si el negocio cambia constantemente, necesitas una metodología flexible"
        ) else 'estables'

        # Entregas
        self.hechos['entregas'] = 'continuas' if self.preguntar_si_no(
            "¿Necesitas entregar valor al cliente de forma continua?",
            "Entregas cada 2-4 semanas vs una gran entrega al final"
        ) else 'final'

        # Equipo
        opciones = {
            '1': ("Pequeño (1-5 personas)", "pequeno"),
            '2': ("Mediano (6-15 personas)", "mediano"),
            '3': ("Grande (más de 15 personas)", "grande")
        }
        self.hechos['equipo'] = self.preguntar_con_info(
            "¿De qué tamaño es tu equipo de desarrollo?",
            "Metodologías como XP funcionan mejor con equipos pequeños",
            opciones
        )

    def calcular_certeza_base(self):
        """Calcula una certeza base para evitar resultados vacíos"""
        certeza_base = 0.5  # Certeza mínima para metodología por defecto
        
        # Ajustar según características del proyecto
        if self.hechos['requisitos'] == 'muy_cambiantes':
            return {'Scrum': 0.7, 'XP': 0.6, 'Kanban': 0.5}
        elif self.hechos['requisitos'] == 'estables':
            return {'Waterfall': 0.7, 'Híbrida (Waterfall + Ágil)': 0.6}
        elif self.hechos['tamano'] == 'grande':
            return {'Scrum': 0.65, 'Waterfall': 0.6}
        else:
            return {'Híbrida (Scrum + Kanban)': 0.6, 'Scrum': 0.5}

    def inferir(self):
        print("\n🔍 Analizando tus respuestas...")
        time.sleep(1.5)
        
        # Primero, aplicar reglas normales
        reglas_activadas = False
        for regla in self.reglas:
            cumple = True
            for premisa, valor in regla['premisas']:
                if premisa not in self.hechos or self.hechos[premisa] != valor:
                    cumple = False
                    break
            
            if cumple:
                reglas_activadas = True
                if regla['conclusion'] in self.conclusiones:
                    # Combinar certezas (fórmula de MYCIN)
                    existente = self.conclusiones[regla['conclusion']]
                    nueva = existente + (regla['certeza'] * (1 - existente))
                    self.conclusiones[regla['conclusion']] = nueva
                else:
                    self.conclusiones[regla['conclusion']] = regla['certeza']
                
                self.traza.append(f"✓ Regla {regla['id']}: {regla['conclusion']} (confianza: {regla['certeza']:.0%})")
                print(f"  • Activada: {regla['conclusion']}")
        
        # Si no se activaron reglas, usar certeza base
        if not reglas_activadas:
            print("\n⚠️ No se encontraron coincidencias exactas, usando recomendación base...")
            base = self.calcular_certeza_base()
            for met, cert in base.items():
                self.conclusiones[met] = cert
                self.traza.append(f"✓ Recomendación base: {met} (confianza: {cert:.0%})")
        
        time.sleep(1)

    def mostrar_resultados(self):
        self.limpiar()
        self.mostrar_titulo("📊 RESULTADOS DE LA EVALUACIÓN")
        
        if not self.conclusiones:
            print("\n❌ Error inesperado: No hay conclusiones")
            return
        
        # Ordenar por certeza
        ranking = sorted(self.conclusiones.items(), key=lambda x: x[1], reverse=True)
        
        print("\n🎯 METODOLOGÍAS RECOMENDADAS:\n")
        
        # Mostrar top 3 con gráfico de barras
        for i, (metodologia, certeza) in enumerate(ranking[:3], 1):
            porcentaje = certeza * 100
            barras = int(certeza * 20)  # 20 caracteres máximo
            barra_grafica = "█" * barras + "░" * (20 - barras)
            
            if i == 1:
                medalla = "🥇 "
            elif i == 2:
                medalla = "🥈 "
            else:
                medalla = "🥉 "
            
            print(f"{medalla} {metodologia}")
            print(f"   {barra_grafica} {porcentaje:.1f}% compatible")
            
            # Descripción breve
            if 'Scrum' in metodologia:
                print("   📝 Ideal para proyectos con requisitos cambiantes y entregas frecuentes")
            elif 'Waterfall' in metodologia:
                print("   📝 Perfecta para proyectos con requisitos estables y contratos fijos")
            elif 'Kanban' in metodologia:
                print("   📝 Excelente para equipos de soporte y flujo continuo de trabajo")
            elif 'XP' in metodologia:
                print("   📝 Enfocada en calidad técnica y requisitos muy cambiantes")
            elif 'Híbrida' in metodologia:
                print("   📝 Combinación flexible que se adapta a tus necesidades específicas")
            print()
        
        # Mostrar traza de inferencia
        print("\n🔍 PROCESO DE RAZONAMIENTO:")
        for paso in self.traza:
            print(f"  {paso}")
        
        # Recomendación final
        print("\n" + "="*60)
        print(f"✨ RECOMENDACIÓN FINAL: {ranking[0][0]} con {ranking[0][1]*100:.1f}% de compatibilidad")
        print("="*60)

    def menu(self):
        while True:
            self.limpiar()
            self.mostrar_titulo("🎯 SISTEMA EXPERTO - METODOLOGÍAS DE DESARROLLO")
            print("""
    Este sistema te ayudará a elegir la metodología más adecuada
    para tu proyecto de software analizando características como:
    • Tamaño y tipo de proyecto
    • Estabilidad de requisitos
    • Experiencia del equipo
    • Restricciones del cliente
            """)
            print("\n1. 🔍 Realizar nueva evaluación")
            print("2. ❌ Salir")
            
            op = input("\n👉 Selecciona una opción: ").strip()
            
            if op == '1':
                self.hechos = {}
                self.conclusiones = {}
                self.traza = []
                self.recolectar_datos()
                self.inferir()
                self.mostrar_resultados()
                input("\n📌 Presiona ENTER para volver al menú...")
            elif op == '2':
                print("\n👋 ¡Gracias por usar el sistema! Hasta luego.")
                break
            else:
                print("\n⚠️ Opción inválida, presiona ENTER para continuar...")
                input()

if __name__ == "__main__":
    sistema = SistemaExpertoMetodologias()
    sistema.menu()