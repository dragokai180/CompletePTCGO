from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="bfad2777-0e65-5264-a477-88d5a7fd958e",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandyShocks.Name",
    display_name="Sandy Shocks",
    searchable_by=["Sandy Shocks", "Basic", "Ancient", "SandyShocks"],
    subtypes=["Basic", "Ancient"],
    collector_number=98,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=989,
    abilities=[
        Attack(
            title="Magnetic Burst",
            game_text="If you have 3 or more Energy in play, this attack does 70 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
