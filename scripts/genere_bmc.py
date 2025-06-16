from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_bmc_box(c, x, y, width, height, title, content):
    """Dessine une case du BMC avec titre et contenu."""
    c.rect(x, y, width, height)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x + 10, y + height - 20, title)
    c.setFont("Helvetica", 10)
    lines = content.split("\n")
    for i, line in enumerate(lines):
        c.drawString(x + 10, y + height - 35 - i*15, line)

def create_bmc_rakuten(output_file="rakuten_bmc.pdf"):
    """Génère le BMC pour Rakuten France."""
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Titre
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height - 50, "Business Model Canvas – Rakuten France")

    # Dimensions des cases
    box_width = width/3 - 20
    box_height = (height - 100)/3 - 10

    # Colonne 1
    draw_bmc_box(c, 30, height - 120, box_width, box_height,
                 "Partenaires clés",
                 "Alliances marques\nMarketing d'affiliation\nInstitutions financières\nCréateurs de contenu")
    draw_bmc_box(c, 30, height - 120 - box_height - 10, box_width, box_height,
                 "Activités clés",
                 "Gestion plateforme\nMarketing\nVérification marchands\nGestion paiements/points")
    draw_bmc_box(c, 30, height - 120 - 2*(box_height + 10), box_width, box_height,
                 "Ressources clés",
                 "Plateforme e-commerce\nTechnologie paiement\nBase clients\nID unique")

    # Colonne 2
    draw_bmc_box(c, 30 + box_width + 10, height - 120, box_width, box_height,
                 "Propositions de valeur",
                 "Cashback, points\nSécurité, choix\nPersonnalisation marchands")
    draw_bmc_box(c, 30 + box_width + 10, height - 120 - box_height - 10, box_width, box_height,
                 "Relations clients",
                 "Email support\nConsultants\nFormation\nSelf-service")
    draw_bmc_box(c, 30 + box_width + 10, height - 120 - 2*(box_height + 10), box_width, box_height,
                 "Canaux",
                 "Site/app\nRéseaux sociaux\nEquipe ventes\nEvénements")

    # Colonne 3
    draw_bmc_box(c, 30 + 2*(box_width + 10), height - 120, box_width, box_height,
                 "Segments de clientèle",
                 "Marchands\nConsommateurs")
    draw_bmc_box(c, 30 + 2*(box_width + 10), height - 120 - box_height - 10, box_width, box_height,
                 "Structure de coûts",
                 "Développement\nMarketing\nSupport\nInfrastructure\nPoints")
    draw_bmc_box(c, 30 + 2*(box_width + 10), height - 120 - 2*(box_height + 10), box_width, box_height,
                 "Flux de revenus",
                 "Commissions\nFrais marchands\nFintech\nPublicité")

    c.save()

create_bmc_rakuten()
